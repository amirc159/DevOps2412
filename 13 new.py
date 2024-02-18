# Open the file in append mode
with open("names.txt", "a") as :
    # Ask the user to input three names
    for i in range(3):
        name = input(f"Enter name {i + 1}: ")
        my_file.write(name + "\n")

# Print the updated content of the file
with open("names.txt", "r") as my_file:
    for name in my_file.readlines():
        print(f"hello {name.strip()}")
