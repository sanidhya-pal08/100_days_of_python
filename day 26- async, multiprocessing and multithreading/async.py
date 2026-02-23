import time 
import asyncio
async def func1():
    print("hi")
    await asyncio.sleep(1)
    print("func1ended")
async def func2():
    print("hi")
    await asyncio.sleep(1)
    print("func2ended")
async def func3():
    print("hi")
    await asyncio.sleep(1)
    print("func3ended")
async def main():
    await func1()
    task=asyncio.create_task(func2())
    await func3()

asyncio.run(main())