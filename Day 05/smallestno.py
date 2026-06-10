def small(a,b,c):
    if(a<c or a<b):
        print(f"{a} is smallest number in this all number.")
    elif(b<c or b<a):
        print(f"{b} is the smallest number in this all number.")
    elif(c<a or c<b):
        print(f"{c} is smallest number in this all number.")

small(-99,23,56)
small(0,-45,56785)
small(99,45,8)



    