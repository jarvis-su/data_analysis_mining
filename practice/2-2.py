# - * - coding:utf-8 -*
# 求解非线性方程组
from scipy.optimize import  fsolve #导入求解方程组的函数

def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 -1,x1**2 - x2 -2]

result = fsolve(f,[1,1]) # 输入初值[1,1] 并求解
print(result)


