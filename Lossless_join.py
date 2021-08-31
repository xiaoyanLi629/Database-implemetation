# Write a function called, "is_lossless_join" that takes the following 4 arguments:

# relation_set: a set of attributes
# fds: a list of functional dependencies (like in the previous homework)
# sub_relation_1: a subrelation
# sub_relation_2: another subrelation
# The function should return true if the decomposition is a valid lossless decomposition, return false otherwise.

# Example (from the Lossless Joins video of Week 10):


# R = (A, B, C, D, E);

# FDs = {A→BC, CD→E, B→D, E→A}

# Decomposed into R1 = (A, B, C) and R2 = (A, D, E)

# becomes:

relation_set = {"A", "B", "C", "D", "E"}
fds = [
    FunctionalDependency({"A"}, {"B", "C"}),
    FunctionalDependency({"C", "D"}, {"E"}),
    FunctionalDependency({"B"}, {"D"}),
    FunctionalDependency({"E"}, {"A"}),
]
subrelation_1 = {"A", "B", "C"}
subrelation_2 = {"A", "D", "E"}

assert is_lossless_join(relation_set, fds, subrelation_1, subrelation_2)


# Another example
subrelation_1 = {"A", "B", "C"}
subrelation_2 = {"C", "D", "E"}

assert not is_lossless_join(relation_set, fds, subrelation_1, subrelation_2)

class FunctionalDependency:
    def __init__(self, left_attributes_set, right_attributes_set):
        self.left_attributes_set = left_attributes_set
        self.right_attributes_set = right_attributes_set

    def __str__(self):
        return f"FunctionalDependency({self.left_attributes_set}, {self.right_attributes_set})"
    __repr__ = __str__

def is_lossless_join(relation_set, fds, sub_relation_1, sub_relation_2):
    
    fds_temp = [ele for ele in fds]
    
    temp_relation = {ele for ele in sub_relation_1}
    temp_relation.update(sub_relation_2)
    
    cond_1 = True
    if temp_relation == relation_set:
        cond_1 = True
    else:
        cond_1 = False

    cond_2 = False
    
    inter_relation = sub_relation_1.intersection(sub_relation_2)
    
    index = 1
    while index > 0:
        index = 0
        fd_remove = []
        for fd in fds_temp:
            if fd.left_attributes_set.issubset(inter_relation):
                inter_relation.update(fd.right_attributes_set)
                fd_remove.append(fd)
                index = 1
        for fd in fd_remove:
            fds_temp.remove(fd)
            
    if sub_relation_1.issubset(inter_relation) or sub_relation_2.issubset(inter_relation):
        cond_2 = True
        
    if cond_1 == True and cond_2 == True:
        return True
    else:
        return False