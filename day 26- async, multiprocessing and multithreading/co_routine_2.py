import asyncio
async def fetch_data(delay,id):
    print("fetching data....",id)
    await asyncio.sleep(delay)
    print("data fetched",id)
    return {"data":"some data","id":id}
async def main():
    print("starting of the main coroutine")
    task1=fetch_data(3,1)
    task2=fetch_data(3,2)


    result1=await task1
    print(f"recived result {result1}")

    result2=await task2
    print(f"recived result {result2}")


    print("end of main coroutine")
asyncio.run(main())