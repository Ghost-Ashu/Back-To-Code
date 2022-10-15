import random

print("This is simple username creator program")

names = input("Your idea-name: ").split(" ")
random_number = int(input("Put your lucky number (1-9): "))

if not(len(names) > 1):
    print("This program needs at least two words of idea-name")
    exit()


first_letter = names[0][:random_number]
surnmae_letter = names[-1][:random_number]

number = f"{random.randrange(1,999)}"
combine = [first_letter, surnmae_letter, number]
random.shuffle(combine)
username = "".join(combine)
print(username)