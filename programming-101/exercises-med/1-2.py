#bill = float(input("What is the total of your bill?\n"))
#service = input("How would you rate the service provided? good, fair or bad?\n")

#if service == "good":
#    tip = "%.2f" % (bill * .20)
#elif service == "fair":
#    tip = "%.2f" % (bill * .15)
#else:
#    tip = "%.2f" % (bill * .10)
#print(f"Tip amount: {tip}") 
#total = "%.2f" % (bill + float(tip))
#print(f"Total amount: {total}")

bill = float(input("What is the total of your bill?\n"))
service = input("How would you rate the service provided? good, fair or bad?\n")
split = float(input("Split how many ways?\n"))
if service == "good":
    tip = "%.2f" % (bill * .20)
elif service == "fair":
    tip = "%.2f" % (bill * .15)
else:
    tip = "%.2f" % (bill * .10)
print(f"Tip amount: {tip}") 
total = "%.2f" % (bill + float(tip))
print(f"Total amount: {total}")
per_person = "%.2f" % (float(total) / split)
print(f"Amount per person: {per_person}")
