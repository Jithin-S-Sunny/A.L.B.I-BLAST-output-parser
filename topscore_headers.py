#BLAST to extract all top score headers
import re 
x=open("blast_input.txt","r")
out1=open("out1.txt","wt")
z=">"
for lines in x:
  if z in lines:
    print(lines, file=out1)    
x=open("out1.txt","r")
out2=open("out2.txt","wt")
lines=x.readlines()
desired=lines[::5]
for i in desired:
  print(i, file=out2)
