person = "Anthony"
today = "Tuesday"
emotion = "excited"

print(f"Hello {person},\nI hope that your {today} is going well.\nI'm personally really {emotion}.")

new_statement = "Hello %s,\nI hope that your %s is going well.\nI'm personally really %s." % (person, today, emotion)
print(new_statement)

print(f"Hello {person},\nI hope that your {today} is going well.\nI'm personally really {emotion}.")