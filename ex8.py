#daydayupq1.py
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))
#daydayup2.py
dayfactor = 0.005
dayup2 = pow(1+dayfactor,365)
daydown2 = pow(1+dayfactor,365)
print("向上：{:.2f},向下{:.2f}".format(dayup2,daydown2))