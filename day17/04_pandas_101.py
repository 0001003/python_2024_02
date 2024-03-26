# import pandas as pd
#
# # DateFrame과 Series
#
# pdSeries = pd.Series(['🍕🍕'for i in range(100)])
# print(pdSeries)
import pandas as pd

data = {
    '학원 지점': ['신촌점', '부평점', '강남점'],
    '시급': [25000, 26000, 30000],
    '강의 수': [1, 3, 1]
}

df = pd.DataFrame(data)
print(df)
df['sth'] = df['시급'] * df['강의 수'] # 새로운 것 추가
print(df)


# column(열)로 데이터 추출하기
print(df['학원 지점']) #무언가의 값을 알고 싶으면 key값을 넣으면 series처럼 나옴.
# print(df['학원 지점','시급']) # 안 나옴
print(df[['학원 지점','시급']]) # 두 개 이상 원하면 []를 하나 더 써 줘야 함

# row(행)으로 데이터 추출하기
print(df.loc[0])
print(df.loc[2])
print(df.loc[0], df.loc[1]) # 두 개 원할 때

# dataframe 속성
print(df.shape)         # 행과 열의 수
print(df.dtypes)        # 각 열의 데이터 타입 object는 대부분 문자임
print(df.columns)       # 열의 이름
print(df.index)         # 인덱스
print(df.values)        # 값을 보여주기 df.values[0][1] 이런 식으로 리스트처럼도 사용 가능함

# 메소드
print(df.describe())      # 숫자로 되어 있는 애들을 통계요약해주는 느낌
print(df.sort_values(by='시급')) # 시급 기준으로 오름차순으로 해 달라 / 가나다, 알파벳도 가능함
