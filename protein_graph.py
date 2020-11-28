#count enzymes and plot graph
import numpy as np
import matplotlib.pyplot as plt
x=open("out2.txt","r")
count=0
y=input("enter a list of 4 proteins saperated by comma: ")
list=y.split(",")
for a in x:
  if list[0] in a:
    count+=1    
list1=count
z=open("out2.txt","r")
counti=0
for e in z:
  if list[1] in e:
    counti+=1        
list2=counti
q=open("out2.txt","r")
countq=0
for b in q:
  if list[2] in b:
    countq+=1      
list3=countq
n=open("out2.txt","r")   
counts=0
for d in n:
  if list[3] in d:
    counts+=1
list4=counts  
Proteins=[list[0],list[1],list[2],list[3]]
Abundance=[list1,list2,list3,list4]
plt.bar(Proteins, Abundance, color =['green','red','maroon','cyan'])
plt.title("Abndance of Proteins from Similarity search")
plt.xlabel("Proteins")
plt.ylabel("No. of Proteins")
plt.show()


























