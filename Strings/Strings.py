name ="lalan"
name1 = ""
for i in range(len(name)-1,-1,-1):
    name1+=name[i]
print (name1);

Myname = "lalan punith"
myname = Myname.split(" ");
word = []

for Word in myname:
    word.insert(0,Word);
    print (word)

print("Reversed String")
print(" ".join(word))


# Reverse the String According to the no of words

Words ="lalan punith raaj ramya mukesh"
Mywords = Words.split(" ");
List = []
if len(Mywords)%2==0:
    for i in range(0 , len(Mywords) , 1):
        if i % 2 != 0:
            print(str(Mywords[i]))
            List.insert(i,"".join(reversed(Mywords[i])))
        else:
            List.insert(i, Mywords[i])
else:
    for i in range(len(Mywords)):
        if i % 2 == 0:
            print (i)
            List.insert(i, "".join(reversed(Mywords[i])))
        else:
            List.insert(i, Mywords[i])
print (" ".join(List))


