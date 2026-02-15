import time
import asyncio
async def func1():
    await asyncio.sleep(1)
    print("nc1")
async def func2():
    await asyncio.sleep(1)
    print("nc2")
async def func3():
    await asyncio.sleep(4)
    print("nc3")
async def  main():
    task=asyncio.create_task(func1())
    await func2()
    await func3()
asyncio.run(main())
