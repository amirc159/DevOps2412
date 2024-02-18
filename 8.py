details = ["amir", "cohen", 41, True]
details_dict = {"fname": "amir",
                "lname": "cohen",
                "age": 41,
                "is_married": True}
my_class = [
    {"fname": "or", "lname": "shemesh"},
    {"fname": "amir", "lname": "cohen"},
]

for student in my_class:
    print(student["fname"])
print(details_dict.keys())
print(details_dict.values())
my_othe_dict = {
    0: "moshe",
    1: "haim",
    2: 56,
    3: False
}
