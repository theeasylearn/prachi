a = 10 
b = 20
c = 20
d = 30 


#we must AND/OR operator between 2 relational expression in single line 
result = a < b and b < d
print(f"{result} = {a} < {b} and {b} < {d}")

result = a < b and b > d
print(f"{result} = {a} < {b} and {b} > {d}")

result = a > b and b < d
print(f"{result} = {a} > {b} and {b} < {d}")

result = a > b and b > d
print(f"{result} = {a} > {b} and {b} > {d}")


result = a < b or b == c
print(f"{result} = {a} < {b} or {b} == {c}")


result = a > b or b == c
print(f"{result} = {a} > {b} or {b} == {c}")


result = a < b or b != c
print(f"{result} = {a} < {b} or {b} != {c}")


result = a > b or b != c
print(f"{result} = {a} > {b} or {b} != {c}")