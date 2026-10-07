# File Organizer

A small Python script that cleans up a messy folder by sorting files into subfolders by file type.

## What it does

Before:
```
Downloads/
  photo.jpeg
  notes.txt
  song.mp3
  report.docx
  script.py
  data.xyz
```

After:
```
Downloads/
  Images/
    photo.jpeg
  Documents/
    notes.txt
    report.docx
  Music/
    song.mp3
  Python Files/
    script.py
  data.xyz
```

Files with an unknown extension are skipped and left where they are.

## Supported file types

| Extension | Folder |
|---|---|
| `.jpeg` | Images |
| `.txt` | Documents |
| `.docx` | Documents |
| `.mp3` | Music |
| `.py` | Python Files |

More types can be added by editing the `folders` dictionary.

## How it works

1. Loops over every file in the target folder
2. Looks up the file's extension in a dictionary
3. Creates the destination folder if it doesn't exist
4. Moves the file into it
5. Skips unknown file types using `try/except KeyError`, so one odd file doesn't crash the run

## Usage

```
python organizer.py
```

The script runs `organize()` on the Downloads and Documents folders in your home directory. To organize a different folder, change the last lines of the script:

```python
organize("your_folder_name")
```

**Warning:** the script moves files and there is no undo. Test it on a throwaway folder first.

## Concepts used

- `pathlib` for working with file paths
- `shutil.move` for moving files
- dictionaries as a lookup table
- `try/except` for handling unknown file types
- functions with parameters

## Requirements

Python 3.6 or newer. No extra packages needed.

## Ideas for improvement

- Add more file types (`.jpg`, `.png`, `.pdf`, `.mp4`, `.zip`)
- Move unknown files into an `Other` folder
- Ask the user which folder to organize with `input()`
- Avoid overwriting files that already exist in the destination
- Write pytest tests for the sorting logic
