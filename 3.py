a = 50
b = 10
my_name = "amir"
if a < 10:
    print("you are amir cohen")
    print("hello")
    print("world")
elif my_name == "amir":
    print("found your name")
elif b > 5:
    print("b is good")
else:
    print("blabla")

print(a == 50)

my_list = []
if len(my_list) > 0:
    print("you have items")
else:
    print("no items in the list")

my_other_list = ["or", "tohar", "adam"]
my_other_name = "moshe"
if my_other_name in my_other_list:
    print("i found you")
else:
    print("not in the list")

tt = [1, 2, 3]
rr = [1, 2, 4]
print(type(tt) is list)