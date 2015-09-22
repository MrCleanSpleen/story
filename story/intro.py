"""Introduction

Would you like to start my text adventure, or
do you want to actually do something productive
with your time? It's your choice.
"""
forward="field"


def parse(s):
    line = s.action_line
    if "what" in line:
        print("You heard me")
    elif "help" in line:
        print("press f to move forward.")
