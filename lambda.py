# 1. Manager son price

manger_son_price = lambda price ,is_maneger_son : price -price/100*20 if is_maneger_son else price +price/100*17
print(manger_son_price(150,True))

#2
final_price= lambda price,discount :price-discount if 0<discount<100 else False
print(final_price(100,110))

#3
full_name = lambda first_name ,last_name :first_name+ " - "+ last_name
print(full_name('dave','kalaora'))

#4 
grade_status = lambda grade: 'pass' if grade>=55 else "fail"
print(grade_status(40))

#5
lorger = lambda n1,n2 : n1 if n1>=n2 else n2 
print(lorger(8,5))

#6
discount_from_10 =lambda num : 10-num if num<10 else num -10
print(discount_from_10(15))

#7

item_total = lambda item :item['price'] * item['amount']
print(item_total({"name": "Pen","price": 5, "amount": 10}))

#8
shiping_cost = lambda weigth,express :50 if weigth>5 and express>5 else 30 if express else 25 if weigth else 10
print(shiping_cost(3,True))
print(shiping_cost(8,True))
print(shiping_cost(8,False))
print(shiping_cost(2,False))
#9
access_message= lambda age,has_ticket,is_vip:"vip entrance" if is_vip else "regular enterance" if 18>= age and has_ticket else "buy ticket"if age<=18 else "too young"

print(access_message(25, True, False))
print(access_message(25, False, False))
print(access_message(15, True, False))
print(access_message(15, False, True))
#10
ticket_price = lambda age, is_student: 20 if age < 12 else 30 if is_student else 50

def ticket_price(age,is_student):
    if age <12:
        return 20
    elif is_student:
        return 30
    else:
        50
print(ticket_price(10, False))
print(ticket_price(20, True))
print(ticket_price(20, False))       