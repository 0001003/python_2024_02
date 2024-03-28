# 미션 목표
# 가상 데이터 생성: 일본 관광객을 상정하고, 이에 데이터를 직접 생성합니다.
# 컬럼 설계하기
# - 다음 정보를 포함하는 컬럼을 설계합니다. (1000명)
# 이름
# 나이대 [10,20,30,40,50,60,70]
# 국적 [한국, 일본, 중국, 미국]
# 출발 일자 [03월 01일~ 03월 27일]
# 여행 목적 [비지니스, 관광, 친지 방문]
# 지출 총액 [100000~2000000]

import pandas as pd
import random
import datetime #datetime말고 다른 것도 있음 밑에 참고하기
import faker

ages = ['10', '20', '30', '40', '50', '60', '70']
start = pd.date_range("2024-03-01","2024-03-27") #<<배열 같으니까 [5]처럼 그걸 뽑도록 할 수 있음
nationality = ['한국', '일본', '중국', '미국']
cities = ['도쿄,','오사카','삿포로','후쿠오카','오키나와']
purpose = ['비지니스', '관광', '친지 방문']
expense = [range(100000, 2000000)]






fake = faker.Faker(['ko_KR','jp_JP', 'en_US', 'zh_CN'])

data = {
    'name': [fake.name() for i in range(1000)],
    'ages': [random.choice(ages) for i in range(1000)],
    'start': [pd.date_range("2024-03-01", "2024-03-27")[random.randint(0, 26)] for i in range(1000)],
    'city': [random.choice(cities) for i in range(1000)],
    'purpose': [random.choice(purpose) for i in range(1000)],
    'expense': [random.choice(expense) for i in range(1000)]
}

df = pd.DataFrame(data)
df.to_csv('japan_visit.csv', index = False)