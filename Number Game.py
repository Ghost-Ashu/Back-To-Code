import random
rand = random.randint(1,10)
#print(rand)
user = None
guess =0
while user!=rand:
    user = int(input("Enter the number:"))
    guess += 1
    if user==rand:
        print("U guess the correct number")
    else:
        if user>rand:
            print("U guess the incorrect number please enter the smaller number")
        else:
            print("U guess the incorrect number please enter the greater number")

print(f"U guessed the number in {guess} guesses")
with open("Scores.txt",'r')as f:
    score = int(f.read())

if (guess<score):
    print("COngratulations you broke the high score:")
    with open("Scores.txt",'w')as f:
        f.write(str(guess))
        f.close()