#End with 101
states={'A':{'0':'A','1':'B'},'B':{'0':'C','1':'B'},'C':{'0':'A','1':'D'},'D':{'0':'C','1':'B'}}
initial_state='A'
final_state='D'
while True:
    user_input=input("Please Enter Your String(x for exit) : ")
    if user_input=='x':
        break
    current_state=initial_state
    for i in user_input:
        current_state=states[current_state][i]
    if current_state==final_state:
        print("Accepted")
    else:
        print('not Accepted')
