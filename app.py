import random


print("Hello")

# ageNumber = input("Ålder:")
age = 15 #int(ageNumber)
name = "Lois"
height = 1.55
is_student = False

if age >= 18: 
    print(f"{name} är vuxen")
    print("______")
elif age > 12:
    print(f"{name} är tonåring")
else:
    print(f"{name} är ett barn")    
    

fruits = ["äpple", "banan", "päron"]
fruits.append("apelsin")
print(fruits)

for fruit in fruits:
    print(f"{fruit} är gott")


for i in range(5):
    print(f"nummer {i}")
    


def greet(person):
    return f"Hej, {person}"


message = greet("David")
print(message)

def calculate_rect_area(width, height, unit="m2"):
    area = width * height
    return f"Arean är {area} {unit}"


print(calculate_rect_area(10 , 5))
print(calculate_rect_area(10 , 5, "cm2"))


letters = ["a", "b", "c", "d", "e"]

print(letters[0])
print(letters[-1])
print(letters[1:4])


word = "python"
print(word[:2])

random_number = random.randint(1,10)

print(random_number)




