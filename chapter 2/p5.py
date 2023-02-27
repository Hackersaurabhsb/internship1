principle=int(input("Enter the principle : "))
rate=float(input("Enter the rate : "))
time=int(input("Enter the time : "))
def calculate(p,r,t):
    print("Amount\t\tInterest\tEnd Amount")
    print("=====================================================")
    for i in range(1,t+1):
        intrst=(p*r*i)/100
        end=p+intrst
        print(format(p,".2f"),'|\t',format(intrst,".2f"),'|\t',format(end,".2f"))
        p=p+intrst
calculate(principle, rate, time)