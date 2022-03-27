import datetime

def uniquecode():
    temp=datetime.datetime.now()
    temp1=str(temp)
    temp1.strip()
    unq=""
    for x in temp1:
        if x!='-' and x!=":" and x!=" " and x!=".":
            unq=unq+x
    return unq
