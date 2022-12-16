x, y = 20, 30
print(f"x = {x}, y = {y}")
print("Swapping x and y")
x, y = y, x
print(f"x = {x}, y = {y}")
x, y = 20, 30
print(f"x = {x}, y = {y}, without swap")
x^=y
print(f"x = {x}, y = {y}, x^=y")
y^=x
print(f"x = {x}, y = {y}, y^=x")
x^=y
print(f"x = {x}, y = {y}, x^=y")
