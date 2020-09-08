'''class Div:
    def reminder_zero(self,no):
        self.no=no
        q0 = 0
        q1 = 1
        q2 = 2
        #no = int(input("enter the no"))
        if no%3==0:
            print("Q0 State \n Reminder is:",q0)
        elif no%3==1:
            print("Q1 State \n Reminer is:",q1)
        elif no%3==2:
            print("Q2 State \n reminder is:",q2)
        else:
            print("Not divided by zero")
obj=Div()
print(obj.reminder_zero(26))'''


# Python 3 program to
# check the number is
# divisible by all
# digits are not.

# Function to check
# the divisibility
# of the number by
# its digit.
def checkDivisibility(n, digit):
    # If the digit divides the
    # number then return true
    # else return false.
    return (digit != 0 and n % digit == 0)


# Function to check if
# all digits of n divide
# it or not
def allDigitsDivide(n):
    temp = n
    while (temp > 0):

        # Taking the digit of
        # the number into digit
        # var.
        digit = temp % 3
        if ((checkDivisibility(n, digit)) == False):
            return False

        temp = temp // 3

    return True


# Driver function
n = 30

if (allDigitsDivide(n)):
    print("Yes")
else:
    print("No")

# This code is contributed by Nikita Tiwari.

