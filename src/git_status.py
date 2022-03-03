class git_status:
    def __init__(self):
        self.after_push()

    def check_move(self, card_type):
        # if self.lastMove == card_type - 1:
        #     self.lastMove = card_type
        #     return True
        print("Last", self.lastMove, "type", card_type)
        if card_type == 0:
            self.lastMove = card_type
            return True

        elif card_type == 1 and self.lastMove == card_type - 1:
            self.lastMove = card_type
            self.commit = True
            return True

        elif card_type == 2 and self.commit:
            self.after_push()
            return True

        else:
            #print(card_type, self.lastMove)
            print("Invalid move")
            return False

    def after_push(self):
        self.add = False
        self.commit = False
        self.push = False
        self.lastMove = -1

