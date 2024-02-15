words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
newWord = [i for i in words if 'a' in i and len(i) > 5]
print(newWord)

numbers = [30, 55, 20, 72, 40, 90, 10, 65]
newNumbers = [i for i in numbers if i > 50]
print(newNumbers)

# 최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서 있는 사람들의 이름이 담긴 리스트.
# 맨 앞에 타는 사람의 이름이 출력 되도록. >> 'nami','vex'가 출력되도록.
names = ['nami', 'ahri', 'jayce', 'garen', 'ivern', 'vex', 'jinx']
firstName = [j for i, j in enumerate(names) if i % 5 == 0]  # enumerate를 쓰면 앞에 요소 두 개를 뱉어냄
print(firstName)
