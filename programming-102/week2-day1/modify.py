# names = ["Anthony", "Foi", "Marizel"]
# cousins = ["Erin", "Eric"]
# names.extend(cousins)
# print(names)

# names = ["Anthony", "Marizel", "Foi", "Erin", "Eric"]
# names[2] = "Foo"
# names[4] = "Bar"
# print(names)

names = ["Anthony", "Marizel", "Foi", "Erin", "Eric"]
index = 0

while index < len(names):
    print(names[0])
    del names[0]