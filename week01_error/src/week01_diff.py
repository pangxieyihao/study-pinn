import os
import math
import csv
base_dir=os.path.dirname(os.path.abspath(__file__))
def f(x):
    return math.sin(x)
def forward(x,h):
    return (f(x+h)-f(x))/h
def central(x,h):
    return (f(x+h)-f(x-h))/(2.0*h)
def main():
    x0=math.pi/4.0
    exact=math.cos(x0)
    hs=[]
    for k in range(1,9):
        hs.append(10 ** (-k))
    rows=[]
    print("前向差分")
    for h in hs:
        approx=forward(x0,h)
        error=abs(approx-exact)
        print("h={:.0e} 近似={:.16f} 误差={:.16e}".format(h,approx,error))
        rows.append([h,approx,error,None,None])
    print("中心差分")
    for i in range(len(hs)):
        h=hs[i]
        approx=central(x0,h)
        error=abs(approx-exact)
        print("h={:.0e} 近似={:.16f} 误差={:.16e}".format(h,approx,error))
        rows[i][3]=approx
        rows[i][4]=error

    csv_path=os.path.join(base_dir,"diff.csv")
    with open(csv_path,"w",newline="")as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(["h","forward_approx","forward_error","central_approx","central_error"])
        for row in rows:
            writer.writerow(row)
if __name__=="__main__":
    main()
