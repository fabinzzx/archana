try:
    num1=int(input("enter numerator:"))
    num2=int(input("enter denominator:"))
    result=num1/num2
    print("result:",result)
except ZeroDivisionError:
 print("error:cannot divide by zero!")
except ValueError:
    print("error:please enter valid integers.")