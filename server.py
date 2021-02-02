#!/usr/bin/env python3

import asyncio
import websockets

async def server(websocket, path):
    async for message in websocket:
        print("Message received")
        await websocket.send(f"Got your message: {message}")

start_server = websockets.serve(server, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
