# invalid_char_checker.py

import os
import argparse
import sys

# valid chars
VALID_CHARS = set(
    # English letters and numbers
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # Basic symbols and whitespace characters
    " \t\n\r\0\b\x0c"
    # Common punctuation symbols
    ",.;:!?()[]{}'\"`+-*/%=<>|&@#$^~\\_"
)

def is_valid_char(char):
    # Check if it is a valid ASCII character
    if char in VALID_CHARS:
        return True
    
    # Get the Unicode code point of the character
    code_point = ord(char)
    
    # Check the range of Chinese characters (CJK Unified Kanji)
    if 0x4E00 <= code_point <= 0x9FFF:
        return True
    
    # Check the range of Japanese hiragana
    if 0x3040 <= code_point <= 0x309F:
        return True
    
    # Check the range of Japanese katakana
    if 0x30A0 <= code_point <= 0x30FF:
        return True
    
    # Check the range of Korean characters
    if 0xAC00 <= code_point <= 0xD7AF:
        return True
    
    # Check the range of Russian characters (Cyrillic alphabet)
    if (0x0400 <= code_point <= 0x04FF) or (0x0500 <= code_point <= 0x052F):
        return True

    # Check the range of Emoji
    if (0x1F600 <= code_point <= 0x1F64F) or (0x1F300 <= code_point <= 0x1F5FF) or (0x1F900 <= code_point <= 0x1F9FF) or (0x1FA70 <= code_point <= 0x1FAFF) or (0x1F400 <= code_point <= 0x1F4FF):
        return True
    
    return False

def check_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                for char_index, char in enumerate(line):
                    if not is_valid_char(char):
                        print(f"Invalid character found in {file_path} at line {line_number}, column {char_index + 1}:")
                        print(f"Character: {char}")
                        print(f"Unicode: U+{ord(char):04X}")
                        print(f"Decimal: {ord(char)}")
                        print("-" * 50)
    except UnicodeDecodeError:
        print(f"Error: Unable to read {file_path} - File encoding is not UTF-8")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def check_directory(directory, file_extensions):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist")
        sys.exit(1)
        
    found_files = False
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(file_extensions)):
                found_files = True
                file_path = os.path.join(root, file)
                check_file(file_path)
    
    if not found_files:
        print(f"No matching files found in '{directory}'")

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Detect invalid characters in code files, support Chinese, Japanese, Korean and Russian.'
    )
    parser.add_argument(
        'directory',
        help='The directory path of the project to be checked'
    )
    parser.add_argument(
        '-e', '--extensions',
        default='.py,.java,.c,.cpp,.js,.html,.css,.txt',
        help='File extensions to be checked, separated by commas (default: .py,.java,.c,.cpp,.js,.html,.css,.txt)'
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    file_extensions = args.extensions.split(',')
    check_directory(args.directory, file_extensions)
