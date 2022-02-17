#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!

from Level import Level

def main():
    Level1 = Level(1)
    list = Level1.createCards()
    for i in list:
        print(i.getType())

if __name__ == "__main__":
    main()