import numpy as np
import random
import matplotlib.pyplot as plt
import os
import shutil
import imageio
def get_data():
    calDistance = lambda x, y: np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    points=[(0,1),(4,5),(2,3),(6,7),(8,9),(1,21)]
    N=len(points)
    Mat = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            dv = calDistance(points[i], points[j])
            Mat[i][j], Mat[j][i] = dv, dv
    return points, Mat

def create_data(N, xu=25, yu=25, xd=-25, yd=-25):
    fx = lambda: random.random() * (xu - xd) + xd
    fy = lambda: random.random() * (yu - yd) + yd
    calDistance = lambda x, y: np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

    points = [(0, 0)] * N
    for i in range(N):
        points[i] = (fx(), fy())
    Mat = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            dv = calDistance(points[i], points[j])
            Mat[i][j], Mat[j][i] = dv, dv
    return points, Mat


def calpathValue(path):
    global Mat
    temp = Mat[0][path[0]]
    for i in range(len(path) - 1):
        temp += Mat[path[i]][path[i + 1]]
    temp += Mat[path[-1]][0]
    return temp


def initial():
    global N
    init = list(range(1, N, 1))
    random.shuffle(init)
    packValue = calpathValue(init)
    return init, packValue


def draw(path, pv):
    global points, N, TIMESIT, PNGFILE, PNGLIST
    plt.cla()
    plt.title('cross=%.4f' % pv)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    plt.scatter(xs, ys, color='b')
    xs = np.array(xs)
    ys = np.array(ys)
    plt.plot(xs[[0, path[0]]], ys[[0, path[0]]], color='r')
    for i in range(N - 2):
        plt.plot(xs[[path[i], path[i + 1]]], ys[[path[i], path[i + 1]]], color='r')
    plt.plot(xs[[path[N - 2], 0]], ys[[path[N - 2], 0]], color='r')
    plt.scatter(xs[0], ys[0], color='k', linewidth=10)
    for i, p in enumerate(points):
        plt.text(*p, '%d' % i)
    plt.savefig('%s/%d.png' % (PNGFILE, TIMESIT))
    PNGLIST.append('%s/%d.png' % (PNGFILE, TIMESIT))
    TIMESIT += 1


if __name__ == '__main__':
    # N, Mat = read_data()
    TIMESIT = 0
    PNGFILE = './png/'
    PNGLIST = []
    if not os.path.exists(PNGFILE):
        os.mkdir(PNGFILE)
    else:
        shutil.rmtree(PNGFILE)
        os.mkdir(PNGFILE)


    points, Mat = get_data()
    N=len(points)

    T = 1000  # 起始温度
    alpha = 0.995  # T_{k+1} = alpha * T_k方式更新温度
    limitedT = 1.  # 最小值的T
    iterTime = 1000  # 每个温度下迭代的次数
    K = 0.8  # 系数K
    p = 0
    path, value = initial()
    tempPath, tempValue = [], 0
    global_Best = value  # 画图
    while T > limitedT:
        print(T)
        for i in range(iterTime):
            tempPath = path.copy()
            tx = random.randint(0, N - 2)
            ty = random.randint(0, N - 2)
            if tx != ty:
                tempPath[tx], tempPath[ty] = tempPath[ty], tempPath[tx]
                tempValue = calpathValue(tempPath)
                if tempValue <= value:
                    path = tempPath.copy()
                    value = tempValue.copy()
                else:
                    p = np.exp((value - tempValue) / (K * T))
                    if random.random() < p:
                        path = tempPath.copy()
                        value = tempValue.copy()
        if value < global_Best:
            global_Best = value
            draw(path, value)
        T *= alpha

    print(value)
    print(0, end='-->')
    for i in path:
        print(i, end='-->')

    generated_images = []
    for png_path in PNGLIST:
        generated_images.append(imageio.imread(png_path))
    shutil.rmtree(PNGFILE)  # 可删掉
    generated_images = generated_images + [generated_images[-1]] * 5
    imageio.mimsave('TSP-SAA.gif', generated_images, 'GIF', duration=0.5)
