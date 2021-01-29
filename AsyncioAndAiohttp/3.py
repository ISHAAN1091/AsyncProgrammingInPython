import asyncio
import aiohttp
# import time


async def fetchFromGoogle():
    url = "https://www.google.com/"
    session = aiohttp.ClientSession()
    resp = await session.get(url)
    # await resp
    await resp.content.read()
    await session.close()


async def main():
    print(time.strftime('%X'))
    # Use asyncio.gather() to run multiple commands asynchronously
    await asyncio.gather(
        *[
            fetchFromGoogle() for _ in range(20)
        ]
    )
    print(time.strftime('%X'))
    # if you would have ran fetchFromGoogle() synchronously that is called it 20 times one after another
    # it would have taken more time than asynchronous calls as they are taking place one after another not simultaneously

if __name__ == "__main__":
    asyncio.run(main())
