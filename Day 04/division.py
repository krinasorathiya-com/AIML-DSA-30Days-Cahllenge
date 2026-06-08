def division(num1,num2):
    if(num2==0):print("Zero Division Error:  ")
    else:
        a=num1/num2
        print(f"division is:{a}")
        return a
division(20,10)
division(10,20)
division(-30,90)
division(90,0)