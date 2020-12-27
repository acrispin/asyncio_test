import asyncio
import time


def count():
    print("func start")
    time.sleep(1)
    print("func end")


async def fib_async(term):
    if term <= 1:
        return term
    else:
        rs = await fib_async(term - 1) + await fib_async(term - 2)
        return rs


async def hello():
    print('Hello ...')
    # await asyncio.sleep(5)
    await fib_async(31)
    print('... World!')


async def main_async():
    await asyncio.gather(hello(), hello())


def main():
    funcs = [count, count, count]
    for func in funcs:
        func()


if __name__ == '__main__':
    asyncio.run(main_async())
    start = time.time()
    main()
    end = time.time()
    print(f"Time elapse count: {end-start}")

"""
python async_bad.py
python -m async_bad
"""
