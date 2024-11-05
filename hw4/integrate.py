import numpy as np
import random

def f(x,y,z):
    return 3*x**2+y**2+2*z**2

step = 0.01 #跑比較快

def integrate(f, rx, ry, rz):
    area = 0
    for x in np.arange(rx[0], rx[1], step):
        for y in np.arange(ry[0], ry[1], step):
            for z in np.arange(rz[0], rz[1], step):
                area += f(x,y,z)*step*step*step
    return area

#ChatGPT
def integrate2(f, rx, ry, rz):
    x = np.arange(rx[0], rx[1], step)
    y = np.arange(ry[0], ry[1], step)
    z = np.arange(rz[0], rz[1], step)
    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")  # 建立 3D 網格
    volume_elements = f(X, Y, Z) * step**3  # 每個體積元素的值
    area = np.sum(volume_elements)  # 加總所有體積元素
    return area


print(integrate(f, [0,1], [0,1], [0,1]))
print(integrate2(f, [0,1], [0,1], [0,1]))

lower = 0
upper = 6 # (3x^2+y^2+2z^)

def mcIntegrate(f, rx, ry, rz,n = 100000):
    hits = 0
    for i in range(n):
        x = random.uniform(rx[0], rx[1])
        y = random.uniform(ry[0], ry[1])
        z = random.uniform(rz[0], rz[1])
        m = random.uniform(lower, upper)
        if f(x,y,z) > m:
            hits += 1
    return (rx[1] - rx[0]) * (ry[1] - ry[0]) * (rz[1] - rz[0]) * (upper - lower) * (hits / n)

print(mcIntegrate(f, [0,1], [0,1], [0,1]))