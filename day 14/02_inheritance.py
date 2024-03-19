# 상속.

# class Minion:
#     def __init__(self, hp, attack):
#         self.hp = hp
#         self.attack = attack
#
#
# class MeleeMinion(Minion): # 괄호 안에 Minion 클래스를 넣어주면 상속 받은 것이다. MeleeMinion이 Minion에게 상속 받음.


class Vihicle:
    def ___init__(self, brand):
        self.brand = brand

class Car(Vihicle):
    def __init__(self, brand, horsePower):
        super().__init__(brand)  #super는 부모를 가리키는 함수임.
        self.horsePower = horsePower


class Airplane(Vihicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
