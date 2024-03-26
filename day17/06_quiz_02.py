import faker
import pandas as pd
import random
import faker
#
kr = faker.Faker('ko_KR')
# for i in range(100):
#     print(kr.name())


# CU_data = {
# 'customer':[] #1000명
# 'purchase_item':[] // 생필품, 기호품, 스낵류, 음료류, 주류,
# 'purchase_price':[] // 1000~50000
# 'payment':[] //신용카드, 체크카드, 카카오페이, 네이버페이, 애플페이
# 'time':[] //오전 오후 저녁 밤 새벽

item = ['생필품', '기호품', '스낵류', '음료류', '주류']
payment = ['신용카드', '체크카드', '카카오페이', '네이버페이', '애플페이']
time =['오전', '오후', '저녁', '밤', '새벽']

CU_data = {
    'customer': [faker.Faker('ko_KR').name() for i in range(1001)],
    'purchase_item': [random.choice(item) for i in range(1001)],
    'purchase_price': [random.randint(1000, 50001) for i in range(1001)],
    'payment': [random.choice(payment) for i in range(1001)],
    'time': [random.choice(time) for i in range(1001)]
}

df = pd.DataFrame(CU_data)
df.sort_values(by="customer")
df.to_csv('CU_data.csv', index=False)
