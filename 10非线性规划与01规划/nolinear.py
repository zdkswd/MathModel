from scipy.optimize import minimize
import numpy as np


# demo
# 计算  (2+x1)/(1+x2) - 3*x1+4*x3 的最小值  x1,x2,x3的范围都在0.1到0.9 之间
def fun(args):
    a, b, c, d = args
    v = lambda x: (a + x[0]) / (b + x[1]) - c * x[0] + d * x[2]
    return v


def con(args):
    # 约束条件 分为eq 和ineq
    # eq表示 函数结果等于0 ； ineq 表示 表达式大于等于0
    x1min, x1max, x2min, x2max, x3min, x3max = args
    cons = ({'type': 'ineq', 'fun': lambda x: x[0] - x1min},
            {'type': 'ineq', 'fun': lambda x: -x[0] + x1max},
            {'type': 'ineq', 'fun': lambda x: x[1] - x2min},
            {'type': 'ineq', 'fun': lambda x: -x[1] + x2max},
            {'type': 'ineq', 'fun': lambda x: x[2] - x3min},
            {'type': 'ineq', 'fun': lambda x: -x[2] + x3max})
    return cons


if __name__ == "__main__":
    # 定义常量值
    args = (2, 1, 3, 4)  # a,b,c,d
    # 设置参数范围/约束条件
    args1 = (0.1, 0.9, 0.1, 0.9, 0.1, 0.9)  # x1min, x1max, x2min, x2max
    cons = con(args1)
    # 设置初始猜测值
    x0 = np.asarray((0.5, 0.5, 0.5))

    res = minimize(fun(args), x0, method='SLSQP', constraints=cons)
    print(res.fun)
    print(res.success)
