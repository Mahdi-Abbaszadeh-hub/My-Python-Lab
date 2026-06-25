# Custom Exceptions in Python

## What Is a Custom Exception?

Python provides many built-in exceptions, but in real-world projects they are often not enough.

For example, an application might need domain-specific errors such as:

- `UserNotFound`
- `InvalidEmail`
- `PaymentFailed`

In such cases, we create our own custom exception classes.

---

## Creating a Custom Exception

The simplest way to create a custom exception is by inheriting from `Exception`:

```python
class InvalidEmailError(Exception):
    pass
```

> **Important:** A custom exception must inherit from `Exception` (or one of its subclasses).

---

## Raising a Custom Exception

Once defined, the exception can be raised using the `raise` keyword:

```python
class InvalidEmailError(Exception):
    pass

def register(email):
    if "@" not in email:
        raise InvalidEmailError("Email is not valid")
```

### Example Usage

```python
register("mehdi.gmail.com")
```

### Output

```
InvalidEmailError: Email is not valid
```

---

## Catching a Custom Exception

Custom exceptions can be caught using `try` and `except`:

```python
try:
    register("mehdi.gmail.com")
except InvalidEmailError as e:
    print("Error:", e)
```

### Output

```
Error: Email is not valid
```

---

## Adding Custom Attributes

You can pass extra information along with the exception by overriding `__init__`:

```python
class InvalidEmailError(Exception):
    def __init__(self, email, message="Email is not valid"):
        self.email = email
        super().__init__(message)

def register(email):
    if "@" not in email:
        raise InvalidEmailError(email)

try:
    register("mehdi.gmail.com")
except InvalidEmailError as e:
    print(f"Error: {e} — provided value: '{e.email}'")
```

### Output

```
Error: Email is not valid — provided value: 'mehdi.gmail.com'
```

---

## Exception Hierarchy (Professional Project Pattern)

In larger applications, it is common to define a base application error and have all custom exceptions inherit from it.

### Step 1: Create a Base Error

```python
class AppError(Exception):
    pass
```

### Step 2: Inherit From the Base Error

```python
class UserNotFound(AppError):
    pass

class InvalidPassword(AppError):
    pass
```

> **Tip:** Always create a project-specific base class instead of inheriting directly from `Exception`. This keeps your error hierarchy clean and distinguishable from third-party or built-in errors.

### Step 3: Handle All App Errors in One Place

```python
try:
    login()
except AppError as e:
    print("Application error:", e)
```

This keeps error handling:

- **Structured** — errors are organized in a clear hierarchy
- **Maintainable** — easy to find and update error definitions
- **Scalable** — new errors plug in without touching existing handlers
- **Clean** — one `except` block covers all application-specific errors
