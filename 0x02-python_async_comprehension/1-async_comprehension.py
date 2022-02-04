#!/usr/bin/env python3
'''
Return 10 random numbers using an async comprehensing over async_generator
'''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ 10 random numbers """
    return [n async for n in async_generator()]
