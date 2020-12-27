import asyncio


async def waiter() -> None:
    task1 = asyncio.create_task(cook('1 Pasta', 5))
    task2 = asyncio.create_task(cook('2 Caesar Salad', 3))
    task3 = asyncio.create_task(cook('3 Lamb Chops', 9))

    await task1
    await task2
    await task3


async def cook(order: str, time_to_prepare: int) -> None:
    print(f'{order} getting order.')
    await asyncio.sleep(time_to_prepare)
    print(order, 'ready')


if __name__ == '__main__':
    asyncio.run(waiter())
