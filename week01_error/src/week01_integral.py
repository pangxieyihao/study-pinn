import os
import math
import csv

def f(x):
    return math.sin(x)
def trapezoid(a,b,n):
    h=(b-a)/n
    total=f(a)+f(b)
    for i in range(1,n):
        x=a+i*h
        total=total+2.0*f(x)
    return total*h/2.0

def simpson(a,b,n):
    h=(b-a)/n
    total=f(a)+f(b)
    for i in range(1,n):
        x=a+i*h
        if i%2==0:
            total=total+f(x)*2.0
        else:
            total=total+f(x)*4.0
    return total*h/3.0
def main():
    a=0.0
    b=math.pi
    ns=[4,8,16,32,64]
    rows=[]
    exact=2.0
    print("区间[0,pi],精确值=",exact)
    for n in ns:
        trap=trapezoid(a,b,n)
        trap_error=abs(trap-exact)
        simp=simpson(a,b,n)
        simp_error=abs(simp-exact)
        print("N=",n)
        print("梯形 近似值={:.16f}  误差={:.6e}".format(trap,trap_error))
        print("SIMPSON  近似值={:.16f}  误差={:.6e} ".format(simp,simp_error))
        rows.append([n,trap,trap_error,simp,simp_error])
    base_dir=os.path.dirname(os.path.abspath(__file__))
    csv_path=os.path.join(base_dir,"intergal_result.csv")
    with open(csv_path,"w",newline="")as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(["N","trap_qpprox","trap_error","simp_approx","simp_error"])
        for row in rows:
            writer.writerow(row)

if  __name__ == "__main__":
     main()
