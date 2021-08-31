from collections import defaultdict

class Action:
  """
  This is the Action class.
  """
  def __init__(self, object_, transaction, type_):
    self.object_ = object_
    self.transaction = transaction
    assert type_ in ("WRITE", "COMMIT", "ROLLBACK", "LOCK", "UNLOCK", "WAIT")
    self.type_ = type_
  def __str__(self):
    return f"Action('{self.object_}', '{self.transaction}', '{self.type_}')"
  __repr__ = __str__
  def __eq__(self, other):
    return ((self.object_ == other.object_) and 
      (self.transaction == other.transaction) and 
      (self.type_ == other.type_))

# Do not modify any code above this line

def wait_die_scheduler(actions):
  # to store the result
  res = []

  # transaction order as dictionary starting with 0
  tran_order = {}
  i = 0
  for action in actions:
    if action.transaction not in tran_order:
      tran_order[action.transaction] = i
      i = i + 1
    
  # remove_dict to store the actions have been conducted
  remove_dict = defaultdict(list)
  
  # tran_act to store actions of each transaction in order
  # could iterate transactions in order by the dictionary by alpgabetic order
  # for example: apple >> carrot >> pear
  tran_act = defaultdict(list)
 
  for action in actions:
    if action.transaction not in tran_act:
      tran_act[action.transaction] = []
  
  
  # store the locking status of the objects
  # object_dict[action.object_] = [True, action.transaction]
  object_dict = {}
  
  while len(tran_act) > 0:
    if len(actions) > 0:
      action_pop = actions.pop(0)
  	  # add one action from actions into tran_act
      tran_act[action_pop.transaction].append(action_pop)
  	  # iterate each transaction once
    for transac in sorted(tran_act):
      transac_act_list = tran_act[transac]
  	    # if there is actions haven't done of the corresponding transaction
      if len(transac_act_list) > 0:
  	    # the action to consider
        action = transac_act_list.pop(0)
  	    # if the action is WRITE
        if action.type_ == 'WRITE':
  	  	  # if the object is not locked
          if action.object_ not in object_dict:
            object_dict[action.object_] = [True, action.transaction]
            res.append(Action(action.object_, action.transaction, 'LOCK'))
            res.append(Action(action.object_, action.transaction, 'WRITE'))
  		    # add the action to remove_dict
            remove_dict[action.transaction].append(action)
  		  # if the object is locked
          else:
  		    # if the requesting transaction is older than locking transaction
            if tran_order[action.transaction] < tran_order[object_dict[action.object_][1]]:
              res.append(Action('NA', action.transaction, 'WAIT'))
  			  # put the action back to transaction actions list
              transac_act_list.insert(0, action)
  		    # if the requestion transaction is locking the object
            elif tran_order[action.transaction] == tran_order[object_dict[action.object_][1]]:
              res.append(Action(action.object_, action.transaction, 'WRITE'))
  		      # add the action to remove_dict
              remove_dict[action.transaction].append(action)
  		    # if the requesting transaction is younger thanlocking transaction
            else:
              res.append(Action('NA', action.transaction, 'ROLLBACK'))
  			  # unlock the actions locked by the rollback transaction
              objects_unlock = []
              for ele in object_dict:
                if object_dict[ele][1] == action.transaction:
                  objects_unlock.append(ele)
              objects_unlock.sort()
              for ele in objects_unlock:
                # add the unlock actions into res
                res.append(Action(ele, action.transaction, 'UNLOCK'))
                # remove the locking status in the object_dict
                object_dict.pop(ele)
  			  # put the actions in remove_dict back
  			  # all the actions of this transaction will be conducted in next iteration
              remove_dict[action.transaction].append(action)
              tran_act[transac] = remove_dict[action.transaction] + tran_act[transac]
              #print('Restore actions:', tran_act)
  			  # empty the action list of the 
              remove_dict[action.transaction] = []
        if action.type_ == 'COMMIT':
          res.append(Action('NA', action.transaction, 'COMMIT'))
		    # unlock the actions locked by the rollback transaction
          objects_unlock = []
          for ele in object_dict:
            if object_dict[ele][1] == action.transaction:
              objects_unlock.append(ele)
          objects_unlock.sort()
          for ele in objects_unlock:
            # add the unlock actions into res
            res.append(Action(ele, action.transaction, 'UNLOCK'))
            # remove the locking status in the object_dict
            object_dict.pop(ele)
          # remove the transaction has been committed
          tran_act.pop(action.transaction)
          # empty the action list of the 
          remove_dict[action.transaction] = []
            
  return res