# 多語言代碼字元檢測工具

[English](README.md) | [简体中文](README_zh.md) | [繁体中文](README_zh_TW.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md)

這是一個用於檢測程式碼檔案中無效字元的 Python 工具。它支援檢測英文、中文、日文、韓文和俄文字符，可以幫助您找出程式碼中可能導致問題的特殊字符或不可見字符。

## 功能特點

- 支援多種程式語言檔案（預設：.py, .java, .c, .cpp, .js, .html, .css, .txt）
- 支援偵測多種語言字元：
 - 英文字母和數字
 - 中文（CJK統一漢字）
 - 日文（平假名和片假名）
 - 韓文
 - 俄文（西里爾字母）
- 遞歸檢查整個專案目錄
- 精確定位無效字元的行號和列號
- 顯示無效字元的 Unicode 編碼值
- 命令列參數支持
- 詳細的錯誤輸出
## 使用方法

1. 基本用法：
```
bash
python invalid_char_checker.py /path/to/your/project
```

2. 指定文件類型：
```
bash
python invalid_char_checker.py /path/to/your/project -e .py,.java,.c,.cpp,.js,.html,.css,.txt
```

## 支援的字符

1. ASCII 字元：
 - 英文字母（a-z, A-Z）
 - 數字（0-9）
 - 常用標點符號和運算符
 - 空白字元（空格、製表符、換行符等）

2. Unicode 字元：
 - 中文字元 (CJK統一漢字)
 - 日文平假名和片假名
 - 韓文字符
 - 俄文字（西里爾字母）

## 注意事項

- 文件必須使用 UTF-8 編碼
- 如果遇到編碼錯誤，程式會顯示對應的錯誤訊息
- 建議在處理大型專案之前先在小範圍測試

## 錯誤處理

- 如果指定的目錄不存在，程式會顯示錯誤訊息並退出
- 如果檔案不是 UTF-8 編碼，會顯示編碼錯誤提示
- 處理文件時的其他錯誤會被捕獲並顯示詳細信息

## 許可證

MIT License