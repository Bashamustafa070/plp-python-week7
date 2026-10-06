# PLP Python Week 7 Assignment: Shopping List Manager

## File Descriptions
- **list_warmup.py**: Demonstrates basic list operations including index access, appending items, removing elements, and tracking length.
- **shopping_list.py**: An interactive command-line application that allows users to manage their shopping list dynamically via an input loop without crashing.
- **list_report.py**: Generates a structured breakdown from a predefined list, outputting numbered entries, item name length conditions, and the longest item name.

## Submission Contents
- `list_warmup.py`
- `shopping_list.py`
- `list_report.py`
- `README.md`
- `SCREENSHOTS/` (save assignment screenshots here; Windows treats `screenshots/` and `SCREENSHOTS/` as the same folder)

## Question Answer
**Why is it safer to check `in` before calling `.remove()`?**
Checking if an item exists using the `in` operator before calling `.remove()` prevents the program from crashing with a `ValueError` when a user attempts to delete an item that isn't on the list. It allows the program to handle missing values gracefully by presenting a user-friendly message instead of abruptly terminating.