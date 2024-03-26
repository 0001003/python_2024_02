# 현재 코인의 종류인 이더리움 코인의 3/1~3/26일까지
# 종가들을 날짜별로 리스트화하고 이를 엑셀화 시켜서 보여주는 코드 만들기


import datetime

# from BlockSDK.blocksdk import BlockSDK
# client = BlockSDK(api_token="YOU_TOKEN")
#
# result = client.ethereum.GetBlockChainInfo()
# print(result)

# datetime을 사용해서 3/1~3/26일까지 범위를 정하고서
# BlockSDK를 사용해서 이더리움의 주가를 확인하면 될 것 같음


import FinanceDataReader as fdr

eth = fdr.DataReader("ETH/KRW", "2024-03-01", "2024-03-25")
print(eth['Close'])



