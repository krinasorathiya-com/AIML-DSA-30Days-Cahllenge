def substraction(num1,num2):
    sub=num1-num2
    if(sub<0):
        print(f"sub : {sub}")
        return num2-num1
    else:
        print(f"sub :{sub}")
        return num1-num2
substraction(20,10)
substraction(10,20)    