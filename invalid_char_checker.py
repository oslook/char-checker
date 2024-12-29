# invalid_char_checker.py

import os
import argparse
import sys
import datetime

# valid chars
VALID_CHARS = set(
    # English letters and numbers
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # Basic symbols and whitespace characters
    " \t\n\r\0\b\x0c"
    # Common punctuation symbols
    ",.;:!?()[]{}'\"`+-*/%=<>|&@#$^~\\_"
    # Chinese punctuation symbols
    "！？，。《》（）【】『』「」﹃﹄〔〕［］｛｝：；"
    # Japanese punctuation symbols
    "。、・「」『』【】〜〝〞〟〰〡〢〣〤〥〦〧〨〩〪〭〮〯〫〬〰〱〲〳〴〵〶〷〸〹〺〻〼〽〾〿"
    # Vietnamese diacritical marks
    "áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ"
    "ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴĐ"
    # Russian letters
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    # Special characters
    "™℠℗℘℅℆℄℀℁℃℉℈℔№℗℞℟℠℡™℣"
    # Mathematical symbols
    "∀∁∂∃∄∅∆∇∈∉∊∋∌∍∎∏∐∑−∓∔∕∖∗∘∙√∛∜∝∞∟∠∡∢∣∤∥∦∧∨∩∪∫∬∭∮∯∰∱∲∳∴∵∶∷∸∹∺∻∼∽∾∿≀≁≂≃≄≅≆≇≈≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟≠≡≢≣≤≥≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡⊢⊣⊤⊥⊦⊧⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊵⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱⋲⋳⋴⋵⋶⋷⋸⋹⋺⋻⋼⋽⋾⋿"
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

    # Check the range of Vietnamese characters
    if (0x1EA0 <= code_point <= 0x1EF9):
        return True

    # Check the range of Emoji
    if (0x1F600 <= code_point <= 0x1F64F) or (0x1F300 <= code_point <= 0x1F5FF) or (0x1F900 <= code_point <= 0x1F9FF) or (0x1FA70 <= code_point <= 0x1FAFF) or (0x1F400 <= code_point <= 0x1F4FF):
        return True
    
    # Check for special characters
    if (0x2100 <= code_point <= 0x214F):  # Letterlike Symbols
        return True
        
    # Check for mathematical operators
    if (0x2200 <= code_point <= 0x22FF):  # Mathematical Operators
        return True
    
    # Check for arrows
    if (0x2190 <= code_point <= 0x21FF):  # Arrows
        return True
    
    # Check for geometric shapes
    if (0x25A0 <= code_point <= 0x25FF):  # Geometric Shapes
        return True
        
    return False

def check_file(file_path, report_file=None):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            has_invalid_chars = False
            report = []
            for line_number, line in enumerate(file, start=1):
                for char_index, char in enumerate(line):
                    if not is_valid_char(char):
                        has_invalid_chars = True
                        message = [
                            f"Invalid character found in {file_path} at line {line_number}, column {char_index + 1}:",
                            f"Character: {char}",
                            f"Unicode: U+{ord(char):04X}",
                            f"Decimal: {ord(char)}",
                            "-" * 50
                        ]
                        if report_file:
                            report.extend(message)
                        print('\n'.join(message))
            
            if report_file and has_invalid_chars:
                report_file.write('\n'.join(report) + '\n')
                
    except UnicodeDecodeError:
        error_msg = f"Error: Unable to read {file_path} - File encoding is not UTF-8"
        print(error_msg)
        if report_file:
            report_file.write(error_msg + '\n')
    except Exception as e:
        error_msg = f"Error processing {file_path}: {str(e)}"
        print(error_msg)
        if report_file:
            report_file.write(error_msg + '\n')

def check_directory(directory, file_extensions):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist")
        sys.exit(1)
    
    report_path = os.path.join(directory, 'invalid_chars_report.txt')
    with open(report_path, 'w', encoding='utf-8') as report_file:
        report_file.write(f"Invalid Characters Report\nDate: {datetime.datetime.now()}\n{'-' * 50}\n")
        
        found_files = False
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(tuple(file_extensions)):
                    found_files = True
                    file_path = os.path.join(root, file)
                    check_file(file_path, report_file)
        
        if not found_files:
            message = f"No matching files found in '{directory}'"
            print(message)
            report_file.write(message)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Detect invalid characters in code files, support Chinese, Japanese, Korean, Vietnamese and Russian.'
    )
    parser.add_argument(
        'directory',
        help='The directory path of the project to be checked'
    )
    parser.add_argument(
        '-e', '--extensions',
        nargs='+',
        default=['.py','.java','.c','.cpp','.js','.html','.css','.txt','.md','.json','.xml','.yaml','.yml','.ini','.conf','.sh','.bat','.ps1'],
        help='File extensions to be checked (default: .py .java .c .cpp .js .html .css .txt .md .json .xml .yaml .yml .ini .conf .sh .bat .ps1)'
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    file_extensions = args.extensions
    check_directory(args.directory, file_extensions)