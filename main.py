import random
from pynput.mouse import Listener

print("Press left click to roll....")


def roll_dice():
    return random.randint(1, 6)


# making function to roll the dice
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if pressed and button == button.left:
        result = roll_dice()
        print("You rolled:", result)
        # Execute your command here


with Listener(on_click=on_click) as listener:
    listener.join()

if __name__ == "__main__":
    on_click()
