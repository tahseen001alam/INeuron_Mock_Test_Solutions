num_list=list(map(int,input().split()))
empty_list=[]
zero_count=0
for i in range(len(num_list)):
    if num_list[i]!=0:
        empty_list.append(num_list[i])
    else:
        zero_count+=1
for i in range(zero_count):
    empty_list.append(0)
print(empty_list)