import re
print('''Consider the grammar G given by S->OSA2. S->012, 2A->A2,
A->11. Test whether (a) 00112 E L(G)''')
str1='00112'
S1='0SA2'
S2='012'
C='A2' #take 2A=C
D='11' #take 1A=D
find=re.search('S',S1)
if find:
    step1=S1.replace('S',S2) # replace is an inbuild method for replace string.
    print('string is : ',step1,'\nThis is not accepting because in the last we have A2 & 2A so this is meaningless')
    print('if we take value 2A=1 then it is Acceptabel')

find1=re.search('2A',step1)
if find1:
    
    step2=step1.replace('2A','1')
    if str1==step2:
        print('now E L(G):', step2)


