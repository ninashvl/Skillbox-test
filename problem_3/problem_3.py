import asyncio
import aiohttp
from tqdm import tqdm

URL = input('Введите URL')

async def get(url):
    async with aiohttp.ClientSession() as session:
        print('Starting {}'.format(url))
        async with session.get(url) as response:
            data = await response.text()
            print('{}: {} bytes: {}'.format(url, len(data), data))
            return data

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    futures = [get(URL) for i in tqdm(range(1000))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))