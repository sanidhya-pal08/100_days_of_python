import asyncio

async def fetch_data(id,sleep_time):
    print(f"coroutine {id} is starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id":id,"data":f"sample data for coroutine {id}"}
async def main():
    # task1=asyncio.create_task(fetch_data(1,3))
    # task2=asyncio.create_task(fetch_data(2,3))
    # task3=asyncio.create_task(fetch_data(3,3))
    # result1=await task1
    # result2=await task2
    # result3=await task3
    # results=await asyncio.gather(fetch_data(1,3),fetch_data(2,3),fetch_data(2,3))  #returns a list of results
    tasks=[]
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([2,1,3],start=1):
            task=tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)
    results = [task.result() for task in tasks]
    for result in results:
        print(result)
asyncio.run(main())