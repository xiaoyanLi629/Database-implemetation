from itertools import combinations
from collections import defaultdict


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
  
class Graph:
  def __init__(self):
    self.graph = defaultdict(list)
    
  def addEdge(self, u, v):
    self.graph[u].append(v)


def dfs(visited, graph, node):
  for v in graph.graph[node]:
    print(node, v, visited)
    r = v in visited
    print(r)
    if v in visited:
      return False
    visited.add(v)
    return dfs(visited, graph, v)
  return True


    
def is_conflict_serializable(schedule):
  prec = determine_precedence(schedule)
  
  list_ = set()
  for act_a, act_b in prec:
    list_.add(act_a)
    list_.add(act_b)
    
  list_ = list(list_)
  
  print(list_)
  
  g = Graph()
  for act_a, act_b in prec:
    g.addEdge(act_a, act_b)

  
  tested = set()
  
  for node in list_:
    if node not in tested:
      visited = set()
      visited.add(node)
      res = dfs(visited, g, node)
      print(node, res)
      if res is False:
        return False
      else:
        for ele in visited:
          tested.add(ele)
  print(prec)
  print(g.graph)
  return True
  