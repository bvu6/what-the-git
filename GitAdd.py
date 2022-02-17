#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!

from CardTypes import CardTypes
from Card import Card


class GitAdd(Card):
    def Add(self):
        return print("Doing git add")


def main():
    AddCard = GitAdd(CardTypes.Add)
    print(AddCard.getType())
    AddCard.Add()
    AddCard.verifyType()


if __name__ == "__main__":
    main()
