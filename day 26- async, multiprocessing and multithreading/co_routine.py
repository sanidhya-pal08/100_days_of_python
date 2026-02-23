import asyncio
async def fetch_data(delay,id):
    print(f"fetching data.....{id}")
    await asyncio.sleep(delay)
    print("data fetching finished ")
    return {"data_recieved":"some data"}
async def main():
    print("we are inside the main coroutine function")
    task =fetch_data(4,1)
    result =await task
    print(result)
    print("data fetching finished")
asyncio.run(main())