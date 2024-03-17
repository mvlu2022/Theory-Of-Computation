import re
'''Consider G whose productions are S ->aAS|a, A->SbA|SS|ba. Show that
S ==> aabbaa and construct a derivation tree whose yield is aabbaa.'''
S1='aAS'
S2='a'
A1='SbA'
A2='SS'
A3='ba'
search1=re.search('aAS',S1)
if search1:
    var1=S1.replace('A','SbA')
    print(S1,' -> ',var1)
search2=re.search('S',var1)
if search2:
    var2=var1.replace('S','a')
    print(S1,' -> ',var1,' -> ',var2)
search3=re.search('A',var2)
if search3:
    var3=var2.replace('A','ba')
    print(S1,' -> ',var1,'-> ',var2, '-> ',var3)
search4=re.search('S',var3)
if search4:
    var4=var3.replace('S','a')
    print(S1,' --> ',var1,' --> ',var2,' --> ',var3,'--> ',var4) 
    
