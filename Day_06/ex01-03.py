from replit import db

print("---------------Ex01---------------")
# create 3 keys in database
# named them with "fruit", "dessert" & "food"
db["fruit"] = ["banana"]
db["dessert"] = ["cake"]
db["food"] = ["spaghetti"]

fruit = list(db["fruit"])
dessert = list(db["dessert"])
food = list(db["food"])

print(f"fruit = {fruit}")
print(f"dessert = {dessert}")
print(f"food = {food}")

# list all the variable keys in database
list_all = db.keys()
print(list_all)

# delete the key name of "food"
del db["food"]

# list the remaining keys
list_remaining = db.keys()
print(list_remaining)

print("---------------Ex02---------------")
# Add one element in fruit
if "fruit" in db.keys():
  db["fruit"].append("apple")

fruit_list = list(db["fruit"])
print(f"fruit = {fruit_list}")

# Add two elements in dessert
if "dessert" in db.keys():
  db["dessert"].append("ice cream")
  db["dessert"].append("souffle")

dessert_list = list(db["dessert"])
print(f"dessert = {dessert_list}")

# Delete one of the elements in list_2 ...
del (db["dessert"][-1])
# del(dessert_list[-1])

# List and show all the values available
dessert_list = list(db["dessert"])
print(f"dessert = {dessert_list}")

print("---------------Ex03---------------")
# Create a new key in database using if-else statement
if "message" not in db.keys():
  db["message"] = []
else:
  print("message key has been created")

# Add "Good Luck" as a value in the key
send = "Good Luck"
if "message" in db.keys():
  db["message"].append(send)
else:
  db["message"] = [send]

# List and show the value available
message_list = list(db["message"])
print(f"message = {message_list}")
