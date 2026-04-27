#create list 
fruits = ["apple", "banana", "orange", "mango", "grapes", "pineapple", "strawberry", "watermelon", "papaya", "kiwi"]
print(fruits)
#add new fruit at the end of list 
fruits.append('cherry')
fruits.append('apple') #add another item apple 
fruits.append('banana') #add another item banana
print("now fruit list has",fruits)
#add item at the beginning 
fruits.insert(0,'coconut')
fruits.insert(1,'watermelon')
print("after insert items at beginning, list has",fruits)
vegetables = ["potato", "tomato", "onion", "carrot", "cabbage"]
#add one list into another list 
fruits.extend(vegetables)
print("after extend list has",fruits)
#remove item onion
fruits.remove('onion')

#remove item at given position
fruits.pop(1)
print("after removal of items, list has",fruits)

#count how many apple fruit list has
print("count of apples ",fruits.count('apple'))
print("count of garlic ",fruits.count('garlic'))

#remove all items from vegetables 
vegetables.clear()
print("after removing all items from vegetables ",vegetables)

#now let us copy list into another list 
fruits2 = fruits.copy()
fruits.sort()
fruits2.sort()
fruits2.reverse()
print("Fruit ",fruits)
print("Fruit 2 ",fruits2)

