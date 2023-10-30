Assignment statements in Python do not copy objects, they create bindings between a target and an object.

#### The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):

#### A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.

#### A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

#### Shallow copies of dictionaries can be made using dict.copy(), 
#### lists by assigning a slice of the entire list, for example, copied_list = original_list[:].



**Shallow Copy:**

A shallow copy of an object is a new object that is a copy of the original object with a new reference. However, the elements within the new object still reference the same objects as the original object. In other words, the outer structure is copied, but the inner objects are still shared between the original and the copy.

You can create a shallow copy of an object using the `copy` module's `copy()` function or by using slicing. Here's an example:

```python
import copy

original_list = [1, [2, 3], 4]
shallow_copy_list = copy.copy(original_list)  # Using copy.copy()
shallow_copy_list[1][0] = 99  # This will affect both the original and the copy
print(original_list)  # [1, [99, 3], 4]
print(shallow_copy_list)  # [1, [99, 3], 4]
```

As you can see, when you modify an element within the inner list of the shallow copy, it also affects the original list because they share the same inner list.

**Deep Copy:**

A deep copy of an object is a new object that is a completely independent copy of the original object, including all nested objects. Changes made to the deep copy do not affect the original object, and vice versa.

You can create a deep copy of an object using the `copy` module's `deepcopy()` function. Here's an example:

```python
import copy

original_list = [1, [2, 3], 4]
deep_copy_list = copy.deepcopy(original_list)  # Using copy.deepcopy()
deep_copy_list[1][0] = 99  # This only affects the deep copy
print(original_list)  # [1, [2, 3], 4]
print(deep_copy_list)  # [1, [99, 3], 4]
```

In this case, modifying the deep copy does not affect the original list because they are entirely independent copies.












#### Shallow copy creates a new object with references to the same nested objects as the original.
#### Deep copy creates a new object with entirely independent copies of all nested objects, making it immune to changes in the original.

```python
original_classroom = [['Alice', 85], ['Bob', 92], ['Charlie', 78]]
```

**Shallow Copy:**

With a shallow copy, you create a new list that references the same student sublists as the original list. Here's how you would create a shallow copy:

```python
import copy

shallow_copy_classroom = copy.copy(original_classroom)
```

Now, both `original_classroom` and `shallow_copy_classroom` point to the same student sublists:

```python
original_classroom[0][1] = 90
print(original_classroom)  # Output: [['Alice', 90], ['Bob', 92], ['Charlie', 78]]
print(shallow_copy_classroom)  # Output: [['Alice', 90], ['Bob', 92], ['Charlie', 78]]
```

Modifying the test score of a student in `original_classroom` also changes the same student in `shallow_copy_classroom`. This is because they share the same student sublists.

**Deep Copy:**

With a deep copy, you create a completely independent copy of the original list, including all nested objects. Here's how you would create a deep copy:

```python
import copy

deep_copy_classroom = copy.deepcopy(original_classroom)
```

Now, `deep_copy_classroom` is an entirely separate copy of the classroom:

```python
original_classroom[0][1] = 85  # Reset Alice's score in the original classroom
print(original_classroom)  # Output: [['Alice', 85], ['Bob', 92], ['Charlie', 78]]
print(deep_copy_classroom)  # Output: [['Alice', 90], ['Bob', 92], ['Charlie', 78]]
```

Modifying the test score of a student in `original_classroom` does not affect `deep_copy_classroom`. They are entirely independent copies.








Consider a custom class called `Person`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
```

Now, let's create instances of the `Person` class and work with shallow and deep copies:

**Shallow Copy with Custom Objects:**

With a shallow copy, we'll create a new list that references the same `Person` objects as the original list:

```python
import copy

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
original_list = [person1, person2]

shallow_copy_list = copy.copy(original_list)

# Modifying an attribute of a Person object in the original list
person1.age = 35

print(original_list[0])         # Output: Name: Alice, Age: 35
print(shallow_copy_list[0])     # Output: Name: Alice, Age: 35
```

Both `original_list` and `shallow_copy_list` reference the same `Person` objects. Therefore, when we modify an attribute (e.g., `age`) of a `Person` object in the original list, it also affects the same object in the shallow copy.

**Deep Copy with Custom Objects:**

With a deep copy, we'll create an entirely independent copy of the original list, including new copies of the `Person` objects:

```python
import copy

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
original_list = [person1, person2]

deep_copy_list = copy.deepcopy(original_list)

# Modifying an attribute of a Person object in the original list
person1.age = 35

print(original_list[0])         # Output: Name: Alice, Age: 35
print(deep_copy_list[0])        # Output: Name: Alice, Age: 30
```

In this case, modifying an attribute of a `Person` object in the original list does not affect the `Person` object in the deep copy. They are entirely independent copies.







#### For simple object(without nested object) Shallow copy and deep copy look like similar

import copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def str(self):
        return f"Name: {self.name}, Age: {self.age}"

person1 = Person("Alice", 30)
person2 = copy.copy(person1)
print(person1.str())
print(person2.str())
person1.age = 35
print(person1.str())
print(person2.str())

Name: Alice, Age: 30
Name: Alice, Age: 30
Name: Alice, Age: 35
Name: Alice, Age: 30




import copy
thislist = [1,2,3,4,5]
shallow_copy = copy.copy(thislist)
print(thislist)
print(shallow_copy)

thislist[0]= 9
print(thislist)

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[9, 2, 3, 4, 5]
