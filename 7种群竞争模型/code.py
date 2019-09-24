import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  # 用以求常微分

plt.rcParams['figure.dpi'] = 100  # 绘图的dpi
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示正负号

# 两个物种的参数
type_x1 = [500, 1.3, 15000, 0.0004]  # [初始数量, 自然增长率, 环境容量, 资源消耗]
type_x2 = [2560, 1.2, 3000, 0.0001]  # 上面资源消耗的意思是：对于可以供养x2的资源，单位数量的x1的消耗为单位数量x2消耗的倍数

# 阻滞作用
def propagate(init, time, x1, x2):
    ix1, ix2 = init
    rx1 = x1[1]*ix1*(1-ix1/x1[2])-x1[3]*ix1*ix2
    rx2 = x2[1]*ix2*(1-ix2/x2[2])-x2[3]*ix1*ix2
    rx = np.array([rx1, rx2])
    return rx

# 画图
def ploter(time, numer):
    plt.xlabel('时间')
    plt.ylabel('物种量')
    plt.plot(time, numer[:,0], "b-", label="物种$x_1$")
    plt.plot(time, numer[:,1], "r-", label="物种$x_2$")
    plt.legend()
    plt.show()

# 运行
time = np.linspace(0, 200, 1000)  # 时间为200个单位，均分为1000份
init = np.array([type_x1[0], type_x2[0]])
numer = odeint(propagate, y0=init, t=time, args=(type_x1, type_x2))
ploter(time, numer)
