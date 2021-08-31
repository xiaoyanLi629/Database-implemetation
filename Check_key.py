class FunctionalDependency:
    def __init__(self, left_attributes_set, right_attributes_set):
        self.left_attributes_set = left_attributes_set
        self.right_attributes_set = right_attributes_set

    def __str__(self):
        return f"FunctionalDependency({self.left_attributes_set}, {self.right_attributes_set})"
    __repr__ = __str__

def is_superkey(list_of_fds, all_attributes, cand):
    
    new_list_of_fds = [ele for ele in list_of_fds]
    
    temp_set = set(cand)
    
    index = 1
    
    while index != 0:
        index = 0 
        fds_remove = []
        for fd in new_list_of_fds:
            fd.right_attributes_set.update(fd.left_attributes_set)
            if all(ele in temp_set for ele in fd.left_attributes_set):
                temp_set.update(fd.right_attributes_set)
                fds_remove.append(fd)
                index = index + 1
        for fd in fds_remove:
            new_list_of_fds.remove(fd)
    
    if temp_set == all_attributes:
        return True
    else:
        return False
    
    
def is_key(all_attributes, list_of_fds, attribute_set):
    
    super_key = is_superkey(list_of_fds, all_attributes, attribute_set)
    
    cand_list = list(attribute_set)
    print('cand_list:', cand_list)
    
    key = False
    if len(cand_list) > 1:
        for ele in cand_list:
            print('cand_list:', cand_list, ele)
            attributes_list = list(attribute_set)
            attributes_list.remove(ele)
            cand = attributes_list
            print('cand:', cand)
            key = is_superkey(list_of_fds, all_attributes, cand)
            if key == True:
                break
    
    if super_key == False:
        False
    else:
        if key == True:
            return False
        else:
            return True