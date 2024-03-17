while True:
    user_input = input("Enter your String : ")
    if user_input=='x':
        break
    atQ0 = True
    atQ1 = False
    atQ2 = False
    atQ3 = False
    AcceptIt = False
    a = "Accepted"
    b = "Not accepted"
    pointer =0
    while True:
        try:
            stringwa = user_input[pointer]
            if stringwa == "0":
                if atQ0 == True:
                    AcceptIt = False
                    print("At State Q0\t" ,end='')
                    print(a if AcceptIt else b)
                elif atQ1 == True:
                    atQ1 = False
                    atQ0 = True
                    AcceptIt = False
                    print("At State Q0\t",end='')
                    print(a if AcceptIt else b)
                elif atQ2 == True:
                    atQ0 = True
                    atQ2 = False
                    AcceptIt =False
                    print("At State Q0\t",end='')
                    print(a if AcceptIt else b)
                elif atQ3 == True:
                    AcceptIt = False
                    print("At state Q0\t",end='')
                    print(a if AcceptIt else b)
                else :
                    print("zero block mai gadbad hai")
            elif stringwa ==  "1":
                if atQ0 == True:
                    atQ0 = False
                    atQ1 = True
                    AcceptIt = False
                    print("At State Q1\t",end='')
                    print(a if AcceptIt else b)
                elif atQ1 == True:
                    atQ2 = True
                    atQ1 = False
                    AcceptIt = False
                    print("At State Q2\t",end='')
                    print(a if AcceptIt else b)
                elif atQ2 == True:
                    atQ3 = True
                    atQ2 = False
                    AcceptIt = True
                    print("At State Q3\t",end='')
                    print(a if AcceptIt else b)
                elif atQ3 == True:
                    atQ3 = False
                    atQ1 = True
                    AcceptIt = False
                    print("At State Q0\t",end='')
                    print(a if AcceptIt else b)
                else :
                    print("one wale mai gadbad hai")
            
            else:
                print("Invalid input")
            pointer +=1
        except IndexError:
            break
