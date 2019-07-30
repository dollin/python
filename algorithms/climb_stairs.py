"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(funcName)s %(lineno)d] %(levelname)s: %(message)s',
)

def climb_stairs(n):
    if n <= 2:
        return max(0, n)
    return climb_stairs(n - 1) + climb_stairs(n - 2)

logging.info(f'1 = {climb_stairs(1)}')
logging.info(f'2 = {climb_stairs(2)}')
logging.info(f'3 = {climb_stairs(3)}')
logging.info(f'5 = {climb_stairs(4)}')
logging.info(f'8 = {climb_stairs(5)}')
logging.info(f'8 = {climb_stairs(6)}')
logging.info(f'8 = {climb_stairs(7)}')
logging.info(f'8 = {climb_stairs(8)}')
logging.info(f'8 = {climb_stairs(9)}')
logging.info(f'89 = {climb_stairs(35)}')
