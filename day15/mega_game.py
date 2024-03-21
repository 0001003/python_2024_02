# 1단계 : 추상 기본 클래스 character 정의
# 모든 캐릭터는 이름(name)과 체력(health)을 속성으로 가집니다.
# attack()과 defend() 두 가지 추상 메소드를 포함합니다.
from day15.model.archer import Archer
from day15.model.mage import Mage
from day15.model.warrior import Warrior

# 2단계 : 구체적 캐릭터 클래스 구현
# 전사(Warrior)
# 고유 속성 : 분노(rage), 분노는 공격할 때마다 쌓이며, 특정 수준에 도달하면 강력한 스킬을 사용할 수 있습니다.
# 마법사(Mage)
# 고유 속성 : 마나(mana), 마나는 마법 공격이나 방어막을 생성할 때 사용됩니다.
# 고유 메소드 :cast_spell() - 마나를 사용하여 강력한 마법 공격을 합니다. 마나가 부족하면 사용할 수 없습니다.
# 궁수(Archer)
# 고유 속성 : 화살(arrows), 공격할 때마다 화살을 소모합니다.
# 고유 메소드 : replenish_arrows() - 화살통을 다시 채웁니다. 화살이 다 떨어지면 공격할 수 없습니다.


# from abc import ABC, abstractmethod
#
# class Character:
#     def __init__(self):
#
#         @abstractmethod
#         def unique_property(self):
#             pass
#
#         @abstractmethod
#         def unique_method(self):
#             pass
#
# class Warrior:
#     def __init__(self):
#         pass
#
#     def unique_property(self, rage):
#         self.rage = rage
#
#     def unique_method(self, berserk):
#         self.berserk = berserk
#
# class Mage:
#     def __init__(self):
#         pass
#
#     def unique_property(self, mana):
#         self.mana = mana
#
#     def unique_method(self, cast_spell):
#         self.cast_spell = cast_spell
#
# class Archer:
#     def __init__(self):
#         pass
#
#     def unique_property(self, arrows):
#         self.arrows = arrows
#
#     def unique_method(self, replenish_arrows):
#         self.replenish_arrows = replenish_arrows

# # 답
#
# from abc import ABC, abstractmethod
#
#
# class Character(ABC):
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     @abstractmethod
#     def attack(self):
#         pass
#
#     @abstractmethod
#     def defend(self):
#         pass
#
#
# class Warrior(Character):
#     def __init__(self, name, health):
#         super().__init__(name, health)
#         self.rage = 0
#
#     def attack(self):
#         print("검 휘두르기")
#         self.rage += 10
#
#     def defend(self):
#         print("방패로 막기")
#
#     def berserk(self):
#         if self.rage == 100:
#             print("분노 모드")
#             self.rage = 0
#         else:
#             print(f"분노 게이지가 {100-self.rage} 만큼 모자릅니다.")
#
#
# class Mage(Character):
#     def __init__(self, name, health):
#         super().__init__(name,health)
#         self.mana = 0
#
#     def attack(self):
#         print("주문 걸기")
#         self.mana += 10
#
#     def defend(self):
#         print("보호막으로 막기")
#
#     def cast_spell(self):
#         if self.mana == 0:
#             print("마나가 부족합니다.")
#         else:
#             print("마법 에너지 공격")
#             self.mana -= 10
#
#
#
# class Archer(Character):
#     def __init__(self, name, health):
#         super().__init__(name, health)
#         self.arrow = 50
#
#     def attack(self):
#         print("화살 쏘기")
#         self.arrow -= 10
#
#
#     def defend(self):
#         print("피하기")
#
#     def replenish_arrows(self):
#             print("화살통 채우기")
#             self.arrow =50


print("메가 게임")

character_number = input("캐릭터를 선택하세요 : (1번 전사, 2번 마법사, 3번 궁수) :")
name = input("이름을 넣어주세요 : ")
choice = {
    "1": Warrior(name, 200),
    "2": Mage(name, 100),
    "3": Archer(name, 150),
}

character = choice[character_number]

while True:
    selected = input("1. 공격하기 2. 방어하기 3. 특수 능력")
    if selected == '1':
        character.attack()
    elif selected == '2':
        character.defend()
    elif selected == '3':
        character.special()
    else:
        print("해당 번호는 없습니다.")







