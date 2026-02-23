import asyncio
async def func1():
    print("you are inside func 1")
    await asyncio.sleep(2)
    print("func1 finished")
async def func2():
    print("you are inside func 2")
    await asyncio.sleep(2)
    print("func2 finished")
async def func3():
    print("you are inside func 3")
    await asyncio.sleep(2)
    print("func3 finished")
async def main():
    async with asyncio.TaskGroup() as tg:
       tg.create_task(func1)
       tg.create_task(func2)
       tg.create_task(func3)
asyncio.run(main())
            