age = int(input("How old are you? "))
print("age,",age)
old = age > 60
young = age < 20
if old:
    print("old")
elif young:
    print("young")
else:
    print("mature")