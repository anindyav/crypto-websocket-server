import asyncio
import websockets
import json

port = 8081
interval = '1m'

base_endpoint = 'wss://stream.binance.com:9443'

crypto_index = {"btc": "Bitcoin",
				"eth": "Ethereum",
				"xrp": "Ripple",
				"bnb": "Binance"
				}

print("Listening on port", str(port))


async def echo(websocket, path):
	"""

	:param websocket:
	:param path:
	:return:

	This is an echo function which is called when the client connects to the local websocket server. When sent the crypto
	symbol, this function queries the binance websocket to fetch the trading details during the interval set in the
	variable

	"""
	print("Connection established")
	try:
		async for message in websocket:
			print("Received message from client, symbol = " + message)
			endpoint = base_endpoint + "/ws/{}usdt@kline_{}".format(message, interval)
			async with websockets.connect(endpoint) as ws:
				for i in range(1):
					data = await ws.recv()
				json_message = json.loads(data)
				candle = json_message["k"]
				return_message = {
					"name": crypto_index[message],
					"symbol": message,
					"Trade interval": interval,
					"Open price": candle['o'],
					"Close price": candle['c']
				}
			await websocket.send(json.dumps(return_message))
	except Exception as e:
		print(repr(e))


start_server = websockets.serve(echo, "localhost", port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
