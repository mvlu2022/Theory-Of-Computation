while True:
    user_input = input("Please Enter your string: ")
    if user_input == 'x':
        break
    q0 = True
    q1 = False
    q2 = False
    q3 = False
    accept = False
    a = ('Accepted')
    b = ('Not Accepted')
    pointer = 0
    end_with_101 = False

    # Check if the string ends with '101'
    if user_input.endswith('101'):
        end_with_101 = True
    else:
        print("The string should end with '101'.")
        continue

##    # Check if the string starts with '101' or contains '101' in the middle
##    if user_input.startswith('101') or '101' in user_input[1:-2]:
##        print("The string cannot start with '101' or contain '101' in the middle.")
##        continue

    while True:
        try:
            string = user_input[pointer]
            if string == '0':
                if q0:
                    accept = False
                    print("String on the q0 state")
                    print(a if accept else b)
                elif q1:
                    q1 = False
                    q2 = True
                    accept = False
                    print("String on the q2 state")
                    print(a if accept else b)
                elif q2:
                    q2 = False
                    q0 = True
                    accept = False
                    print("String on the q0 state")
                    print(a if accept else b)
                elif user_input=='101':
                    accept=True
                    print('String on the q2 state')
                    print(a if accept else b)
                else:
                    print("Something went wrong for 0 string")
            elif string == '1':
                if q0:
                    q0 = False
                    q1 = True
                    accept = False
                    print("String on the q1 state")
                    print(a if accept else b)
                elif q1:
                    accept = False
                    print("String on the q1 state")
                    print(a if accept else b)
                elif q2:
                    q2 = False
                    q3 = True
                    accept = True
                    print("String on the q3 state")
                    print(a if accept else b)
                elif q3:
                    q3 = False
                    q1 = True
                    accept = False
                    print("String on the q1 state")
                    print(a if accept else b)
                else:
                    print("Something went wrong for 1 string")
            else:
                print("Please Enter A Valid Input. The input should be BINARY.")
            pointer += 1
        except IndexError:
            break

    # Check if the string ends with '101' and is accepted
    if end_with_101 and accept:
        print("The string is accepted.")
    else:
        print("The string is not accepted.")
