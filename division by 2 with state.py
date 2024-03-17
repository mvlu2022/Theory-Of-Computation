print("Abhishek Gautam")
while True:
    user_input=input("Please Enter Your String: ")
    if user_input=='x':
        break
    q0=True
    q1=False
    accept=False
    a=('Accepted')
    b=('Not Accepted')
    pointer=0
    while True:
        try:
            string=user_input[pointer]
            if string=='0':
                if q0==True:
                    accept=True
                    print("on the q0 state")
                    print(a if accept else b)
                elif q1==True:
                    q0=True
                    accept=True
                    print('on the q0 state')
                    print(a if accept else b)
                else:
                    print("Somthing went wrong for 0")
            elif string=='1':
                if q0==True:
                    q1=True
                    accept=False
                    print('on the q1 state')
                    print(a if accept else b)
                elif q1==True:
                    accept=False
                    print('on the q1 string')
                    print(a if accept else b)
                else:
                    print('Sonthing went wrong for 1')

            else:
                print('invalid string :')
            pointer+=1
        except IndexError:
            break
                
                    
                
            
