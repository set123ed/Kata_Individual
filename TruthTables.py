
enouns = input("introduzca el enunciado deseado: ").replace(" ","")
lowerenouns = enouns.lower()
uniquelist = []
count = 0
# a || b && !c
def Findvocals(enouns, uniquelist):
    enouns = enouns.replace("&&","")
    enouns = enouns.replace("||","")
    enouns = enouns.replace("^","")
    enouns = enouns.replace("!","")

    for x in enouns:
        if x not in uniquelist:
            uniquelist.append(x)
    return uniquelist

find = Findvocals(enouns,uniquelist)

def CountVocals(enouns,count):
    enouns = enouns.replace("&&","")
    enouns = enouns.replace("||","")
    enouns = enouns.replace("^","")
    enouns = enouns.replace("!","")
    
    uniquelist = []
    for x in enouns:
        if x not in uniquelist:
            uniquelist.append(x)
    for i in uniquelist:
        count += 1
    return count

counter = CountVocals(enouns,count)

def TruthTables(lowerenouns,count, uniquelist):
    lowerenouns = lowerenouns.replace("&&","&")
    lowerenouns = lowerenouns.replace("||","|")
    lowerenouns = lowerenouns.replace("xor","^")
    lowerenouns = lowerenouns.replace("!","~")
    countertimes = 0

    if(count == 2 ):
        (uniquelist[0] + "\t"  + uniquelist[1] +"\t" + lowerenouns + "\t")
        lowerenouns = lowerenouns.replace(uniquelist[0],"a")
        lowerenouns = lowerenouns.replace(uniquelist[1],"b")
        for a in range(0,2):
            for b in range (0,2):
                x = eval(lowerenouns)
                (str(a) + "\t"  + str(b) +"\t" + str(x) + "\t")
                countertimes += 1
    

    if(count == 3 ):
        (uniquelist[0] + "\t"  + uniquelist[1] +"\t" + lowerenouns + "\t")
        lowerenouns = lowerenouns.replace(uniquelist[0],"a")
        lowerenouns = lowerenouns.replace(uniquelist[1],"b")
        lowerenouns = lowerenouns.replace(uniquelist[2],"c")

        for a in range(0,2):
            for b in range (0,2):
                for c in range (0,2):
                    x = eval(lowerenouns)
                    (str(a) + "\t"  + str(b) +"\t" + str(c) + "\t"+ str(x))
                    countertimes += 1
    if(count == 4 ):
        (uniquelist[0] + "\t"  + uniquelist[1] +"\t" + lowerenouns + "\t")
        lowerenouns = lowerenouns.replace(uniquelist[0],"a")
        lowerenouns = lowerenouns.replace(uniquelist[1],"b")
        lowerenouns = lowerenouns.replace(uniquelist[2],"c")
        lowerenouns = lowerenouns.replace(uniquelist[3],"d")
        for a in range(0,2):
            for b in range (0,2):
                for c in range (0,2):
                    for d in range (0,2):
                        x = eval(lowerenouns)
                        (str(a) + "\t"  + str(b) +"\t" + str(c) + "\t"+ str(d)+"\t" + str(x))
                        countertimes += 1
    if(count == 5 ):
        (uniquelist[0] + "\t"  + uniquelist[1] +"\t" + lowerenouns + "\t")
        lowerenouns = lowerenouns.replace(uniquelist[0],"a")
        lowerenouns = lowerenouns.replace(uniquelist[1],"b")
        lowerenouns = lowerenouns.replace(uniquelist[2],"c")
        lowerenouns = lowerenouns.replace(uniquelist[3],"d")
        lowerenouns = lowerenouns.replace(uniquelist[4],"e")
        for a in range(0,2):
            for b in range (0,2):
                for c in range (0,2):
                    for d in range (0,2):
                        for e in range (0,2):
                            x = eval(lowerenouns)
                            (str(a) + "\t"  + str(b) +"\t" + str(c) + "\t"+ str(d)+"\t" + str(e) +"\t" + str(x))
                            countertimes += 1
    print(countertimes)

TruthTables(lowerenouns,counter,uniquelist)
