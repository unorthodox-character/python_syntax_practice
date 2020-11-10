seq = {'a', 'b', 'c', 'd', 'e'}
lis1 = [2,3]
res_dict = dict.fromkeys(seq,lis1)
#print(res_dict)
lis1.append(4)
print(res_dict)
lis1 = [2,3]
res_dict2 = {key: list(lis1) for key in seq}
#print(res_dict2)
lis1.append(4)
#print(res_dict2)
