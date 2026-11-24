m=int(input("Enter Your Marks"))
if m>100 or m<0:
    print("Invalid Marks!!!")
elif m>=90 and m<=100:
    print("A Grade")
elif m>=75 and m<=89:
    print("B Grade")
elif m>=60 and m<=74:
    print("C Grade")
elif m>=40 and m<=59:
    print("D Grade")
else:
    print("FAIL")