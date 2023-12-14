inp_string = input("Ente the String:")
length = len(inp_string)
flag = 0
for i in range(length):
    print(inp_string[i],inp_string[i+1],inp_string[i+2])
    if((inp_string[i]==1) and (inp_string[i+1]==0) and (inp_string[i+2]==1)):
        flag = 1
if flag==1:
    print("101 exists")
else:
    print("It dosent")
