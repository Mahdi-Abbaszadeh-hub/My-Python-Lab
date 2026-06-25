# Code Quality Tools: Linters & Formatters

Writing messy code is easy — keeping it clean is a discipline. Two tools help you stay consistent and professional: **Pylint** (a linter) and **Black** (a formatter). Each solves a different problem.

---

## Why Code Quality Tools Matter

When code grows, readability becomes critical — for teammates, for future you, and for any open-source audience. Python has an official style guide called **PEP 8** that defines best practices for formatting and structure. Linters and formatters help you follow it automatically.

---

## Pylint — The Linter

A **linter** analyzes your code *without running it* and reports problems: style violations, logical errors, unused variables, wrong function calls, and more.

### Installation

```bash
pip install pylint
```

### Usage

```bash
pylint your_script.py
```

### What Pylint Catches

- PEP 8 style violations (spacing, naming conventions, line length)
- Logical errors (e.g., calling a function with wrong arguments)
- Unused imports or variables
- Missing docstrings
- Undefined variables

### Example Output

```
your_script.py:5:0: C0303 (trailing-whitespace) Trailing whitespace
your_script.py:12:4: E1101 (no-member) Module 'os' has no 'pathh' member
your_script.py:18:0: W0611 (unused-import) Unused import sys

Your code has been rated at 6.50/10
```

Pylint scores your code out of 10. Aim for **8+** in real projects.

---

## Black — The Formatter

A **formatter** does not report problems — it *fixes them automatically*. Black rewrites your code to be consistently formatted: correct indentation, proper spacing, consistent quotes, and more.

Black is opinionated by design. It makes formatting decisions for you so you never argue about style again.

### Installation

```bash
pip install black
```

### Usage

```bash
black your_script.py
```

Or format an entire directory:

```bash
black .
```

### What Black Fixes

- Indentation and whitespace
- Line length (default: 88 characters)
- Blank lines between functions and classes
- Trailing commas
- Quote style (converts to double quotes)

### Example — Before Black

```python
x=1+2
def greet(name,greeting='Hello'):
    print(greeting+', '+name+'!')
```

### Example — After Black

```python
x = 1 + 2


def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")
```

---

## Pylint vs Black — Key Difference

| Feature | Pylint | Black |
|---|---|---|
| Type | Linter | Formatter |
| Fixes code automatically | ❌ No | ✅ Yes |
| Catches logical errors | ✅ Yes | ❌ No |
| Enforces PEP 8 style | ✅ Yes (reports) | ✅ Yes (fixes) |
| Output | Error report | Reformatted file |

---

## Recommended Workflow

Use both tools together for maximum benefit:

```bash
# Step 1: Auto-format with Black
black your_script.py

# Step 2: Check for remaining issues with Pylint
pylint your_script.py

# Step 3: Fix any logical errors Pylint reports manually
```

---

## Pro Tips

- Run Black **before** committing any code to Git — it keeps your diffs clean.
- Add Pylint to your CI/CD pipeline to enforce quality on every push.
- Most modern editors (VS Code, PyCharm) support both tools as plugins for real-time feedback.
- You can configure Black's line length in a `pyproject.toml` file if the default (88) doesn't suit your project.

---

## Quick Reference

```bash
# Install both tools
pip install pylint black

# Format a file
black filename.py

# Lint a file
pylint filename.py

# Lint with a minimum score requirement (useful in CI)
pylint --fail-under=8 filename.py
```

---

*Part of [My-Python-Lab](https://github.com/Mahdi-Abbaszadeh-hub/My-Python-Lab) — a hands-on Python learning repository.*