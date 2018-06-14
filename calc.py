# calculator :
# addition,multiplication,subtraction,square,division
# use loops, functions, try:except

def add(n1,n2) :
    return (n1+n2)

def sub(n1,n2):
    return (n1-n2)

def mul(n1,n2):
    return (n1*n2)

def div(n1,n2):
        return float(n1/n2)

def sqr(n1):
    return (n1**2)

def input_prompt() :
        try :
            n1 = float(input("n1>> "))
            return n1
        except :
            print('Enter a proper value!')
            return input_prompt()

onoff = 1
while onoff :
    print("*************************")
    print("Select your operation : ")
    print("[1] Addition")
    print("[2] Subtration")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Square")
    print("[6] Exit")
    print("*************************")
    try :
        selec = int(input("Enter your selection : "))
    except ValueError :
        print("Enter a proper selection!")
        continue
    if(selec == 1) :
        n1 = input_prompt()
        n2 = input_prompt()
        res = add(n1,n2)
        print("Result : ")
        print(str(n1)+" + "+str(n2)+" = "+ str(res))
        
    elif(selec == 2) :
        n1 = input_prompt()
        n2 = input_prompt()
        res = sub(n1,n2)
        print("Result : ")
        print(str(n1)+" - "+str(n2)+" = "+ str(res))
    
    elif(selec == 3) :
        n1 = input_prompt()
        n2 = input_prompt()
        res = mul(n1,n2)
        print("Result : ")
        print(str(n1)+" * "+str(n2)+" = "+ str(res))
    
    elif(selec == 4) :
        n1 = input_prompt()
        n2 = input_prompt()
        try :
            res = div(n1,n2)
        except ZeroDivisionError :
            print('Divide by Zero error')
            continue
        print("Result : ")
        print(str(n1)+" / "+str(n2)+" = "+ str(res))
    
    elif(selec == 5) :
        n1 = input_prompt()
        res = sqr(n1)
        print("Result : ")
        print(str(n1) + "^2 = " + str(res))
        
    elif(selec == 6) :
        print('Exiting.........')
        onoff=0
    
    else:
        print("Enter a proper selection!")
        continue

            
        
            
