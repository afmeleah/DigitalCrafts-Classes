i_user = "whoisthebest"
i_pass = "anthonyisthebest"

new_user = input("Username:\n")
new_pass = input("Password:\n")

l = 1
while new_user == i_user and new_pass == i_pass:
    print("You're the best!")
    stop = input("No more looping\n")

while new_user != i_user and new_pass != i_pass and l < 6:
    new_user = input("Username:\n")
    new_pass = input("Password:\n")
    l += 1
    if l == 6:
        print("You have reached the limit. This program will now exit.")