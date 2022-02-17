from CardTypes import CardTypes
from GitAdd import GitAdd
from GitCommit import GitCommit
from GitPush import GitPush


class Level:
    def __init__(self, lv):
        self.lv = lv

    def createCards(self):
        cardList = []
        if self.lv == 1:
            cardList.append(GitAdd(CardTypes.Add))
            cardList.append(GitCommit(CardTypes.Commit))
            cardList.append(GitPush(CardTypes.Push))
            print("Created add, commit, and push card objects")
            return cardList
