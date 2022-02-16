from CardTypes import CardTypes


class Card:
    def __init__(self, type):
        self.type = type

    def getType(self):
        return self.type

    def verifyType(self):
        for types in CardTypes:
            if types == self.type:
                print("Valid type")
                return True
        print("Not a valid type")
