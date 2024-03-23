def flatten_list(data, result=[]):
    for element in data:
        if isinstance(element, (float,int, str)):
            result.append(element)
        else:
            flatten_list(element)
    result.sort()
    return result

print(flatten_list([1,[2,[5,6,[8,9]]]]))
