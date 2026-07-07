'''
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
'''


'''



#filter exe 

#1 
numbers = [4, 7, 10, 13, 18, 21]
result = list(filter(lambda x : x%2==0 , numbers))
print(result)
#2
grades = [100, 55, 70, 40, 88, 59]
result = list(filter(lambda x : x >= 60 , grades))
print(result)
#3
words = ["dog", "elephant", "cat", "computer", "sun"]
result = list(filter(lambda x : len(x)<= 3  , words))
print(result)
#4
names = ["Adam", "Dana", "Amit", "Noa", "Alon"]
result = list(filter(lambda x :len(x) > 0 and x[0] == "A" , names))
print(result)
#5 
numbers = [-5, 3, 0, 12, -2, 8]
result = list(filter(lambda x : x >0 , numbers))
print(result)
#6
products = [{"name": "Book", "price": 40},{"name": "Bag", "price": 120},{"name": "Pen", "price": 5},{"name": "Shirt", "price": 60}]
result = list(filter(lambda x :x["price"]<50 , products))
print(result)
#7
users = [{"name": "Dana", "active": True},{"name": "Ron", "active": False},{"name": "Maya", "active": True},{"name": "Gil", "active": False}]
result = list(filter(lambda x: x["active"], users))
print(result)
#8
passwords = ["abc", "hello123", "Python2026", "pass", "GoodPass99"]
result = list(filter(lambda x:len(x)>=8,passwords))
print(result)
#9 
tasks = [
{"title": "Clean room", "done": True, "priority": 2},
{"title": "Study Python", "done": False, "priority": 1},
{"title": "Play game", "done": False, "priority": 5},
{"title": "Send email", "done": True, "priority": 1}]
result = list(filter(lambda x : not x["done"]and x["priority"]<=3 , tasks))
print(result)
#10 
students = [
{"name": "Noa", "grade": 90, "attendance": 95},
{"name": "Dan", "grade": 55, "attendance": 100},
{"name": "Rina", "grade": 80, "attendance": 70},
{"name": "Eli", "grade": 75, "attendance": 85}]
result = list(filter(lambda x:x["grade"] >=70 and x["attendance"]>=80 , students))

print(result)
'''

#reduce
#1 reduce retern one final val becouse its combines all elements to one result 

#2 
#firest will multiply 2*3 = 6 
# second will multiply by 6* 4= 24  

#3
# map chenges all elments , 
#reduce when you want one result 

#4
#x= its runing a total 
#y = is the new value your adding


#5
# reduce when its a simply action to do like in a lambda func
#for loop when more comlex action

