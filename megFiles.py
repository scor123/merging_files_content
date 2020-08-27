
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
