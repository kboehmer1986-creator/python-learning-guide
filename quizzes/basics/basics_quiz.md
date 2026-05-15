# Python Basics Quiz

This quiz is designed to test your understanding of **basic Python concepts**. Try to answer each question without referring to external resources.

---

## Instructions
- Answer each question to the best of your ability.
- After completing the quiz, check your answers against the solutions provided at the end.
- Each question is worth 1 point.

---

## Section 1: Variables and Data Types

### Question 1
What is the output of the following code?

x = 5
y = 2
print(x + y)

- A) 7
- B) 52
- C) 10
- D) Error

**Answer:** [ ]

---

### Question 2
Which of the following is not a valid variable name in Python?
- A) `my_var`
- B) `2var`
- C) `_var`
- D) `var2`

**Answer:** [ ]

---

### Question 3
What is the data type of the value `3.14` in Python?
- A) `int`
- B) `float`
- C) `str`
- D) `bool`

**Answer:** [ ]

---

### Question 4
How do you convert the string `"123"` to an integer in Python?
- A) `int("123")`
- B) `str(123)`
- C) `float("123")`
- D) `list("123")`

**Answer:** [ ]

---

### Question 5
What is the output of the following code?
```python
print(type("Hello"))
```
- A) `<class 'int'>`
- B) `<class 'float'>`
- C) `<class 'str'>`
- D) `<class 'bool'>`

**Answer:** [ ]

---

## Section 2: Operators

### Question 6
What is the result of `10 % 3` in Python?
- A) 0
- B) 1
- C) 3
- D) 10

**Answer:** [ ]

---

### Question 7
What does the `**` operator do in Python?
- A) Multiplication
- B) Exponentiation
- C) Addition
- D) Division

**Answer:** [ ]

---

### Question 8
What is the output of the following code?

a = 10
b = 3
print(a // b)

- A) 3.333
- B) 3
- C) 4
- D) 3.0

**Answer:** [ ]

---

### Question 9
Which operator is used for **logical AND** in Python?
- A) `&&`
- B) `and`
- C) `&`
- D) `||`

**Answer:** [ ]

---

### Question 10
What is the output of the following code?

print(5 > 3 and 2 < 4)

- A) `True`
- B) `False`
- C) `5`
- D) `3`

**Answer:** [ ]

---

## Section 3: Control Flow

### Question 11
What is the output of the following code?

x = 10
if x > 5:
    print("A")
elif x > 15:
    print("B")
else:
    print("C")

- A) A
- B) B
- C) C
- D) A and B

**Answer:** [ ]

---

### Question 12
What does the `break` statement do in a loop?

- A) Skips the current iteration
- B) Exits the loop immediately
- C) Continues to the next iteration
- D) Raises an error

**Answer:** [ ]

---

### Question 13
What is the output of the following code?
```python
for i in range(3):
    print(i)
```
- A) 0 1 2
- B) 1 2 3
- C) 0 1 2 3
- D) 1 2

**Answer:** [ ]

---

### Question 14
What is the output of the following code?
```python
i = 0
while i < 3:
    print(i)
    i += 1
```
- A) 0 1 2
- B) 0 1 2 3
- C) 1 2 3
- D) Infinite loop

**Answer:** [ ]

---

### Question 15
Which statement is used to skip the current iteration of a loop?
- A) `break`
- B) `continue`
- C) `pass`
- D) `skip`

**Answer:** [ ]

---

## Section 4: Functions

### Question 16
What is the output of the following code?
```python
def add(a, b):
    return a + b

print(add(2, 3))
```
- A) 2
- B) 3
- C) 5
- D) Error

**Answer:** [ ]

---

### Question 17
What does the `return` statement do in a function?
- A) Prints the result
- B) Exits the function and returns a value
- C) Raises an error
- D) Skips the function

**Answer:** [ ]

---

### Question 18
What is the output of the following code?
```python
def greet(name="User"):
    return f"Hello, {name}!"

print(greet())
```
- A) `Hello, User!`
- B) `Hello, name!`
- C) `Hello, !`
- D) Error

**Answer:** [ ]

---

### Question 19
What is a **lambda function** in Python?
- A) A function with no name
- B) A function that can only be called once
- C) A function defined using the `lambda` keyword
- D) A built-in function

**Answer:** [ ]

---

### Question 20
What is the output of the following code?
```python
square = lambda x: x ** 2
print(square(4))
```
- A) 4
- B) 8
- C) 16
- D) Error

**Answer:** [ ]

---

## Section 5: Data Structures

### Question 21
What is the output of the following code?
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```
- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[4, 1, 2, 3]`
- D) Error

**Answer:** [ ]

---

### Question 22
How do you access the first element of a list `my_list`?
- A) `my_list[0]`
- B) `my_list[1]`
- C) `my_list.first()`
- D) `my_list.get(0)`

**Answer:** [ ]

---

### Question 23
What is the output of the following code?
```python
my_dict = {"name": "Kay", "age": 39}
print(my_dict["name"])
```
- A) `Kay`
- B) `39`
- C) `"name"`
- D) Error

**Answer:** [ ]

---

### Question 24
How do you add a new key-value pair to a dictionary `my_dict`?
- A) `my_dict.add("city", "Erfurt")`
- B) `my_dict["city"] = "Erfurt"`
- C) `my_dict.append("city", "Erfurt")`
- D) `my_dict.insert("city", "Erfurt")`

**Answer:** [ ]

---

### Question 25
What is the output of the following code?
```python
my_set = {1, 2, 3, 3, 4}
print(my_set)
```
- A) `{1, 2, 3, 3, 4}`
- B) `{1, 2, 3, 4}`
- C) `[1, 2, 3, 4]`
- D) Error

**Answer:** [ ]

---

## Section 6: Input and Output

### Question 26
What function is used to take user input in Python?
- A) `input()`
- B) `raw_input()`
- C) `print()`
- D) `scan()`

**Answer:** [ ]

---

### Question 27
What is the output of the following code?
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```
If the user enters `Kay`, what will be printed?
- A) `Hello, Kay!`
- B) `Hello, name!`
- C) `Enter your name: Hello, Kay!`
- D) Error

**Answer:** [ ]

---

### Question 28
How do you write to a file in Python?
- A) `open("file.txt", "r")`
- B) `open("file.txt", "w")`
- C) `open("file.txt", "a")`
- D) `open("file.txt", "x")`

**Answer:** [ ]

---

### Question 29
What is the output of the following code?
```python
with open("test.txt", "w") as file:
    file.write("Hello, World!")
```
- A) Creates a file named `test.txt` with the content `Hello, World!`
- B) Reads the content of `test.txt`
- C) Appends `Hello, World!` to `test.txt`
- D) Error

**Answer:** [ ]

---

### Question 30
How do you read the entire content of a file in Python?
- A) `file.read()`
- B) `file.readline()`
- C) `file.readlines()`
- D) `file.write()`

**Answer:** [ ]

---

## Solutions

### Section 1: Variables and Data Types
1. **A) 7**
2. **B) `2var`**
3. **B) `float`**
4. **A) `int("123")`**
5. **C) `<class 'str'>`**

---

### Section 2: Operators
6. **B) 1**
7. **B) Exponentiation**
8. **B) 3**
9. **B) `and`**
10. **A) `True`**

---
### Section 3: Control Flow
11. **A) A**
12. **B) Exits the loop immediately**
13. **A) 0 1 2**
14. **A) 0 1 2**
15. **B) `continue`**

---
### Section 4: Functions
16. **C) 5**
17. **B) Exits the function and returns a value**
18. **A) `Hello, User!`**
19. **C) A function defined using the `lambda` keyword**
20. **C) 16**

---
### Section 5: Data Structures
21. **B) `[1, 2, 3, 4]`**
22. **A) `my_list[0]`**
23. **A) `Kay`**
24. **B) `my_dict["city"] = "Erfurt"`**
25. **B) `{1, 2, 3, 4}`**

---
### Section 6: Input and Output
26. **A) `input()`**
27. **A) `Hello, Kay!`**
28. **B) `open("file.txt", "w")`**
29. **A) Creates a file named `test.txt` with the content `Hello, World!`**
30. **A) `file.read()`**

---
## Scoring
- **25-30 points**: Python Basics Master! 🎉
- **20-24 points**: Great job! You have a strong understanding of Python basics.
- **15-19 points**: Good start! Review the topics you struggled with.
- **Below 15 points**: Keep practicing! Python basics will become clearer with more exposure.

---
**Note**: This quiz is for self-assessment. Use it to identify areas where you need more practice.