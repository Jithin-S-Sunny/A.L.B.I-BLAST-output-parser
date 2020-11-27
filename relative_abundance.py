#count by enzyme name & abundance"
import matplotlib.pyplot as plt
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
labels=y,'total'
sizes=[count,total]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  

plt.show()
    
            
        