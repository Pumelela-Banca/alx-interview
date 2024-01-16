#!/usr/bin/python3
"""
coroutine called async_comprehension
that takes no arguments
"""
import asyncio
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    collects numbers random iters
    """
    return [i async for i in async_generator()]
