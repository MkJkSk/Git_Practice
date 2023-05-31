def Number_Checker(a):


    if a>0 and a<=100:
        print("Your Given Number is Postive")

    elif a<0 :
        print("Your Given Number is Negative")

    elif a>100:
        print("Your Given Number is purely Positive +ve")

    else:
        print("Your Given Number is Zero")


a = int(input("Enter Your Number:\n"))
Number_Checker(a)
