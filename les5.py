#Урок 5

'''if 5 == 5:
    print("yes")
    # знак рівності == використовується для порівняння двох значень. Якщо вони рівні, то виконується блок коду всередині if.

num = int(input("enter num: "))
if num == 55:
    print("yes")
print("no")'''
#Другий принт не відноситься до умови if, тому він виконається завжди, незалежно від того, чи виконується умова if чи ні.

'''num = int(input("enter num: "))
# ==, !=, >, <, >=, <= - це оператори порівняння, які використовуються для порівняння двох значень. Вони повертають булеве значення (True або False) в залежності від того, чи виконується умова.
if num != 55:
    print("yes")
print("no")
# != means "not equal to"'''

'''num = int(input("enter num: "))
if num >= 55:
    print("yes")
    if num == 100:
        print("HARYUR")
print("no")'''

'''isHappy = True
if isHappy == True:
    print("I am happy")
   
isHappy = True
if not isHappy == False:
    print("I am happy") '''

'''num = int(input("enter num: "))
if num >= 55:
    print("yes")
    if num == 100:
        print("HARYUR")
elif num == 40:
    print("elif")
    #elif is used to check multiple conditions. If the first condition is not met, it checks the next condition, and so on. If none of the conditions are met, it executes the code in the else block.
else:
    print("else")'''

'''data = "info"
if data == "info":
    correct = True
else:
    correct = False
print(correct)
'''
data = "info"
correct = True if data == "info" else False
print(correct)