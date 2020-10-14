pet_name = input("What is your pet's name?\n")
num = len(pet_name)
if pet_name == "Shadow":
    print("El Gato Diablo!")
elif pet_name == "Daisy":
    print("Good Dog!")
elif num < 3:
    print("Name length is too short")
elif num > 3:
    print(f"AWWW sweet {pet_name}")
else:
    print("Be more creative with your pet names.")
