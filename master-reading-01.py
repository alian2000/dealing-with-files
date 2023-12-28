x="Nour"
print(len(x))
# with open('first-names.txt') as malaf:
#     print(malaf.__dict__)
#     f_content = malaf.read(21)
#     print(f_content,end='')   #read and print the whole file
#     print(x,"end of the file",end="")
#     print("end of the file")
    
# with open('first-names.txt') as f:
#     f_content = f.readline()
#     print(len(f_content))
#     print(f_content,end='')   #read and print the first line
#     f_content = f.readline()
#     print(f_content,end='')   #read and print the 2nd line
#     f_content = f.readline(14)
#     print(f_content)   #read and print the 7 charachters

with open('first-names.txt','r') as file:
    for sater in file:
        print(sater,end='')  # read line by line
        print(len(sater))  # read line by line
        

