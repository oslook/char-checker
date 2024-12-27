# 多语言代码字符检测工具

[English](README.md) | [简体中文](README_zh.md) | [繁体中文](README_zh_TW.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [Tiếng Việt](README_vi.md)

这是一个用于检测代码文件中无效字符的 Python 工具。它支持检测英文、中文、日文、韩文和俄文字符，可以帮助您找出代码中可能导致问题的特殊字符或不可见字符。

## 功能特点

-   支持多种编程语言文件（默认：.py, .java, .c, .cpp, .js, .html, .css, .txt）
-   支持检测多种语言字符：
    -   英文字母和数字
    -   中文（CJK 统一汉字）
    -   日文（平假名和片假名）
    -   韩文
    -   俄文（西里尔字母）
    -   越南文（拉丁字母）
-   递归检查整个项目目录
-   精确定位无效字符的行号和列号
-   显示无效字符的 Unicode 编码值
-   命令行参数支持
-   详细的错误输出

## 使用方法

1. 基本用法：

```bash
python invalid_char_checker.py /path/to/your/project
```

2. 指定文件类型：

```bash
python invalid_char_checker.py /path/to/your/project -e .py,.java,.c,.cpp,.js,.html,.css,.txt
```

## 支持的字符

1. ASCII 字符：

    - 英文字母（a-z, A-Z）
    - 数字（0-9）
    - 常用标点符号和运算符
    - 空白字符（空格、制表符、换行符等）

2. Unicode 字符：
    - 中文字符 (CJK 统一汉字)
    - 日文平假名和片假名
    - 韩文字符
    - 俄文字符（西里尔字母）

## 注意事项

-   文件必须使用 UTF-8 编码
-   如果遇到编码错误，程序会显示相应的错误信息
-   建议在处理大型项目之前先 �� 小范围测试

## 错误处理

-   如果指定的目录不存在，程序会显示错误信息并退出
-   如果文件不是 UTF-8 编码，会显示编码错误提示
-   处理文件时的其他错误会被捕获并显示详细信息

## 许可证

MIT License
