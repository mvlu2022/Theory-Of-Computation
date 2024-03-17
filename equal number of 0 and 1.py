while True:
    user_input=input("Please Enter Your String: ")
    if user_input=='x':
        break
    count_ones=0
    count_zeros=0
    for char in user_input:
        if char=='0':
            count_zeros+=1
        elif char=='1':
            count_ones+=1
        else:
            print(" valid input:",char)
    print('count of zero is :',count_zeros)
    print('count of ones is :',count_ones)
    if count_zeros==count_ones:
        print("Accepted")
    else:
        print("Not Accepted")
        
