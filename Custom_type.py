import sqlite3

class Address:
  def __init__(self, street, city, state, zipcode):
    # All of these values are strings consisting of only
    # uppercase and lowercase letters, digits, and whitespace.
    self.street = street
    self.city = city
    self.state = state
    self.zipcode = zipcode
  def is_local(self):
    return self.zipcode == "48823"
  def __str__(self):
    return f"Address({self.street}, {self.city}, {self.state} {self.zipcode})"
  __repr__ = __str__

# Do not modify any code above this point!


def add_adapter_converter():
  sqlite3.register_adapter(Address, adapter)
  sqlite3.register_converter('ADDRESS', converter)


def adapter(address):  
  return "{};{};{};{}".format(address.street, address.city, address.state, address.zipcode)
  
def converter(bytestring):
  as_str = bytestring.decode('ascii')
  street, city, state, zipcode = [x for x in as_str.split(';')]
  return Address(street, city, state, zipcode)