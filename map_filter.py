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