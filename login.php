<?php

declare(strict_types=1);

session_start();

require_once __DIR__ . '/auth_lib.php';

$errors = [];
$username = '';
$message = '';

if (isset($_SESSION['flash_message'])) {
    $message = (string) $_SESSION['flash_message'];
    unset($_SESSION['flash_message']);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $result = validate_login($_POST);
    $errors = $result['errors'];
    $username = $result['username'];

    if ($errors === []) {
        $_SESSION['auth_user'] = [
            'username' => $result['user']['username'],
            'email' => $result['user']['email'],
        ];
        $message = 'Đăng nhập thành công. Xin chào ' . $result['user']['username'] . '!';
    }
}

$loggedInUser = $_SESSION['auth_user']['username'] ?? null;
?>
<!doctype html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đăng nhập</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f8; margin: 0; padding: 20px; }
        .container { max-width: 420px; margin: 20px auto; background: #fff; border-radius: 8px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        h1 { margin-top: 0; font-size: 1.5rem; }
        label { display: block; margin-bottom: 6px; font-weight: 600; }
        input { width: 100%; box-sizing: border-box; padding: 10px; border: 1px solid #ccd2d8; border-radius: 4px; margin-bottom: 6px; }
        .error { color: #b00020; font-size: 0.9rem; margin-bottom: 10px; }
        .message { background: #ecfdf3; border: 1px solid #22a06b; color: #166534; padding: 10px; border-radius: 4px; margin-bottom: 12px; }
        .alert { background: #fff4f4; border: 1px solid #dc2626; color: #991b1b; padding: 10px; border-radius: 4px; margin-bottom: 12px; }
        button { width: 100%; border: none; background: #2563eb; color: #fff; padding: 10px; border-radius: 4px; cursor: pointer; font-size: 1rem; }
        button:hover { background: #1d4ed8; }
        .link-row { margin-top: 12px; text-align: center; }
        .link-row a { color: #2563eb; text-decoration: none; }
        .user-box { background: #eff6ff; border: 1px solid #93c5fd; color: #1e3a8a; padding: 10px; border-radius: 4px; margin-bottom: 12px; }
    </style>
</head>
<body>
<div class="container">
    <h1>Đăng nhập</h1>

    <?php if ($message !== ''): ?>
        <div class="message"><?= esc($message) ?></div>
    <?php endif; ?>

    <?php if ($loggedInUser !== null): ?>
        <div class="user-box">Bạn đang đăng nhập với tài khoản: <strong><?= esc((string) $loggedInUser) ?></strong></div>
    <?php endif; ?>

    <?php if (isset($errors['general'])): ?>
        <div class="alert"><?= esc($errors['general']) ?></div>
    <?php endif; ?>

    <form method="post" action="/login.php" novalidate>
        <label for="username">Tên đăng nhập</label>
        <input id="username" name="username" type="text" value="<?= esc($username) ?>" autocomplete="username">
        <?php if (isset($errors['username'])): ?>
            <div class="error"><?= esc($errors['username']) ?></div>
        <?php endif; ?>

        <label for="password">Mật khẩu</label>
        <input id="password" name="password" type="password" autocomplete="current-password">
        <?php if (isset($errors['password'])): ?>
            <div class="error"><?= esc($errors['password']) ?></div>
        <?php endif; ?>

        <button type="submit">Đăng nhập</button>
    </form>

    <div class="link-row">
        Chưa có tài khoản? <a href="/register.php">Đăng ký</a>
    </div>
</div>
</body>
</html>
