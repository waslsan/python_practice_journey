import cowsay
import random

name = input(str("what is your name?"))
characters = [cowsay.cheese, cowsay.cow, cowsay.kitty, cowsay.meow, cowsay.tux]
random_char = random.choice(characters)
message = random_char(f"welcome {name}")
print(message)

