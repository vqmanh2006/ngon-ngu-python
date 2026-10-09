<?php

declare(strict_types=1);

function auth_data_file_path(): string
{
    $dataDir = __DIR__ . '/data';
    if (!is_dir($dataDir)) {
        mkdir($dataDir, 0775, true);
    }

    $filePath = $dataDir . '/users.json';
    if (!file_exists($filePath)) {
        file_put_contents($filePath, json_encode([], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
    }

    return $filePath;
}

function load_users(): array
{
    $filePath = auth_data_file_path();
    $content = file_get_contents($filePath);
    if ($content === false || trim($content) === '') {
        return [];
    }

    $decoded = json_decode($content, true);
    return is_array($decoded) ? $decoded : [];
}

function save_users(array $users): bool
{
    $filePath = auth_data_file_path();
    $payload = json_encode($users, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    if ($payload === false) {
        return false;
    }

    return file_put_contents($filePath, $payload, LOCK_EX) !== false;
}

function find_user_by_username(string $username): ?array
{
    foreach (load_users() as $user) {
        if (($user['username'] ?? '') === $username) {
            return $user;
        }
    }

    return null;
}

function normalize_username(string $value): string
{
    return trim($value);
}

function normalize_phone(string $value): string
{
    return preg_replace('/\s+/', '', trim($value)) ?? '';
}

function validate_registration(array $input): array
{
    $errors = [];

    $username = normalize_username((string) ($input['username'] ?? ''));
    $password = (string) ($input['password'] ?? '');
    $gender = (string) ($input['gender'] ?? '');
    $email = trim((string) ($input['email'] ?? ''));
    $phone = normalize_phone((string) ($input['phone'] ?? ''));

    if ($username === '') {
        $errors['username'] = 'Vui lòng nhập tên tài khoản.';
    } elseif (mb_strlen($username) < 3 || mb_strlen($username) > 30) {
        $errors['username'] = 'Tên tài khoản phải từ 3 đến 30 ký tự.';
    } elseif (!preg_match('/^[A-Za-z0-9_\.]+$/', $username)) {
        $errors['username'] = 'Tên tài khoản chỉ gồm chữ, số, dấu gạch dưới hoặc dấu chấm.';
    } elseif (find_user_by_username($username) !== null) {
        $errors['username'] = 'Tên tài khoản đã tồn tại.';
    }

    if ($password === '') {
        $errors['password'] = 'Vui lòng nhập mật khẩu.';
    } elseif (strlen($password) < 6 || strlen($password) > 255) {
        $errors['password'] = 'Mật khẩu phải từ 6 ký tự trở lên.';
    }

    $allowedGenders = ['male', 'female', 'other'];
    if (!in_array($gender, $allowedGenders, true)) {
        $errors['gender'] = 'Vui lòng chọn giới tính hợp lệ.';
    }

    if ($email === '') {
        $errors['email'] = 'Vui lòng nhập email.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Email không đúng định dạng.';
    } elseif (mb_strlen($email) > 254) {
        $errors['email'] = 'Email quá dài.';
    }

    if ($phone === '') {
        $errors['phone'] = 'Vui lòng nhập số điện thoại.';
    } elseif (!preg_match('/^(?:\+84|0)[0-9]{9,10}$/', $phone)) {
        $errors['phone'] = 'Số điện thoại không hợp lệ (ví dụ: 0912345678 hoặc +84912345678).';
    }

    return [
        'errors' => $errors,
        'clean' => [
            'username' => $username,
            'password' => $password,
            'gender' => $gender,
            'email' => $email,
            'phone' => $phone,
        ],
    ];
}

function register_user(array $cleanData): bool
{
    $users = load_users();
    $users[] = [
        'username' => $cleanData['username'],
        'password_hash' => password_hash($cleanData['password'], PASSWORD_DEFAULT),
        'gender' => $cleanData['gender'],
        'email' => $cleanData['email'],
        'phone' => $cleanData['phone'],
        'created_at' => date('c'),
    ];

    return save_users($users);
}

function validate_login(array $input): array
{
    $errors = [];

    $username = normalize_username((string) ($input['username'] ?? ''));
    $password = (string) ($input['password'] ?? '');

    if ($username === '') {
        $errors['username'] = 'Vui lòng nhập tên đăng nhập.';
    }

    if ($password === '') {
        $errors['password'] = 'Vui lòng nhập mật khẩu.';
    }

    if ($errors !== []) {
        return [
            'errors' => $errors,
            'username' => $username,
            'user' => null,
        ];
    }

    $user = find_user_by_username($username);
    if ($user === null || !password_verify($password, (string) ($user['password_hash'] ?? ''))) {
        $errors['general'] = 'Tên đăng nhập hoặc mật khẩu không đúng.';
        return [
            'errors' => $errors,
            'username' => $username,
            'user' => null,
        ];
    }

    return [
        'errors' => [],
        'username' => $username,
        'user' => $user,
    ];
}

function esc(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
}
