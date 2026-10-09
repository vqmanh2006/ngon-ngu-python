# ngon-ngu-python

Repository này chứa các bài tập Python theo từng buổi (`buoi1` ... `buoi5`).

## Chạy giao diện đăng nhập/đăng ký bằng PHP

Phần đăng nhập/đăng ký được thêm ở thư mục gốc với các file:
- `login.php`
- `register.php`
- `auth_lib.php`
- `index.php`

### Yêu cầu
- PHP 8.1+ (đã kiểm tra với PHP 8.3)

### Cách chạy
```bash
cd /home/runner/work/ngon-ngu-python/ngon-ngu-python
php -S 127.0.0.1:8000
```

Mở trình duyệt:
- http://127.0.0.1:8000/login.php (đăng nhập)
- http://127.0.0.1:8000/register.php (đăng ký)

Dữ liệu tài khoản được lưu cục bộ tại `data/users.json` (tự tạo khi chạy lần đầu), mật khẩu được băm bằng `password_hash`.
