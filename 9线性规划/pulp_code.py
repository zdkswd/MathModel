import pulp

# 目标函数的系数
z = [2, 3, 1]
# 约束
a = [[1, 4, 2], [3, 2, 0]]
b = [8, 6]
# 确定最大化最小化问题，最大化只要把Min改成Max即可
m = pulp.LpProblem(sense=pulp.LpMinimize)
# 定义三个变量放到列表中
x = [pulp.LpVariable(f'x{i}', lowBound=0) for i in [1, 2, 3]]
# 定义目标函数，lpDot可以将两个列表的对应位相乘再加和
# 相当于z[0]*x[0]+z[1]*x[0]+z[2]*x[2]
m += pulp.lpDot(z, x)

# 设置约束条件
for i in range(len(a)):
    m += (pulp.lpDot(a[i], x) >= b[i])
# 求解
m.solve()
# 输出结果
print(f'优化结果：{pulp.value(m.objective)}')
print(f'参数取值：{[pulp.value(var) for var in x]}')
