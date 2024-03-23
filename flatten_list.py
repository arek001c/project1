def flatten_list(data):
    result = []
    for element in data:
        if isinstance(element, (list,float,str)):
            result.append(element)
        else:
            flatten_list(element)
    result.sort()
    return result

print(flatten_list([1,[2,3],[5,[2,[8,9]]]]))
