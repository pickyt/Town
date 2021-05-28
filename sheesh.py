import math
import time

def chudapprox(n):
    approx=1
    for i in range(0,n):
        approx += (pow(-1,n)*math.factorial(6*n)*(13591409+545140134*n))/(math.factorial(3*n)*pow(math.factorial(n),3)*pow(640320,3*n+3/2))
        i+=1
    return 1/(12*approx)


def rampiapprox(n):
    approx = 0
    for i in range(0,n):
        approx += (math.factorial(4*i)*(1103+26390*i))/(pow(math.factorial(i),4)*pow(396,4*i))
        i+=1
    return 1/((2*math.sqrt(2)/9801)*approx)


def stats(n,arg):
    for i in range(1,n+1):
        t = time.time()
        if arg == "ram":
            print (rampiapprox(i),"PI offset = ", math.pi-rampiapprox(i), " in ",time.time()-t,"seconds")
        if arg == "chud":
            print (chudapprox(i),"PI offset = ", math.pi-chudapprox(i), " in ",time.time()-t,"seconds")

stats(1,"ram")
