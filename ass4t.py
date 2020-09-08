q0=0
q1=1
q2=2
'''l=[0,1,2,3,4,5,6,7,8,9]
s1=0,3,6,9
s2=1,4,7
s3=2,5,8
l1=[0,3,6,9]
l2=[1,4,7]
l3=[2,5,8]'''
a=int(input())
for i in range(a):
    n=int(input("Enter no"))
    if n%3==0:
      print("Q0 State")
    elif n%3==1:
        print("Q1 state")
    elif n%3==2:
        print("Q2 State")
    else:
        print("Invalid data")

