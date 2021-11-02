import websocket, json

base_endpoint = 'wss://stream.binance.com:9443'

symbol = 'xrp'
interval = '1m'

endpoint = base_endpoint + "/ws/{}usdt@kline_{}"


def on_message(ws, message):
	"""

	:param ws: This is the websocket instance that is passed
	:param message: The message that has been received from the websocket
	:return: Currently, it does not have a return statement but in future will return the high price
	and low price for a crypto during an interval

	This function fetches (in the form of a candlestick chart)
	and then dispatches the important metrics for a selected crypto during a selected interval

	"""
	json_message = json.loads(message)
	candle = json_message["k"]
	print(candle)
	print("The crypto currency is : ", candle['s'], ", for the interval of ", candle["i"])
	return candle


ws = websocket.WebSocketApp(endpoint, on_message=on_message)
ws.run_forever()
