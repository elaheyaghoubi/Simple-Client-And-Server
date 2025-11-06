import asyncio
import websockets
import json
from datetime import datetime
import uuid
import time


max_client = 3
semaphore = asyncio.Semaphore(max_client)

async def handle_sum(websocket):
    async with semaphore:
        try: 
          
            msg = await websocket.recv()   

            start_time = time.perf_counter() 
            request_id = uuid.uuid4().hex[:8]     
            request_ip = websocket.remote_address[0]   
            request_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

            print(f"{request_time} REQUEST id={request_id} ip={request_ip} method=GET body={msg}")

            data = json.loads(msg)
            result = round(sum(data), 3)

            await websocket.send(str(result))

            end_time = time.perf_counter()
            response_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

            print(f"{response_time} RESPONSE id={request_id} body={result} latency={(end_time - start_time) * 1000:.2f}ms")
            

        except websockets.ConnectionClosed:
            print("Client disconnected")


async def main():
    async with websockets.serve(handle_sum, "localhost", 8765):
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())

