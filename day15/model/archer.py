from day15.model.chracter_abc import Character


class Archer(Character):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.arrow = 50

    def attack(self):
        print("화살 쏘기")
        self.arrow -= 10

    def defend(self):
        print("피하기")

    def special(self):
            print("화살통 채우기")
            self.arrow = 50