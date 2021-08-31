class FunctionalDependency:
    def __init__(self, left_attributes_set, right_attributes_set):
        self.left_attributes_set = left_attributes_set
        self.right_attributes_set = right_attributes_set

    def __str__(self):
        return f"FunctionalDependency({self.left_attributes_set}, {self.right_attributes_set})"
    __repr__ = __str__


# left_side_set = {"age", "allergies"}
# right_side_set = {"name", "age"}
# functional_dependency = FunctionalDependency(left_side_set, right_side_set)


def check_funtional_dependency(list_of_dict_rows, functional_dependency):
    left_list = list(functional_dependency.left_attributes_set)
    right_list = list(functional_dependency.right_attributes_set)
    
    dict_ = {}
    for ele in list_of_dict_rows:
        key_temp = []
        for att in left_list:
            key_temp.append(ele[att])
        val_temp = []
        for att in right_list:
            val_temp.append(ele[att])
        
        key_temp = tuple(key_temp)
        val_temp = tuple(val_temp)
        
        if key_temp not in dict_:
            dict_[key_temp] = val_temp
        elif dict_[key_temp] == val_temp:
            pass
        else:
            return False
    return True