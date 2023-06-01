def Find_index(lst,item):
    try:
        index = lst.index(item)
        return index
    except ValueError:
        return -1
    
my_list=[20,10,30,40,50,60,70,80]
Finding_index=80
result=Find_index(my_list,Finding_index)
print(result) 