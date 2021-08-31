def add_collation(conn):
  conn.create_collation('BILL_FIRST', BILL_FIRST)
  
def BILL_FIRST(left, right):
  if 'bill' in left and 'bill' in right:
    if left == right == min(left, right):
      return 0
    elif left == min(left, right):
      return -1
    else:
      return 1
  
  if 'bill' in left and 'bill' not in right:
    return -1
  if 'bill' not in left and 'bill' in right:
    return 1
    
  if 'bill' not in left and 'bill' not in right:
    if left == right == min(left, right):
      return 0
    elif left == min(left, right):
      return -1
    else:
      return 1