import asyncio


async def waiter() -> None:
    await cook('1 Pasta', 5)
    await cook('2 Caesar Salad', 3)
    await cook('3 Lamb Chops', 9)


async def cook(order: str, time_to_prepare: int) -> None:
    print(f'{order} getting order.')
    await asyncio.sleep(time_to_prepare)
    print(order, 'ready')


if __name__ == '__main__':
    asyncio.run(waiter())
