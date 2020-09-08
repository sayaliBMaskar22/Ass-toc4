class Digit:
    def mod():
        num=int(input("How many no u want to check:"))
        for i in range(num):
            n=int(input("Enter no:"))
            mod=n%10
            print('mod:',mod)
            n1=n//10
            print("rem:",n1)
            t=mod
            t1=n1
            if t%3==0:
                print("Q0 state")
            elif t%3==1:
                print("Q1 state")
            elif t%3==2:
                print("Q2 state")
o=Digit.mod()
