t = int(input("Enter the number: "))
def fact(n):
    if (n==1) or (n==0):
        return 1
    elif n<0:
        print("Negative numbers can't be factorised")
    else:
        return n*(fact(n-1))

ru=fact(t)
print(ru)