import asyncio
from random import randint

"""
synchronous way;
def greet(name):
    print(f"Hello, {name}!")
    random_time_for_waiting_network_call = randint(1, 3)
    print(f"How are you, {name}? (after {random_time_for_waiting_network_call} seconds)")

def main():
    greet("Alice")
    greet("Bob")
    greet("Charlie")

output:
Hello, Alice!
(waiting 1-3 seconds)
How are you, Alice? (after 2 seconds)
Hello, Bob!
(waiting 1-3 seconds)
How are you, Bob? (after 1 seconds)
Hello, Charlie!
(waiting 1-3 seconds)
How are you, Charlie? (after 3 seconds)
"""


async def greet(name):
    print(f"Hello, {name}!")
    random_time_for_waiting_network_call = randint(1, 3)
    await asyncio.sleep(random_time_for_waiting_network_call)  # Simulates a network call or a long I/O operation
    print(f"How are you, {name}? (after {random_time_for_waiting_network_call} seconds)")


async def main():
    # Run greet functions concurrently
    await asyncio.gather(greet("Alice"), greet("Bob"), greet("Charlie"))


# Run the main function
asyncio.run(main())
