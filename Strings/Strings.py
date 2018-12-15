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