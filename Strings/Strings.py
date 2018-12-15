# Reverse a String Method 1
name ="lalan"
name1 = ""
for i in range(len(name)-1,-1,-1):
    name1+=name[i]
print (name1);

# Reverse a String Method 2
name ="lalan"
print("".join(reversed(name)))

#Reverse words in a given string
Myname = "lalan punith"
myname = Myname.split(" ");
word = []

for Word in myname:
    word.insert(0,Word);

print("Reversed String")
print(" ".join(word))


# Reverse the String According to the no of words

Words ="lalan punith raaj ramya mukesh"
Mywords = Words.split(" ");
List = []
if len(Mywords)%2==0:
    for i in range(0 , len(Mywords)):
        if i % 2 != 0:
            List.insert(i,"".join(reversed(Mywords[i])))
        else:
            List.insert(i, Mywords[i])
else:
    for i in range(0,len(Mywords)):
        if i % 2 == 0:
            List.insert(i, "".join(reversed(Mywords[i])))
        else:
            List.insert(i, Mywords[i])
print (" ".join(List))


# Reverse middle words of a string

Words ="lalan punith raaj ramya mukesh"
Mywords = Words.split(" ")
Str=[];
for i in range(len(Mywords)):
    if(i==0 or i==len(Mywords)-1):
        Str.insert(i, Mywords[i])
    else:
        Str.insert(i, "".join(reversed(Mywords[i])))
print(" ".join(Str))

# Swap corner words and reverse middle characters
Words ="lalan punith raaj ramya mukesh"
Mywords = Words.split(" ")
Str1=[];
temp=Mywords[0]
Mywords[0]=Mywords[len(Mywords)-1]
Mywords[len(Mywords)-1]=temp
for i in range(len(Mywords)):
    if(i==0 or i==len(Mywords)-1):
        Str1.insert(i, Mywords[i])
    else:
        Str1.insert(i, "".join(reversed(Mywords[i])))
print(" ".join(Str1))