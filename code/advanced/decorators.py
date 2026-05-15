# This file demonstrates the use of decorators in Python.

import time
import functools
from typing import Callable, Any

# --- Basic Decorator ---
def my_decorator(func: Callable) -> Callable:
    """
    A simple decorator that adds behavior before and after a function call.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapped function.
    """
    def wrapper(*args, **kwargs) -> Any:
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello() -> None:
    """A simple function that prints a greeting."""
    print("Hello!")

print("--- Basic Decorator Example ---")
say_hello()

# --- Decorator with Arguments ---
def repeat(num_times: int) -> Callable:
    """
    A decorator factory that repeats the execution of a function.

    Args:
        num_times: The number of times to repeat the function.

    Returns:
        The decorator function.
    """
    def decorator_repeat(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name: str) -> None:
    """Greets a person by name."""
    print(f"Hello, {name}!")

print("\n--- Decorator with Arguments Example ---")
greet("Kay")

# --- Decorator with Return Value ---
def timer(func: Callable) -> Callable:
    """
    A decorator that measures the execution time of a function.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return result
    return wrapper

@timer
def waste_some_time(num_times: int) -> None:
    """Wastes some time by sleeping."""
    for _ in range(num_times):
        time.sleep(0.1)

print("\n--- Decorator with Return Value Example ---")
waste_some_time(2)

# --- Decorator with Arguments and Return Value ---
def debug(func: Callable) -> Callable:
    """
    A decorator that prints the function name, arguments, and return value.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Calling: {func.__name__}")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@debug
def make_greeting(name: str, age: int = None) -> str:
    """
    Creates a greeting message.

    Args:
        name: The name to greet.
        age: The age of the person (optional).

    Returns:
        The greeting message.
    """
    if age is None:
        return f"Hello, {name}!"
    else:
        return f"Hello, {name}! You are {age} years old."

print("\n--- Decorator with Arguments and Return Value Example ---")
greeting = make_greeting("Kay", 39)
print(greeting)

# --- Chaining Decorators ---
def bold(func: Callable) -> Callable:
    """
    A decorator that wraps the return value in HTML bold tags.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

def italic(func: Callable) -> Callable:
    """
    A decorator that wraps the return value in HTML italic tags.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

@bold
@italic
def say_hello_html() -> str:
    """Returns a greeting message."""
    return "Hello, World!"

print("\n--- Chaining Decorators Example ---")
print(say_hello_html())  # Output: <b><i>Hello, World!</i></b>

# --- Class-Based Decorator ---
class CountCalls:
    """
    A class-based decorator that counts the number of times a function is called.
    """
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs) -> Any:
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello_counted() -> None:
    """A function that prints a greeting."""
    print("Hello!")

print("\n--- Class-Based Decorator Example ---")
say_hello_counted()
say_hello_counted()
say_hello_counted()

# --- Decorator with Conditions ---
def only_if(condition: bool) -> Callable:
    """
    A decorator that only executes the function if a condition is met.

    Args:
        condition: The condition to check.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if condition:
                return func(*args, **kwargs)
            else:
                print(f"Condition not met. Skipping {func.__name__}.")
                return None
        return wrapper
    return decorator

@only_if(True)
def do_something() -> str:
    """A function that does something."""
    return "Something was done!"

@only_if(False)
def do_something_else() -> str:
    """A function that does something else."""
    return "Something else was done!"

print("\n--- Decorator with Conditions Example ---")
print(do_something())  # Output: Something was done!
print(do_something_else())  # Output: Condition not met. Skipping do_something_else. None

# --- Decorator with Arguments Validation ---
def validate_args(arg_types: dict) -> Callable:
    """
    A decorator that validates the types of arguments passed to a function.

    Args:
        arg_types: A dictionary mapping argument names to their expected types.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Check positional arguments
            for i, (arg_name, arg_type) in enumerate(arg_types.items()):
                if i < len(args):
                    if not isinstance(args[i], arg_type):
                        raise TypeError(f"Argument {arg_name} must be of type {arg_type.__name__}")

            # Check keyword arguments
            for arg_name, arg_type in arg_types.items():
                if arg_name in kwargs:
                    if not isinstance(kwargs[arg_name], arg_type):
                        raise TypeError(f"Argument {arg_name} must be of type {arg_type.__name__}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_args({"a": int, "b": int})
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

print("\n--- Decorator with Arguments Validation Example ---")
print(add(2, 3))  # Output: 5
try:
    print(add("2", 3))  # Raises TypeError
except TypeError as e:
    print(f"Error: {e}")

# --- Decorator for Caching (Memoization) ---
def cache(func: Callable) -> Callable:
    """
    A decorator that caches the results of a function to avoid redundant calculations.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapped function.
    """
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        if args in cached_results:
            print(f"Returning cached result for {func.__name__}{args}")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n--- Decorator for Caching Example ---")
print(fibonacci(10))  # Output: 55 (with caching messages)
print(fibonacci(10))  # Output: Returning cached result for fibonacci(10,). 55

# --- Decorator for Logging ---
def log_to_file(filename: str) -> Callable:
    """
    A decorator that logs function calls to a file.

    Args:
        filename: The name of the file to log to.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            with open(filename, "a") as f:
                f.write(f"Called {func.__name__} with args: {args}, kwargs: {kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_to_file("function_log.txt")
def add_and_log(a: int, b: int) -> int:
    """Adds two numbers and logs the call."""
    return a + b

print("\n--- Decorator for Logging Example ---")
result = add_and_log(2, 3)
print(f"Result: {result}")  # Output: Result: 5
# Check the function_log.txt file for the log entry

# --- Decorator for Retrying on Failure ---
def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """
    A decorator that retries a function if it fails.

    Args:
        max_attempts: The maximum number of attempts.
        delay: The delay between attempts in seconds.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            print(f"All {max_attempts} attempts failed.")
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function() -> str:
    """
    A function that might fail randomly.
    """
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ValueError("Random failure!")
    return "Success!"

print("\n--- Decorator for Retrying on Failure Example ---")
try:
    result = unreliable_function()
    print(f"Result: {result}")
except ValueError as e:
    print(f"Final error: {e}")

# --- Decorator for Rate Limiting ---
def rate_limit(max_calls: int, period: float) -> Callable:
    """
    A decorator that limits the number of times a function can be called in a given period.

    Args:
        max_calls: The maximum number of calls allowed in the period.
        period: The time period in seconds.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        calls = []
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            now = time.time()
            # Remove calls older than the period
            calls[:] = [call for call in calls if now - call < period]
            if len(calls) >= max_calls:
                raise Exception(f"Rate limit exceeded. Max {max_calls} calls per {period} seconds.")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=2, period=1.0)
def limited_function() -> str:
    """A function with a rate limit."""
    return "Function executed successfully."

print("\n--- Decorator for Rate Limiting Example ---")
print(limited_function())  # Output: Function executed successfully.
print(limited_function())  # Output: Function executed successfully.
try:
    print(limited_function())  # Raises Exception
except Exception as e:
    print(f"Error: {e}")

# --- Decorator for Timing Out ---
def timeout(seconds: float) -> Callable:
    """
    A decorator that times out a function if it takes too long.

    Args:
        seconds: The maximum time allowed for the function to run.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            def handle_timeout(signum, frame):
                raise TimeoutError(f"{func.__name__} timed out after {seconds} seconds.")

            import signal
            signal.signal(signal.SIGALRM, handle_timeout)
            signal.alarm(int(seconds))

            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)  # Disable the alarm
            return result
        return wrapper
    return decorator

@timeout(2.0)
def long_running_function() -> str:
    """A function that takes a long time to run."""
    time.sleep(3)  # Sleep for 3 seconds
    return "Function completed."

print("\n--- Decorator for Timing Out Example ---")
try:
    result = long_running_function()
    print(f"Result: {result}")
except TimeoutError as e:
    print(f"Error: {e}")

# --- Practical Example: Decorator for Input Validation ---
def validate_input(min_value: float = None, max_value: float = None) -> Callable:
    """
    A decorator that validates the input to a function.

    Args:
        min_value: The minimum allowed value (optional).
        max_value: The maximum allowed value (optional).

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for arg in args:
                if min_value is not None and arg < min_value:
                    raise ValueError(f"Argument {arg} is less than minimum {min_value}")
                if max_value is not None and arg > max_value:
                    raise ValueError(f"Argument {arg} is greater than maximum {max_value}")
            for key, value in kwargs.items():
                if min_value is not None and value < min_value:
                    raise ValueError(f"Argument {key}={value} is less than minimum {min_value}")
                if max_value is not None and value > max_value:
                    raise ValueError(f"Argument {key}={value} is greater than maximum {max_value}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_input(min_value=0, max_value=100)
def calculate_percentage(value: float) -> float:
    """
    Calculates a percentage value.

    Args:
        value: The value to calculate the percentage for.

    Returns:
        The percentage value.
    """
    return value / 100

print("\n--- Practical Example: Decorator for Input Validation ---")
try:
    print(calculate_percentage(50))  # Output: 0.5
    print(calculate_percentage(150))  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

# --- Practical Example: Decorator for Authentication ---
def requires_auth(username: str, password: str) -> Callable:
    """
    A decorator that checks for authentication before executing a function.

    Args:
        username: The required username.
        password: The required password.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            input_username = input("Enter username: ")
            input_password = input("Enter password: ")
            if input_username == username and input_password == password:
                return func(*args, **kwargs)
            else:
                raise PermissionError("Authentication failed.")
        return wrapper
    return decorator

@requires_auth(username="admin", password="secret")
def protected_function() -> str:
    """A function that requires authentication."""
    return "Access granted to protected content."

print("\n--- Practical Example: Decorator for Authentication ---")
try:
    result = protected_function()
    print(f"Result: {result}")
except PermissionError as e:
    print(f"Error: {e}")