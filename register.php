<?php

declare(strict_types=1);

session_start();

require_once __DIR__ . '/auth_lib.php';

$errors = [];
$message = '';
$formData = [
    'username' => '',
    'gender' => '',
    'email' => '',
    'phone' => '',
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $validation = validate_registration($_POST);
    $errors = $validation['errors'];
    $clean = $validation['clean'];

    $formData['username'] = $clean['username'];
    $formData['gender'] = $clean['gender'];
    $formData['email'] = $clean['email'];
    $formData['phone'] = $clean['phone'];

    if ($errors === []) {
        if (register_user($clean)) {
            $_SESSION['flash_message'] = 'Đăng ký thành công. Bạn có thể đăng nhập ngay bây giờ.';
            header('Location: /login.php');
            exit;
        }

        $message = 'Không thể lưu tài khoản. Vui lòng thử lại.';
    }
}

$genderOptions = [
    'male' => 'Nam',
    'female' => 'Nữ',
    'other' => 'Khác',
];
?>
<!doctype html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đăng ký</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f8; margin: 0; padding: 20px; }
        .container { max-width: 460px; margin: 20px auto; background: #fff; border-radius: 8px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        h1 { margin-top: 0; font-size: 1.5rem; }
        label { display: block; margin-bottom: 6px; font-weight: 600; }
        input, select { width: 100%; box-sizing: border-box; padding: 10px; border: 1px solid #ccd2d8; border-radius: 4px; margin-bottom: 6px; }
        .error { color: #b00020; font-size: 0.9rem; margin-bottom: 10px; }
        .alert { background: #fff4f4; border: 1px solid #dc2626; color: #991b1b; padding: 10px; border-radius: 4px; margin-bottom: 12px; }
        button { width: 100%; border: none; background: #16a34a; color: #fff; padding: 10px; border-radius: 4px; cursor: pointer; font-size: 1rem; }
        button:hover { background: #15803d; }
        .link-row { margin-top: 12px; text-align: center; }
        .link-row a { color: #2563eb; text-decoration: none; }
    </style>
</head>
<body>
<div class="container">
    <h1>Đăng ký tài khoản</h1>

    <?php if ($message !== ''): ?>
        <div class="alert"><?= esc($message) ?></div>
    <?php endif; ?>

    <form method="post" action="/register.php" novalidate>
        <label for="username">Tên tài khoản</label>
        <input id="username" name="username" type="text" value="<?= esc($formData['username']) ?>" autocomplete="username">
        <?php if (isset($errors['username'])): ?>
            <div class="error"><?= esc($errors['username']) ?></div>
        <?php endif; ?>

        <label for="password">Mật khẩu</label>
        <input id="password" name="password" type="password" autocomplete="new-password">
        <?php if (isset($errors['password'])): ?>
            <div class="error"><?= esc($errors['password']) ?></div>
        <?php endif; ?>

        <label for="gender">Giới tính</label>
        <select id="gender" name="gender">
            <option value="">-- Chọn giới tính --</option>
            <?php foreach ($genderOptions as $key => $label): ?>
                <option value="<?= esc($key) ?>" <?= $formData['gender'] === $key ? 'selected' : '' ?>><?= esc($label) ?></option>
            <?php endforeach; ?>
        </select>
        <?php if (isset($errors['gender'])): ?>
            <div class="error"><?= esc($errors['gender']) ?></div>
        <?php endif; ?>

        <label for="email">Email</label>
        <input id="email" name="email" type="email" value="<?= esc($formData['email']) ?>" autocomplete="email">
        <?php if (isset($errors['email'])): ?>
            <div class="error"><?= esc($errors['email']) ?></div>
        <?php endif; ?>

        <label for="phone">Số điện thoại</label>
        <input id="phone" name="phone" type="text" value="<?= esc($formData['phone']) ?>" autocomplete="tel">
        <?php if (isset($errors['phone'])): ?>
            <div class="error"><?= esc($errors['phone']) ?></div>
        <?php endif; ?>

        <button type="submit">Đăng ký</button>
    </form>

    <div class="link-row">
        Đã có tài khoản? <a href="/login.php">Đăng nhập</a>
    </div>
</div>
</body>
</html>
