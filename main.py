def getUser(id):
    if id > 0:
        return {
            "id" : 1,
            "name": "santosh",
            "role": "AI"
        }
    else:
        return "none"
def calculate_total(price, quantity):
    return price * quantity
result = getUser(2)
print(result)
result1 = getUser(0)
print(result1)
user = ["name","santosh"]
user1 = {
            "name" : "santosh",
            "age" : 10
        }
for name in user:
    print(name)
for key,value in user1.items():
    print(value)
cal = calculate_total(250, 4)
print(cal)
class users:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"name is {self.name}")
userCls = users("santosh")
userCls.greet()
