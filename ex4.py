#多层缩进
import random
DARTS = 1000
hits = 0.0
#clock()
for i in range(1,DARTS):
    x,y = random(),random()
    dist = sprt(x**2 + y**2)
    if dist <= 1.0:
        #此处是多层缩进
        hits = hits + 1
    pi = 4*(hits/DARTS)
    print("pi的值是{:.2f}F.format(pi)")
