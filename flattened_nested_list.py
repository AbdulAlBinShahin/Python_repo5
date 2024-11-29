def flatten_nested_list(nested_list):
    flatten_list=[]
    for i in nested_list:
        if isinstance(i,list):
            flatten_list.extend(flatten_nested_list(i))
        else:
            flatten_list.append(i)
    return flatten_list
 
flattened_list=[1,[2,3],4,[5,6],7,8,[9,10,11],12]
 
new_flatten=flatten_nested_list(flattened_list)
print(f"the list is {new_flatten}")
