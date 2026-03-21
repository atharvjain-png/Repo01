# Assignment: Git and Python Concepts

## Overview
This repository contains my assignment work on Python data types and Git concepts.

# Task 1: Identity Investigation
In this task, I used `id()` to check memory locations of variables before and after changing them.

I observed that:
- Immutable types (int, string, tuple) create new objects when changed
- Mutable types (list, dictionary) stay in the same memory location

# Task 2: Git Commit Immutability

I created multiple commits like Version 1 and Version 2.
I noticed that even after making changes, the older versions are still present in Git history.
This shows that Git does not delete old commits. It creates new ones for every change.

# Task 3: Nested List Copy

I created a nested list and copied it using `list()`.
After changing the copied list, the original list also changed.
This happens because `list()` makes a shallow copy, so inner lists are shared.

# Task 4: Commit Hash Change

I created a file and committed it, then modified the commit message using `git commit --amend`.
After that, I checked the commit hash again.
The hash changed, which shows that even a small change creates a new commit.

# Files
- identity_atharv.py
- change.py
- data.py
- evidence.md



## Conclusion
From this assignment, I understood:
- Difference between mutable and immutable data types
- Concept of shallow copy
- Git stores all commits permanently
- Commit hash changes if anything in commit changes
