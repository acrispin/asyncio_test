import asyncio
from functools import wraps, partial
import time
from awaits.awaitable import awaitable


def fib_sync(term):
    if term <= 1:
        return term
    else:
        rs = fib_sync(term - 1) + fib_sync(term - 2)
        return rs


@awaitable
def fib_wrapper_async(term):
    return fib_sync(term)


async def hello():
    print('Hello ...')
    # await asyncio.sleep(5)
    await fib_wrapper_async(31)
    print('... World!')


async def main_async():
    await asyncio.gather(hello(), hello())


async_sleep = awaitable(time.sleep)


async def count():
    print("func start")
    await async_sleep(1)
    print("func end")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    asyncio.run(main_async())
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time elapse count: {end-start}")

"""
python async_ok_3.py
python -m async_ok_3
"""
