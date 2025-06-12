
x = int(input("enter the number: "))


def isdivbytwo(x):
    if x==1:
        print("true")
        return True
    if x < 1:
        return False
    else:
        isdivbytwo(x/2)

isdivbytwo(x)