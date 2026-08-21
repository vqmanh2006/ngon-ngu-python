#import keyword
#print(keyword.kwlist)
#print("Số lượng từ khóa:", len(keyword.kwlist))
# cac tu khoa trong python
"""['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
Số lượng từ khóa: 35"""

"""Thử đặt tên biến trùng với một từ khóa, ví dụ class = 5, quan sát lỗi SyntaxError mà Python trả về rồi
giải thích."""
# from = 3
# SyntaxError: invalid syntax : đây là lỗi cú pháp, vì "from" là một từ khóa trong Python, không thể sử dụng làm tên biến.

# Tại sao True, False, None cũng là từ khóa chứ không phải định danh thông thường?
""" Vì True, False, None là các giá trị đặc biệt trong Python, chúng được sử dụng để biểu thị các trạng thái logic và giá trị không xác định.
Chúng không thể được sử dụng làm tên biến hoặc định danh thông thường vì chúng có ý nghĩa cố định trong ngôn ngữ lập trình."""