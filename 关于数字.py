#用列表生成100以内能被3整除的数
list1 =[]
for i in range (1,100):
    if i % 3 ==0:
        list1.append(i)
print ("100以内能被3整除的数：",list1)

#完全平方数
#10000以内的一个整数，它加上100后是一个完全平方数，
#再加上168又是一个完全平方数，请问该数是多少？ 
for i in range (1,10000):
    for j in range(1,100):
        if j*j ==i +100:
           for k in range (1,10000):
                if k*k ==i + 168:
                   print (j,k)
                   print(i)
                   break


#输出100以内质数
for i in range (2,101):
    for m in range(2,i):
        if i%m==0:
           break
    else:
        print(i,end= " ")
        #if m ==i-1:
           # print(i,end =" ")
       
#用列表切片判断素数
primes = [1]*100
primes [0:2] = [0,0]
for i in range (2,100):
    if primes[i] ==1:
        for j in range (i+1,100):
            if primes [j]!= 0 and j % i == 0 :
                primes [j] = 0
print ("100以内的素数包括：")
for i in range (2,100):
    if primes [i]:
        print(i ,end = ' ')

#判断素数
i=eval(input("数字"))
for m in range(2,i):
    if i%m==0:
        print("不是素数")
        break            
else:
    print("素数")        


#用列表切片判断素数
primes = [1]*300
primes [0:2] = [0,0]
for i in range (2,300):
    if primes[i] ==1:
        for j in range (i+1,300):
            if primes [j]!= 0 and j % i == 0 :
                primes [j] = 0
print ("300以内的素数包括：")
for i in range (2,300):
    if primes [i]:
        print(i ,end = ' ')

#输出100以内的偶数
for i in range(0,101):
    if i%2==0:
        print(i)


i =0
while i <=100:
    print(i,end=" ")
    i+=2

'''
for i in range (101,1000):
    if i %  10==5 and i % 3==0 :
        print (i)
'''

#数列求和
fenzi = 1
fenmu = 3
s = 1
for i in range (int(input("请输入你想计算几项："))-1):
    s = fenzi/fenmu + s
    fenmu +=2
    fenzi = (-1)**(i+1)
print(s)

#数列求和
fenzi=2
fenmu=1
sum=0
for i in range(20):
     sum=fenzi/fenmu+sum
     temp=fenmu#前一项分母
     fenmu=fenzi#本项的分母
     fenzi=temp+fenzi#本项的分子
print(sum)

#无重复的三位数
for i in range(1,5):
    for j in range(1,5 ):
        for k in range(1,5):
          if(i!=j and i!=k and j!=k ):
           print(i*100+j*10+k)

""" for i in range(1,10): """
"""   for j in range(1,i+1): """
"""     print(j,"X",i,"=",i*j,end=" ") """
"""   print(end='\n')   """
#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(i,j,j*i),end=" ")#:2右对齐，end=" "换行符
    print("")  

#############################
    #阶乘  普通循环
x = int (input("请输入一个数："))
a = 1
for i in range (1,x+1):
    a = a *i
print(a)
#用函数循环
def f(n):
    r = 1
    if n <=1:
        if  n==0 or n==1:
            return 1
        else:
            return "n不能小于0"
    else:
        for i in range (1,n+1):
            r*=i
        return r 
print(f(-3))  
print(f(3))

#用函数递归
def f(n):
    if n <= 1:
        if n == 0 or n==1:
           return 1
        else:
           return "n不能小于0"
    else:
        return n *f(n-1)

#f(3)  #不能直接调用
print(f(-3))
#n的阶乘
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
print(f(4))
####################################

