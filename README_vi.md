# Công cụ kiểm tra ký tự trong mã nguồn đa ngôn ngữ

[English](README.md) | [简体中文](README_zh.md) | [繁体中文](README_zh_TW.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [Tiếng Việt](README_vi.md)

Đây là công cụ Python để phát hiện các ký tự không hợp lệ trong các tệp mã nguồn. Nó hỗ trợ phát hiện các ký tự tiếng Anh, tiếng Trung, tiếng Nhật, tiếng Hàn và tiếng Nga, có thể giúp bạn tìm ra các ký tự đặc biệt hoặc ký tự không nhìn thấy được trong mã nguồn của bạn có thể gây ra vấn đề.

## Tính năng

-   Hỗ trợ nhiều loại tệp ngôn ngữ lập trình (mặc định: .py, .java, .c, .cpp, .js, .html, .css, .txt)
-   Hỗ trợ phát hiện ký tự trong nhiều ngôn ngữ:
    -   Chữ cái và số tiếng Anh
    -   Tiếng Trung (CJK Unified Kanji)
    -   Tiếng Nhật (Hiragana và Katakana)
    -   Tiếng Hàn
    -   Tiếng Nga (bảng chữ cái Cyrillic)
    -   Tiếng Việt (bảng chữ cái Latin)
-   Kiểm tra đệ quy toàn bộ thư mục dự án
-   Xác định chính xác số dòng và cột của các ký tự không hợp lệ
-   Hiển thị giá trị mã hóa Unicode cho các ký tự không hợp lệ
-   Hỗ trợ tham số dòng lệnh
-   Đầu ra lỗi chi tiết

## Cách sử dụng

1. Sử dụng cơ bản:

```bash
python invalid_char_checker.py /path/to/your/project
```

2. Chỉ định loại tệp:

```bash
python invalid_char_checker.py /path/to/your/project -e .py,.java,.c,.cpp,.js,.html,.css,.txt
```

## Các ký tự được hỗ trợ

1. Ký tự ASCII:

    - Chữ cái tiếng Anh (a-z, A-Z)
    - Số (0-9)
    - Dấu câu và toán tử thông dụng
    - Ký tự trống (dấu cách, tab, xuống dòng, v.v.)

2. Ký tự Unicode:
    - Ký tự tiếng Trung (CJK Unified Kanji)
    - Hiragana và Katakana tiếng Nhật
    - Ký tự tiếng Hàn
    - Ký tự tiếng Nga (bảng chữ cái Cyrillic)
    - Ký tự tiếng Việt (bảng chữ cái Latin)

## Lưu ý

-   Các tệp phải được mã hóa bằng UTF-8
-   Nếu gặp lỗi mã hóa, chương trình sẽ hiển thị thông báo lỗi phù hợp
-   Khuyến nghị thử nghiệm chương trình trên quy mô nhỏ trước khi làm việc với dự án lớn

## Xử lý lỗi

-   Nếu thư mục được chỉ định không tồn tại, chương trình sẽ hiển thị thông báo lỗi và thoát
-   Nếu tệp không được mã hóa UTF-8, thông báo lỗi mã hóa sẽ được hiển thị
-   Các lỗi khác trong khi xử lý tệp sẽ được bắt và hiển thị thông tin chi tiết

## Giấy phép

Giấy phép MIT
