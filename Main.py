import math
import time
from VecAndFunc import vec2, vec3, vecFunc

h = 28
w = 120
gradient = " .':\"!/r(l1Z4H9W8$@"
screen = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
screen2 = ''
rate = 2
light = vec3.Norm(vec3(-0.5, 0.5, -10))
for i in range(0, 30000):
    screen2 = ''
    for y in range (0, h):
        screen2 = ''
        for x in range(0, w):
            uv = vec2(x, y)
            dimen = vec2(w, h)
            min = vec2(0.5, 0.5)
            uv = vec2.Division(uv, dimen)
            uv = vec2.Minus(uv, min)
            uv.x *= rate
            ro = vec3(-5, 0, 0)
            rd1 = vec3(1, uv.x, uv.y)
            rd = vec3.Norm(rd1)
            ce = vec3(0, 0, 0)
            light = vec3.Norm(vec3(math.sin(i * 0.1), math.cos(i * 0.1), -0.5))
            it = vecFunc.sph(ro, rd, ce, 2)
            if (it.x > 0):
                normale2 = vec3.Multiplication(rd, vec3(it.x, it.x, it.x))
                normale2 = vec3.Plus(normale2, ro)
                normale2 = vec3.Minus(normale2, ce)
                normale = vec3.Norm(normale2)
                diff = vec3.Dot(normale, light)
                if diff < 0:
                    diff = 0
                #diff = diff * 0.9 + 0.1
                s = gradient[int(diff * 19)]
            else:
                s = gradient[1]
            screen2 += s
        screen[y] = screen2
    print(str(''.join(str(x) for x in screen)))