#daydayupq1.py
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))
#daydayup2.py
dayfactor = 0.005
dayup2 = pow(1+dayfactor,365)
daydown2 = pow(1+dayfactor,365)
print("向上：{:.2f},向下{:.2f}".format(dayup2,daydown2))
#daydayup3.py
dayup3 = 1.0
dayfactor3 = 0.01
for i in range(365):
    if i % 7 in[6,0]:
        dayup3 = dayup3*(1-dayfactor3)
    else:
        dayup3 = dayup3*(1+dayfactor3)
print("工作日的力量为:{:.2f}".format(dayup3))