# Multi-language code character detection tool

[English](README.md) | [简体中文](README_zh.md) | [繁体中文](README_zh_TW.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md)


This is a Python tool for detecting invalid characters in code files. It supports detecting English, Chinese, Japanese, Korean and Russian characters and can help you find special or invisible characters in your code that may cause problems, and you can use it to detect invalid characters in your code.

## Features

- Supports multiple programming language files (default: .py, .java, .c, .cpp, .js, .html, .css, .txt)
- Support for detecting characters in multiple languages:
  - English letters and numbers
  - Chinese (CJK Unified Kanji)
  - Japanese (Hiragana and Katakana)
  - Korean (Hiragana and Katakana)
  - Russian (Cyrillic alphabet)
- Recursive checking of the entire project catalog
- Precisely locate the row and column numbers of invalid characters
- Displays the Unicode encoding value of invalid characters
- Command line parameter support
- Detailed error output
## Usage

1. Basic usage:
```bash
python invalid_char_checker.py /path/to/your/project
```

2. Specify the file type:
```bash
python invalid_char_checker.py /path/to/your/project -e .py, .java, .c, .cpp, .js, .html, .css, .txt
```

## Supported characters

1. ASCII characters:
   - English letters (a-z, A-Z)
   - Numbers (0-9)
   - Common punctuation and operators
   - Blank characters (spaces, tabs, line breaks, etc.)

2. Unicode characters:
   - Chinese characters (CJK Unified Kanji)
   - Japanese hiragana and katakana
   - Korean characters
   - Russian characters (Cyrillic alphabet)

## Caution

- Files must be encoded in UTF-8
- If an encoding error is encountered, the program will display an appropriate error message
- It is recommended that you test the program on a small scale before working on a large project.

## Error handling

- If the specified directory does not exist, the program will display an error message and exit.
- If the file is not UTF-8 encoded, the program will display an encoding error message.
- If the file is not UTF-8 encoded, an encoding error will be displayed. Other errors while processing the file will be caught and detailed information will be displayed.

## License

MIT License
