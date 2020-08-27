""" This code create or accurately write on three files different content and then take this content from each file and write it in new text file"""
"""idea to develop it, instead of using list and file names,
we can have  input number value let's say 4 and create four files and writing it different content and merge it in the new one"""

files = ["file1","file2","file3"]
i=0
while i< len(files):
    for file in files:
        opened = open(file,"w")
        ready= opened.write("Content"+str(i))
        i+=1
content=[]
for file in files:
     opened = open(file,"r")
     content.append(opened.readlines())
print(content)
handle = open("file4", "w")

for i in content:
    for j in i:
     print(j)
     writy = handle.write(j+"\n")
