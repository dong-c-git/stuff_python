try :
    num = eval(input("请输入一个整数："))
    print(num**2)
except NameError:
    print("输入不是整数")
else:
    a = num**3
    print("{}的3次方是：{}".format(num,a))
finally:
    print("finally执行部分！")




