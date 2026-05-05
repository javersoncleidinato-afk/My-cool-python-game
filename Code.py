import random
import time

def wait(n):
    time.sleep(n)

score = 0
chances = 10

events = ["gold", "trap", "money", "stealer"]

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

    wait(0.5)

    chances -= 1
    print("Chances left:", chances)
    wait(0.5)

print("\nGame ended!")
print("Final score:", score)
