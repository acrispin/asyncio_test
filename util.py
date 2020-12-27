
from typing import ClassVar


def fib_sync(term):
    if term <= 1:
        return term
    else:
        rs = fib_sync(term - 1) + fib_sync(term - 2)
        return rs


async def fib_wrapper_async(term):
    return fib_sync(term)


async def fib_async(term):
    if term <= 1:
        return term
    else:
        rs = await fib_async(term - 1) + await fib_async(term - 2)
        return rs


if __name__ == "__main__":
    _term = 32
    print(fib_sync(_term))
    import asyncio
    loop = asyncio.get_event_loop()
    t1 = loop.create_task(fib_wrapper_async(_term))
    t2 = loop.create_task(fib_async(_term))
    print(loop.run_until_complete(t1))
    print(loop.run_until_complete(t2))
