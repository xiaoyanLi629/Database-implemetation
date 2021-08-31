class Action:
  """
  This is the Action class. It is already in the test cases, so please don't
  put it in your solution.
  """
  def __init__(self, object_, transaction, type_):
    self.object_ = object_
    self.transaction = transaction
    assert type_ in ("READ", "WRITE", "LOCK", "UNLOCK")
    self.type_ = type_
  def __str__(self):
    return f"Action({self.object_}, {self.transaction}, {self.type_})"

from collections import defaultdict

class LegalityOfScheduleViolation(Exception): pass
class TwoPhasedLockingViolation(Exception): pass
class ConsistencyOfTransactionViolation(Exception): pass

# Do not modify code above this line

def validate_locking_schedule(actions):
  
  # class LegalityOfScheduleViolation(Exception)
  act_dict = defaultdict(list)
  
  for action in actions:
    if action.object_ not in act_dict:
      if action.type_ == 'LOCK':
        act_dict[action.object_].append(action.transaction)
        act_dict[action.object_].append(action.type_)
    elif action.type_ == 'UNLOCK' and action.object_ in act_dict and action.transaction == act_dict[action.object_][0]:
      act_dict.pop(action.object_)
    elif action.object_ in act_dict and action.type_ == 'LOCK' and action.transaction != act_dict[action.object_][0]:
      raise LegalityOfScheduleViolation()

  # class TwoPhasedLockingViolation(Exception)
  tran_dict = defaultdict(list)
  
  for action in actions:
    if action.type_ == 'LOCK' and 'UNLOCK' in tran_dict[action.transaction]:
      raise TwoPhasedLockingViolation()
    else:
      tran_dict[action.transaction].append(action.type_)

  # ConsistencyOfTransactionViolation(Exception)
  con_dict = defaultdict(list)
  
  for action in actions:
    if action.type_ == 'LOCK' and action.object_ not in con_dict:
      con_dict[action.object_].append(action.transaction)
      con_dict[action.object_].append(action.type_)
    if action.type_ == 'READ' and action.object_ not in con_dict:
      raise ConsistencyOfTransactionViolation()
    if action.type_ == 'WRITE' and action.object_ not in con_dict:
      raise ConsistencyOfTransactionViolation()
    if action.type_ == 'READ' and action.object_ in con_dict and action.transaction != con_dict[action.object_][0]:
      raise ConsistencyOfTransactionViolation()
    if action.type_ == 'WRITE' and action.object_ in con_dict and action.transaction != con_dict[action.object_][0]:
      raise ConsistencyOfTransactionViolation()
    if action.type_ == 'UNLOCK':
      if action.object_ in con_dict and action.transaction == con_dict[action.object_][0]:
        con_dict.pop(action.object_)
  if len(con_dict) > 0:
    raise ConsistencyOfTransactionViolation()