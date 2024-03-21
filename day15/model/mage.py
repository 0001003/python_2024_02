from day15.model.chracter_abc import Character


class Mage(Character):
    def __init__(self, name, health):
        super().__init__(name,health)
        self.mana = 0

    def attack(self):
        print("주문 걸기")
        self.mana += 10

    def defend(self):
        print("보호막으로 막기")

    def special(self):
        if self.mana == 0:
            print("마나가 부족합니다.")
        else:
            print("마법 에너지 공격")
            self.mana -= 10