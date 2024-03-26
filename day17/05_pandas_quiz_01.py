# 카페에 데이터가 아래와 같이 있습니다.
import pandas as pd

data = {
    'Menu': ['Americano', 'Latte', 'Green Tea', 'Muffin', 'Sandwich'],
    'Sales': [100, 150, 90, 80, 60],
    'Price': [3000, 3500, 4000, 2500, 5000]
}

# 총 수입 열까지 만들어서 오름차순으로 모든 데이터를 보여주세요

df = pd.DataFrame(data)
df['total'] = df['Sales'] * df['Price']

print(df.sort_values(by='total'))

df.to_csv('megaCoffee.csv') # , index=False 하게 된다면 맨 왼쪽 index를 없애줌
