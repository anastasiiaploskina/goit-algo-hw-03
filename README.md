
# File Organizer and Koch Snowflake Visualizer

This project consists of two independent tasks, each in its own folder:

- `task_1/`: A file sorting utility that organizes files by extension.
- `task_2/`: A fractal visualizer that draws a Koch snowflake using Turtle graphics.

---

## Directory Structure

```

.
├── task_1/
│   └── main.py
├── task_2/
│   └── snowflake.py

````
---

## Task 1: File Sorter (`task_1/main.py`)

### Description

Recursively copies files from a source directory to a destination. Files are organized into subdirectories named after their file extensions (e.g. `pdf`, `jpg`, `txt`). Duplicate filenames are automatically renamed with incremental suffixes.

### Usage

```bash
python3 main.py <source_directory> [destination_directory]
````

* `<source_directory>`: Path to the directory you want to sort (required).
* `[destination_directory]`: Optional output path. Defaults to `dist/`.

### Example

```bash
python3 main.py ./Downloads ./Sorted
```

This will sort files from `Downloads` into folders like `Sorted/pdf`, `Sorted/mp3`, etc.

---

## Task 2: Koch Snowflake (`task_2/snowflake.py`)

### Description

Generates a Koch snowflake using the Turtle graphics module. The shape is constructed recursively, with options for controlling depth and size.

### Usage

```bash
python3 snowflake.py [-o ORDER] [-s SIZE]
```

* `-o`, `--order`: Recursion depth (default: 3)
* `-s`, `--size`: Length of each side (default: 600)

### Example

```bash
python3 snowflake.py -o 4 -s 400
```

This will draw a Koch snowflake of order 4 with side length 400 pixels.

---

## Requirements

* Python 3.6 or newer
* No external dependencies

Uses the following Python standard libraries:

* `argparse`
* `pathlib`
* `shutil`
* `turtle`

---

## Notes

* The sorter will skip the destination folder if it's within the source path.
* Duplicate files are renamed automatically using a numeric suffix to avoid overwriting.
* Turtle graphics requires a GUI. If run in a headless environment, the snowflake script may fail to open a window.

---
