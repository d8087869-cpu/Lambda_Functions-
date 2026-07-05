#1
numbers = [3, 7, 10, 15]
result = list(map(lambda x:x +10 ,numbers))
print(result)
#2
prices = [100, 50, 200, 80]
result = list(map(lambda x :x * 1.17, prices))
print(result)
#3
words = ["cat", "elephant", "dog", "python"]
result = list(map(len,words))
print(result)
#4
names = ["dan", "maya", "ron", "lea"]
result = list(map(str.upper, names))
print(result)
#5
users = ["Noa", "Adam", "Lior", "Tamar"]
result = list(map(lambda x:f"Hello {x}",users))
print(result)
#6
meters = [1.5, 2, 0.75, 3.2]
result = list(map(lambda x:x *100,meters))
print(result)
#7 
grades = [95, 40, 67, 88, 52]
result = list(map(lambda x :"pass" if x >60 else "fail", grades ))
print(result)
#8 
products = [{"name": "Bread", "price": 8},{"name": "Milk", "price": 6},{"name": "Eggs", "price": 15}]
result = list(map(lambda x : f"{x ["name"]} cost {x["price"]}" , products))
print(result)
#9
players = [{"name": "Dana", "score": 70},{"name": "Yoni", "score": 85},{"name": "Rami", "score": 40}]
result = list(map(lambda x :{'name': x['name'], "score":x["score"]+5},players))
print(result)
#10 
orders = [{"id": 1, "item": "Book", "amount": 3, "price": 40},{"id": 2, "item": "Pen", "amount": 10, "price": 5},{"id": 3, "item": "Bag", "amount": 1, "price": 120}]
result = list(map(lambda x : f"order {x['id']}:{x["item"]} total is {x["amount"]* x["price"]}" , orders))
print(result)


