import websockets
import asyncio
import time


async def listen():
	base_url = "ws://127.0.0.1:8081"

	async with websockets.connect(base_url) as ws:
		while True:
			symbol = "btc"
			await ws.send(symbol)
			msg = await ws.recv()
			print(msg)


asyncio.get_event_loop().run_until_complete(listen())
