import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('tpss_bcycl_od_statnhm_20240323.csv')
# #프로그램getta에러 나왔을 때 부호체계가 달라서encoing='cp949' 이건 외워야함
#
# df['시작_동'] = [df['시작_대여소명'][i].split("동_")[0] for i in range(len(df['시작_대여소명']))]
# df.to_csv('new.csv', encoding='cp949',index=False)

df = pd.read_csv('new.csv', encoding='cp949')

new_dong = list(df['시작_동'])
dong = {}

for i in new_dong:
    if i in dong:
        dong[i] += 1
    else:
        dong[i] = 1


labels = dong.keys()
sizes = dong.values()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()