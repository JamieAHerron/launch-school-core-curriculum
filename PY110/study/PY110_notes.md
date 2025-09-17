# PY110 Study Notes 

Below is a collection of notes taken whilst studying PY110. This is not exhaustive and only covers the areas that I personally found important/ challenging to internalize. 

## Python Sequences & Collections

A **collection** is a generic term that encompasses several container data types in Python. These containers hold multiple objects, which can be of varied types. The primary purpose of a collection is to store, retrieve, and manipulate data.

**Sequences**, on the other hand, are a subset of collections. What sets them apart is their inherent ability to maintain order. In a sequence, each element has a definite position, defined by its index, which starts from zero and increments by one for each subsequent element.

It's crucial to understand that all sequences are collections, but not all collections are sequences, since some collections like `dictionaries`, `sets`, and `frozen sets` do not maintain order.

## Tuples

Tuples are ordered collections of objects, similar to lists. However, unlike lists, **tuples are immutable**, meaning their content cannot be altered after creation. This makes them suitable for representing fixed collections of objects.

```Python
>>> fruits = ("apple", "banana", "cherry")
>>> fruits[0] = "strawberry"
TypeError: 'tuple' object does not support item assignment
```

However, you can replace a tuple's value with a completely new tuple by using reassignment:

```Python
>>> fruits = ("apple", "banana", "cherry")
>>> fruits
('apple', 'banana', 'cherry')

>>> fruits = ("strawberry", "banana", "cherry")
>>> fruits
('strawberry', 'banana', 'cherry')
```

## Ranges 

Compared to lists and tuples, **they are memory-efficient** since they only store the start, stop, step, and current values. The next element in a range is computed based on the current state of the range, but only when it is needed.

To access a specific element in a range, use its index.

```Python
>>> numbers = range(10, 20)
>>> numbers[3]
13

>>> numbers[-4]
16
```

The memory efficiency of ranges is why we need to **use `list` to expand** the below **ranges**. Since Python doesn't automatically expand the ranges, we have to explicitly do so ourselves.

```Python
>>> numbers = range(5, 10)
>>> list(numbers)
[5, 6, 7, 8, 9]

>>> numbers = range(5, 0, -1)
>>> list(numbers)
[5, 4, 3, 2, 1]
```

What are the defining characteristics that make a collection a sequence in Python? Which characteristics can vary between different types of sequences?

<details>
<summary>Show answer</summary>
Sequences in Python are collections of items that are ordered and accessible by their position (index). All sequences support indexing, slicing, and iteration. However, some characteristics vary between sequence types, for example, mutability (lists are mutable; tuples, strings, and ranges are immutable) and memory efficiency (ranges are more memory-efficient because they generate values on demand rather than storing them all explicitly).
</details>

## Operations on Sequences


