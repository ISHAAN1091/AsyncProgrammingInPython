# Even though we are using asyncio here but still the task are not taking place asynchronously
# as we can see that to execute they took a total of 5 seconds while if they were taking place
# asynchronously they would have been completed in 3 seconds only. This is happening because
# even though we are asyncio here we are not using it to carry out tasks asynchronously
import asyncio
import time


async def waiter(n):
    await asyncio.sleep(n)
    print(f'Waited for {n} seconds')


async def main():
    print(time.strftime('%X'))
    await waiter(2)
    await waiter(3)
    print(time.strftime('%X'))

if __name__ == "__main__":
    asyncio.run(main())
