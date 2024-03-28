import pandas as pd

df = pd.read_csv('japan_visit.csv')
# grouped_by_city = df.groupby("city")
# print(grouped_by_city)
#
# # 도시별로 나이대 그룹핑
# ages_by_city = grouped_by_city['ages'].value_counts() #sort가 자동으로 됨.
# print(ages_by_city)

# 나이대 별로 그룹핑하고 방문 목적을 보여주는 코드
grouped_by_ages = df.groupby("ages")
purpose_by_ages = grouped_by_ages['purpose'].value_counts()
print(purpose_by_ages)

# groupby 함수