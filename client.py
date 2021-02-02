#!/usr/bin/env python3

import asyncio
import websockets

async def client():
    uri = "ws://localhost:5000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

asyncio.get_event_loop().run_until_complete(client())
