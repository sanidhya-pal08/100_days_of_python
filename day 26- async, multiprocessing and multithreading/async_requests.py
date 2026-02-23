import asyncio
import aiohttp
import time

async def fetch(session):
    async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
        return await response.json()

async def main():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session) for _ in range(5)]
        results = await asyncio.gather(*tasks)
        print(results)

    end = time.perf_counter()
    print("Time:", end - start)

asyncio.run(main())