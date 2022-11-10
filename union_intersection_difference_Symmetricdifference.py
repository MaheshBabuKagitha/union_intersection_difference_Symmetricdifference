#union=all values
#differece= A/B values which are not in B/A
#intersection = common values in two lists
#symmetric difference = all numbers except intersection values


#two empty lists to collect data from user 
List1=[]
List2=[]

# collect  list-1 data with while loop until user entered nothing
while True:
    number=input("Enter Number in List 1: ")
    #exception handling to avoid Error from user input 
    try:
        if number=="":
            break
        else:
            number=int(number)
            List1.append(number)
    except:
        print("Invlaid input")

# collect list-2 data with while loop until user entered nothing
while True:
    number=input("Enter Number in List 2: ")
    #exception handling to avoid Error from user input 
    try:
        if number=="":
            break
        else:
            number=int(number)
            List2.append(number)
    except:
        print("Invlaid input")


def union():
    All=[]
    for i in List1 :
        #add number if not repeated
        if i not in All:
            All.append(i)
    for j in List2:
        #add number if not repeated
        if j not in All:
            All.append(j)
    print("\n\n",50*"*","\nUNION NUMBERS in LIST-1 and LIST-2 NUMBERS :",end="")
    #arrange in assending order
    All.sort()
    print(All)

def diff():
    dif1=[]
    dif2=[]
    for i in List1:
        # consider number if not repeated
        if i not in dif1:
            # if number not in another list of numbers add to lsit
            if i not in List2:
                dif1.append(i)
    for k in List2:
        # consider number if not repeated
        if k not in dif2:
            # if number not in another list of numbers add to list
            if k not in List1:
                dif2.append(k)
    #arrange in assending order
    dif1.sort()
    dif2.sort()
    print("\nDIFFERENCE in LIST=1 from LIST-2 NUMBERS :",dif1)
    print("DIFFERENCE in LIST=2 from LIST-1 NUMBERS :",dif2)

def intersection():
    inter=[]
    for i in List1:
        # consider number if not repeated
        if i not in inter:
            # consider if number present in another list of numbers
            if i in List2:
                inter.append(i)
    inter.sort()
    print("\nINTERSECTION common NUMBERS :",inter)

def symmetric():
    sym=[]
    for i in List1:
        # consider number if not repeated
        if i not in sym:
            # consider if number not in another list
            if i not in List2:
                sym.append(i)
    for j in List2:
        # consider number if not repeated
        if j not in sym:
            # consider if number not in another list
            if j not in List1:
                sym.append(j)
    sym.sort()
    print("\nSYMMETRIC NUMBERS : ",sym,"\n\n",50*"*")

#call all functions
union()
diff()
intersection()
symmetric()