
#count by enzyme name & abundance"
x=open("out2.txt","r")
y=input("enter the protein name:")
count=0
total=0
p=">"
for lines in x:
    if y in lines:
        count=count+1
    if p in lines:
        total=total+1
print("the number of",y, "is: ",count)
print("the abundance of",y, "is:",round((count/total)*100),"%" )


    
            
        