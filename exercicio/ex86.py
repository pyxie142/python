temp = []
princ = []
mai = men = []
while true:
    temp.append(str(input('nome')))
    temp.append(float(input('peso')))
    if len (princ)==0:
        mai=men=temp[1]
    else:
        if temp [1]>mai:
            mai = temp [1]
        if temp [1]<men:
            men = temp [1]
        princ.append(temp[:])
        temp. clear ()           