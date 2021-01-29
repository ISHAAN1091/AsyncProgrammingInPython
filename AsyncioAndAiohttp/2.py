# Here the tasks take place asynchronously which can be seen in the total time taken by them to complete their
# execution i.e. 3 seconds in total compared 5 seconds in the previous code
import asyncio
import time


async def waiter(n):
    await asyncio.sleep(n)
    print(f'Waited for {n} seconds')


async def main():
    task1 = asyncio.create_task(waiter(2))
    task2 = asyncio.create_task(waiter(3))
    print(time.strftime('%X'))
    await task1
    await task2
    print(time.strftime('%X'))

if __name__ == "__main__":
    asyncio.run(main())
