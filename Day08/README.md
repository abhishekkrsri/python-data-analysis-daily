# Day 08 - Python Practice

Today I continued my Python learning according to the W3Schools Python tutorial sequence.

## Topics Covered

### 1. Sort Lists

Learned how to sort list items using:

- `sort()`
- Ascending order
- Descending order
- `reverse=True`
- Sorting numbers
- Sorting strings

Example:

```python
prices = [120, 95, 110, 100, 105]

prices.sort()

print(prices)
```

Output:

```text
[95, 100, 105, 110, 120]
```

---

### 2. Copy Lists

Learned how to create an independent copy of a list.

Methods practiced:

- `copy()`
- `list()`

Example:

```python
prices = [100, 105, 110]

copied_prices = prices.copy()
```

Also learned the difference between:

```python
new_list = old_list
```

and:

```python
new_list = old_list.copy()
```

---

### 3. Join Lists

Learned how to combine multiple lists.

Methods practiced:

- `+`
- `extend()`

Example:

```python
list1 = ["EURUSD", "GBPUSD"]
list2 = ["USDJPY", "XAUUSD"]

result = list1 + list2

print(result)
```

Output:

```text
['EURUSD', 'GBPUSD', 'USDJPY', 'XAUUSD']
```

---

### 4. Access Tuples

Learned how to access elements from tuples using:

- Positive indexing
- Negative indexing
- Slicing
- `len()`
- `in` operator

Example:

```python
prices = (100, 105, 110, 115)

print(prices[0])
print(prices[-1])
```

---

### 5. Update Tuples

Learned that tuples are immutable and cannot be directly changed.

To update a tuple:

```text
Tuple
  ↓
Convert to List
  ↓
Modify List
  ↓
Convert back to Tuple
```

Example:

```python
prices = (100, 105, 110)

price_list = list(prices)

price_list[1] = 200

prices = tuple(price_list)

print(prices)
```

Output:

```text
(100, 200, 110)
```

## Files

- `01_sort_lists.py`
- `02_copy_lists.py`
- `03_join_lists.py`
- `04_access_tuples.py`
- `05_update_tuples.py`

## Key Concepts Learned

- `sort()`
- `reverse=True`
- `copy()`
- `list()`
- List concatenation using `+`
- `extend()`
- Tuple indexing
- Tuple slicing
- `len()`
- `in` operator
- Tuple immutability
- Converting Tuple to List
- Converting List back to Tuple

## Progress

- ✅ Day 01 – Python Basics
- ✅ Day 02 – Loops, Lists, Tuples and Functions
- ✅ Day 03 – Dictionaries, Sets, List Comprehension, Exception Handling and File Handling
- ✅ Day 04 – String Methods, Nested Loops, Function Arguments, Lambda Functions and Modules
- ✅ Day 05 – Classes, Inheritance, Datetime Module, Random Module and JSON Handling
- ✅ Day 06 – Variable Scope, `*args`, `**kwargs`, `map()` and `filter()`
- ✅ Day 07 – Access Lists, Change Lists, Add List Items, Remove List Items and Loop Lists
- ✅ Day 08 – Sort Lists, Copy Lists, Join Lists, Access Tuples and Update Tuples

## Goal

The goal of this repository is to complete Python systematically by following the W3Schools Python tutorial sequence, understanding every important concept, practicing each topic, and gradually building a strong foundation for Django and data analysis.

## Author

**Abhishek Kumar Srivastava**