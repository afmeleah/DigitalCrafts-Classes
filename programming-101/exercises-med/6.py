num = 1
num2 = 1
product = num * num2
print(f"{num} X {num2} = {product}")

while num <= 10:
    while num2 < 10:
        num2 += 1
        product = num * num2
        print(f"{num} X {num2} = {product}")
    if num2 == 10:
        num2 = 1
    if num == 11:
        print("We're Done!")
    num += 1
    product = num * num2
    print(f"{num} X {num2} = {product}")



# while sec_num < 10:
#     sec_num += 1
#     answer = num * sec_num
#     print(f"{num} X {sec_num} = {answer}")
#     if sec_num == 10:
#         sec_num = 1
#         while num < 10:
#             num += 1
#             answer = num * sec_num
#             print(f"{num} X {sec_num} = {answer}")


