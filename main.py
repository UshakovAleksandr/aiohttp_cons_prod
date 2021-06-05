import asyncio
import aiohttp as aiohttp
from time_count import async_time_count
import os
import json


async def async_get_album(url, session):
    # print(f"Запрос {url}")
    async with session.get(url) as resp:
        album = await resp.json()
    # print(f"Ответ {url}")
    return album


async def async_write_file(n, album):
    # print(f"Начинаю записывать альбом {n}")
    filename = f"{n}_async_album.json"
    with open(os.path.join("data", "async_files", filename), "w") as file:
        file.write(json.dumps(album, indent=4))
        # print(f"Записан альбом {n}")


async def tasks_union(n, url, session):
    album = await async_get_album(url, session)
    await async_write_file(n, album)


@async_time_count
async def main():
    URL = "https://jsonplaceholder.typicode.com/photos?"

    async with aiohttp.ClientSession() as session:
        tasks = []
        for n in range(1, 101):
            task = asyncio.create_task(tasks_union(n, f"{URL}albumId={n}", session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
