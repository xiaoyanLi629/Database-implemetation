def add_aggregate_function(conn):
  conn.create_aggregate("lines_censored", 1, lines_censored)

class lines_censored:
  def __init__(self):
    self.counter = 0
    
  def step(self, text):
    # UMich
    # Maize
    # Blue
    # Wolverines
    if 'UMich' in text or 'Maize' in text or 'Blue' in text or 'Wolverines' in text: 
      self.counter = self.counter + 1
    
  def finalize(self):
    return self.counter