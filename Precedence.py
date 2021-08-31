from itertools import combinations

def determine_precedence(list_of_actions):
  res = set()
  comb = list(combinations(list_of_actions, 2))
  for act_a, act_b in comb:
    if act_a.is_write == True or act_b.is_write == True:
      if act_a.object_ == act_b.object_:
        if act_a.transaction != act_b.transaction:
          res.add((act_a.transaction, act_b.transaction))
  res = list(res)
  res.sort()
  return res