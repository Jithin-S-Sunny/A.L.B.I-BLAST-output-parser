#to extract Query, full id and its sequences from BLAST output
import re
x=open("blast_input.txt","r")
y=open("raw.txt","wt")
z=["Query",">"]
for lines in x:
  if any (i in lines for i in z):
    print(lines.strip(), file=y)                                    
inputfile=open("raw.txt","r")
out=open("Id & Query.txt","wt")
for lines in inputfile:
  if not re.findall(r".*Query=",lines):
    print(lines.strip(), file=out)

#Strip background informations
delete_list=["Query"]
x=open("trail_out.txt","wt")
with open("Id & Query.txt") as f:
  data=''.join(i for i in f.read() if not i.isdigit())
  print(data, file=x)
y=open("ID & Sequence.txt","wt")
with open("trail_out.txt","r") as g:
  for line in g:
    for word in delete_list:
      line=line.replace(word, "")
      k=line.replace(" ","")
      print(k.strip(),file=y) 

#convert to FASTA      
data=open("ID & Sequence.txt").readlines()
y=open("final.txt","wt")
for n,line in enumerate(data):
    if line.startswith(">"):
       data[n] = "\n"+line.rstrip()
    else:
       data[n]=line.rstrip()
print (' '.join(data), file=y)
data=open("final.txt").readlines()
x=open("Fasta.txt","wt")
desired=data[1::5]
for i in desired:
  print(i, file=x)














