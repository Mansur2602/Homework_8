import os
import aiohttp
import json
import asyncio

async def fetch_json(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    new_folder = 'json_files'
    os.makedirs(new_folder, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        url = 'https://jsonplaceholder.typicode.com/posts'
        json_data = await fetch_json(session, url)

        for index, item in enumerate(json_data):
            filename = f'{new_folder}/json_{index + 1}.json'
            with open(filename, 'w') as file:
                json.dump(item, file, indent=4)

        

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
