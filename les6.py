#Урок 6ю Цикли for/while
#Цикл for використовується для ітерації по послідовності (наприклад, списку, кортежу, словника, набору або рядка).
# for i in range(5, 16, 3):
#     print("el:", i)

# print ("\n")

# word = "some text"
# for i in word:
#     print(i)

# word = "some text"
# for i in word:
#     if i == "m":
#         print("m present")

#Цикл while використовується для повторення блоку коду, поки умова є істинною.
# i = 0
# while i <= 10:
#     print(i)
#     i += 1  

# i = 100
# while i >= 10:
#     print(i)
#     i -= 10

#practice

# work = True
# while work:
#     user_input = input("enter word STOP: ")
#     if user_input == "STOP":
#         work = False
# print("while loop is done")

#cycle operators

# for i in range(1, 11):
#    if i == 7:
#         break
# print("el:", i)

#ELSE IN CYCLE

for i in "hello world":
    if i == "v":
        print("done")
        break
else: 
    print("not found")