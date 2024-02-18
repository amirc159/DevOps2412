
with open("names.txt", "a") as my_file:
    my_file.write("eli\n")
    my_file.write("david\n")
    my_file.write("aviv\n")


with open("names.txt", "r") as my_file:
    for name in my_file.readlines():
        print(f"hello {name.strip()}")