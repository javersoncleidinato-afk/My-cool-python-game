import random
import time

def wait(n):
    time.sleep(n)

score = 0
chances = 10

events = ["gold", "trap", "money", "stealer", "chest"]

caction = ["win", "lose"]

for i in range(10):
    event = random.choice(events)

    if event == "gold":
        print("You found gold! +10")
        score += 10

    elif event == "trap":
        print("You fell in a trap... -4")
        score -= 4

    elif event == "money":
        print("You found money! +5")
        score += 5

    elif event == "stealer":
        print("You got stolen... -6")
        score -= 6
        
    elif event == "chest":
    	print("you found one chest...")
    	wait(0.75)
    	chest_result = random.choice(caction)
    	print("you open it and find...")
    	wait(0.8)
    	if chest_result == "win":
    		print("some gold! +9")
    		score += 9
    	else:
    		print("one stealer, idk how it was on it... -6")
    		score -= 6

    wait(1.1)

    chances -= 1
    print("Chances left:", chances)
    wait(1.5)

print("\nGame ended!")
print("Final score:", score)