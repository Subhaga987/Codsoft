ch=input("enter any character")
low_count=0
up_count=0
num_count=0
if(ch>='0' and ch<='9'):
    num_count=num_count+1
elif(ch>='a' and ch<='z'):
    low_count=low_count+1
elif(ch>='A' and ch<='Z'):
    up_count=up_count+1
while(ch!='*'):
    ch=input("enter a character")
    if(ch>='0' and ch<='9'):
        num_count=num_count+1
    elif(ch>='a' and ch<='z'):
        low_count=low_count+1
    elif(ch>='A' and ch<='Z'):
        up_count=up_count+1
print("the number of lower cases are",low_count)
print("the number of upper cases are",up_count)
print("the number of number counts are",num_count)
   
