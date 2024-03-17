input_string=input("Please Enter Your String: ")
if all(char in '01' for char in input_string):
    token=list(input_string)
    print("Tokenization value is: ",token)
else:
    print("Enter A valid string")
