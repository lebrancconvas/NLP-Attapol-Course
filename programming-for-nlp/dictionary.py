# Contained Key-Value pairs 

def my_dict():
  tel_dict = {"meow": "000-111-234", "bee": "111-234-555"}
  key = iteration_key(tel_dict)
  return(key)

# Get All Keys from Dictionary. 
def iteration_key(dict):
  return(dict.keys())

mydict = my_dict()

print(mydict)