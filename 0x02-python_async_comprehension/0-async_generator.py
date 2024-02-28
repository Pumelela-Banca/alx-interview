#!/usr/bin/env python3
"""
minimum operations to get to text
"""
import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[int]:
    """
    yields float
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

if __name__ == "__main__":
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)


    asyncio.run(print_yielded_values())