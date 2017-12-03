import requests

# ############
# https://api.coindesk.com/v1/bpi/currentprice/USD.json
# ref: http://docs.python-requests.org/en/master/
# Chương trình lấy giá bitcoin/usd realtime bằng Python tại kênh Youtube: Tran Duc Loi
# ############

def getBTCUSD():
	api = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
	ret = requests.get(api)

	if ret.status_code == 200:
		ret = ret.json()
		# print ret
		btcprice = ret['bpi']['USD']['rate']
		# print btcprice
		return btcprice
	else:
		print ("Unable to call API this time.")
		return False

if __name__ == '__main__':
	print getBTCUSD()

