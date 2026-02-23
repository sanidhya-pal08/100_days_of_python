import asyncio
async  def set_future_result(future,value):
    await asyncio.sleep(2)
    future.set_result(value)
    print(f"set the future's result to {value}")
async def main():
    #create a future object
    loop=asyncio.get_running_loop()
    future=loop.create_future()
    
    #schedule setting the future's result
    asyncio.create_task(set_future_result(future,"future result is ready"))

    #wait for future's result
    result =await future
    print(f"recieved future result: {result}")
asyncio.run(main())