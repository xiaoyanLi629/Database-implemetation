# Note not all or your solution should be in the function definition 

def add_censor_function(conn):
  conn.create_function("censor", 1, censor)

def censor(text):
  text = text.replace('UMich', '*****')
  text = text.replace('Maize', '*****')
  text = text.replace('Blue', '****')
  text = text.replace('Wolverines', '**********')
  return text