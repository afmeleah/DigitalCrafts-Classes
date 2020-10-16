coin = 0
get_coin = "yes"
#how_many = f"You have {coin} coins."
#print(how_many)
while get_coin == "yes":
    print(f"You have {coin} coins.")
    get_coin == input("Do you want a coin?\n")
    if get_coin == "yes":
        coin += 1
print("Bye")














# coin = 0
# get_coin = "yes"
# while get_coin == "yes":
#     print(f"You have {coin} coins.")
#     get_coin = input("Do you want another coin?")
#     if get_coin == "yes":
#         coin += 1
# print("Bye")


    