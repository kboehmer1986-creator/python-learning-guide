# This file demonstrates the use of generators in Python.

import sys
import time

# --- Basic Generator Function ---
def simple_generator():
    """
    A simple generator that yields numbers from 1 to 5.
    """
    for i in range(1, 6):
        yield i

print("--- Basic Generator Function ---")
gen = simple_generator()
for value in gen:
    print(value)

# --- Generator with Parameters ---
def count_up_to(n):
    """
    A generator that counts up to a specified number.

    Args:
        n (int): The number to count up to.
    """
    i = 1
    while i <= n:
        yield i
        i += 1

print("\n--- Generator with Parameters ---")
for num in count_up_to(5):
    print(num)

# --- Generator Expression ---
print("\n--- Generator Expression ---")
# Similar to list comprehension but uses () instead of []
squares_gen = (x**2 for x in range(10))
for square in squares_gen:
    print(square)

# --- Infinite Generator ---
def infinite_counter():
    """
    An infinite generator that counts forever.
    """
    count = 0
    while True:
        yield count
        count += 1

print("\n--- Infinite Generator (first 5 values) ---")
inf_gen = infinite_counter()
for _ in range(5):
    print(next(inf_gen))

# --- Generator with send() Method ---
def echo():
    """
    A generator that echoes back values sent to it.
    """
    while True:
        received = yield
        print(f"Received: {received}")

print("\n--- Generator with send() Method ---")
e = echo()
next(e)  # Prime the generator
e.send("Hello")
e.send("World")

# --- Generator for Fibonacci Sequence ---
def fibonacci(limit):
    """
    A generator that yields the Fibonacci sequence up to a limit.

    Args:
        limit (int): The maximum value in the sequence.
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

print("\n--- Fibonacci Sequence Generator ---")
for num in fibonacci(100):
    print(num, end=" ")
print()

# --- Generator for Reading Large Files ---
def read_large_file(file_path, chunk_size=1024):
    """
    A generator that reads a file in chunks.

    Args:
        file_path (str): Path to the file.
        chunk_size (int): Size of each chunk in bytes.
    """
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

print("\n--- Generator for Reading Large Files ---")
# Example usage (uncomment to test with a real file):
# for chunk in read_large_file("large_file.txt"):
#     print(f"Read chunk of size {len(chunk)}")

# --- Generator Pipeline ---
def double(numbers):
    """
    A generator that doubles each number in the input.
    """
    for num in numbers:
        yield num * 2

def add_five(numbers):
    """
    A generator that adds 5 to each number in the input.
    """
    for num in numbers:
        yield num + 5

def square(numbers):
    """
    A generator that squares each number in the input.
    """
    for num in numbers:
        yield num ** 2

print("\n--- Generator Pipeline ---")
original_numbers = [1, 2, 3, 4, 5]
pipeline = square(add_five(double(original_numbers)))
for result in pipeline:
    print(result, end=" ")
print()

# --- Memory Efficiency Demonstration ---
print("\n--- Memory Efficiency Demonstration ---")
# List comprehension (creates entire list in memory)
list_comp = [x**2 for x in range(1000000)]
print(f"List comprehension memory usage: {sys.getsizeof(list_comp) / (1024 * 1024):.2f} MB")

# Generator expression (creates one item at a time)
gen_exp = (x**2 for x in range(1000000))
print(f"Generator expression memory usage: {sys.getsizeof(gen_exp)} bytes")

# --- Generator for Prime Numbers ---
def primes(limit):
    """
    A generator that yields prime numbers up to a limit.

    Args:
        limit (int): The upper limit for prime numbers.
    """
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

print("\n--- Prime Numbers Generator ---")
for prime in primes(50):
    print(prime, end=" ")
print()

# --- Generator for Time Series Data ---
def time_series(start, end, interval):
    """
    A generator that yields timestamps between start and end at a given interval.

    Args:
        start (float): Start time in seconds since epoch.
        end (float): End time in seconds since epoch.
        interval (float): Time interval in seconds.
    """
    current = start
    while current <= end:
        yield current
        current += interval

print("\n--- Time Series Generator ---")
start_time = time.time()
end_time = start_time + 10  # 10 seconds from now
for timestamp in time_series(start_time, end_time, 2):
    print(f"Timestamp: {timestamp:.2f}, Time: {time.ctime(timestamp)}")

# --- Generator with yield from ---
def chain_generators(*generators):
    """
    A generator that chains multiple generators together.

    Args:
        *generators: Variable number of generator objects.
    """
    for gen in generators:
        yield from gen

print("\n--- Generator with yield from ---")
gen1 = (x for x in range(3))
gen2 = (x for x in range(3, 6))
for num in chain_generators(gen1, gen2):
    print(num, end=" ")
print()

# --- Generator for Reading Multiple Files ---
def read_multiple_files(*file_paths):
    """
    A generator that reads multiple files line by line.

    Args:
        *file_paths: Variable number of file paths.
    """
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            for line in file:
                yield (file_path, line.strip())

print("\n--- Generator for Reading Multiple Files ---")
# Example usage (uncomment to test with real files):
# for file_path, line in read_multiple_files("file1.txt", "file2.txt"):
#     print(f"{file_path}: {line}")

# --- Generator for Pagination ---
def paginate(items, page_size):
    """
    A generator that yields pages of items.

    Args:
        items (list): The list of items to paginate.
        page_size (int): The number of items per page.
    """
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

print("\n--- Pagination Generator ---")
items = list(range(1, 21))
for page in paginate(items, 5):
    print(f"Page: {page}")

# --- Generator for Tree Traversal ---
def tree_traversal(node):
    """
    A generator that traverses a tree structure in depth-first order.

    Args:
        node: The root node of the tree.
    """
    yield node
    if hasattr(node, 'children'):
        for child in node.children:
            yield from tree_traversal(child)

print("\n--- Tree Traversal Generator ---")
# Example tree node class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return f"TreeNode({self.value})"

# Create a sample tree
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
grandchild1 = TreeNode(4)
grandchild2 = TreeNode(5)
root.children = [child1, child2]
child1.children = [grandchild1, grandchild2]

for node in tree_traversal(root):
    print(node)

# --- Generator for Cartesian Product ---
def cartesian_product(*iterables):
    """
    A generator that yields the Cartesian product of input iterables.

    Args:
        *iterables: Variable number of iterables.
    """
    if not iterables:
        yield ()
    else:
        for item in iterables[0]:
            for product in cartesian_product(*iterables[1:]):
                yield (item,) + product

print("\n--- Cartesian Product Generator ---")
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
for combination in cartesian_product(colors, sizes):
    print(combination)

# --- Generator for Permutations ---
def permutations(iterable, r=None):
    """
    A generator that yields all permutations of length r from the iterable.

    Args:
        iterable: The iterable to permute.
        r (int): The length of each permutation (default: length of iterable).
    """
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r

    if r > n:
        return

    indices = list(range(n))
    cycles = list(range(n - r + 1, n + 1))[::-1]
    yield tuple(pool[i] for i in indices[:r])

    while True:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

print("\n--- Permutations Generator ---")
for perm in permutations(['a', 'b', 'c'], 2):
    print(perm)

# --- Generator for Combinations ---
def combinations(iterable, r):
    """
    A generator that yields all combinations of length r from the iterable.

    Args:
        iterable: The iterable to combine.
        r (int): The length of each combination.
    """
    pool = tuple(iterable)
    n = len(pool)

    if r > n:
        return

    indices = list(range(r))
    yield tuple(pool[i] for i in indices)

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return

        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)

print("\n--- Combinations Generator ---")
for combo in combinations(['a', 'b', 'c', 'd'], 2):
    print(combo)

# --- Practical Example: Data Processing Pipeline ---
def read_data(file_path):
    """
    A generator that reads data from a file line by line.

    Args:
        file_path (str): Path to the file.
    """
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def parse_csv(line):
    """
    A generator that parses a CSV line into fields.

    Args:
        line (str): A line from a CSV file.
    """
    yield line.split(',')

def filter_data(fields):
    """
    A generator that filters data based on some condition.

    Args:
        fields (list): A list of fields from a CSV line.
    """
    if len(fields) >= 2 and fields[1].isdigit():
        yield fields

def process_data(file_path):
    """
    A generator pipeline for processing CSV data.

    Args:
        file_path (str): Path to the CSV file.
    """
    for line in read_data(file_path):
        for fields in parse_csv(line):
            for valid_fields in filter_data(fields):
                yield valid_fields

print("\n--- Practical Example: Data Processing Pipeline ---")
# Example usage (uncomment to test with a real CSV file):
# for data in process_data("data.csv"):
#     print(data)

# --- Practical Example: Infinite Sequence Generator ---
def infinite_sequence():
    """
    A generator that yields an infinite sequence of numbers.
    """
    num = 0
    while True:
        yield num
        num += 1

def take(n, sequence):
    """
    A generator that takes the first n items from a sequence.

    Args:
        n (int): The number of items to take.
        sequence: The sequence to take from.
    """
    for _ in range(n):
        yield next(sequence)

print("\n--- Practical Example: Infinite Sequence with take() ---")
inf_seq = infinite_sequence()
first_10 = take(10, inf_seq)
for num in first_10:
    print(num, end=" ")
print()

# --- Practical Example: Generator for Chunking Data ---
def chunked(iterable, size):
    """
    A generator that yields chunks of a specified size from an iterable.

    Args:
        iterable: The iterable to chunk.
        size (int): The size of each chunk.
    """
    it = iter(iterable)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            break
        yield chunk

from itertools import islice

print("\n--- Practical Example: Chunking Data ---")
data = range(20)
for chunk in chunked(data, 4):
    print(chunk)

# --- Practical Example: Generator for Windowed Processing ---
def windowed(iterable, size):
    """
    A generator that yields sliding windows of a specified size from an iterable.

    Args:
        iterable: The iterable to window.
        size (int): The size of each window.
    """
    it = iter(iterable)
    window = []
    for _ in range(size):
        try:
            window.append(next(it))
        except StopIteration:
            return
    yield window

    for item in it:
        window.pop(0)
        window.append(item)
        yield window

print("\n--- Practical Example: Windowed Processing ---")
data = range(10)
for window in windowed(data, 3):
    print(window)

# --- Practical Example: Generator for Lazy Evaluation ---
class LazyRange:
    """
    A lazy implementation of range that generates values on demand.
    """
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        current = self.start
        while current < self.stop if self.step > 0 else current > self.stop:
            yield current
            current += self.step

print("\n--- Practical Example: Lazy Range ---")
lazy_range = LazyRange(1, 11, 2)
for num in lazy_range:
    print(num, end=" ")
print()

# --- Practical Example: Generator for Coroutines ---
def coroutine_example():
    """
    An example of a generator used as a coroutine.
    """
    while True:
        received = yield
        print(f"Received: {received}")

print("\n--- Practical Example: Generator as Coroutine ---")
coro = coroutine_example()
next(coro)  # Prime the coroutine
coro.send("First message")
coro.send("Second message")
coro.close()  # Close the coroutine