<?php
session_start();

$adminPin = "9999"; // Change this PIN if needed
$postsFile = "posts.json";

// Handle Admin Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['admin_pin'])) {
    if ($_POST['admin_pin'] === $adminPin) {
        $_SESSION['admin_logged_in'] = true;
        session_regenerate_id(true); // Prevent session fixation
    } else {
        $error = "❌ Incorrect PIN!";
    }
}

// Show login screen if not logged in
if (!isset($_SESSION['admin_logged_in'])) {
    ?>
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin Login</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: Arial, sans-serif; padding: 40px; text-align: center; background: #f5f5f5; }
            input, button { padding: 12px; margin: 10px 0; width: 90%; max-width: 300px; font-size: 16px; }
            button { background: #c3355d; color: white; border: none; cursor: pointer; border-radius: 5px; }
            form { display: inline-block; width: 100%; max-width: 320px; }
        </style>
    </head>
    <body>
        <h2>🔒 Admin Login</h2>
        <form method="POST">
            <input type="password" name="admin_pin" maxlength="4" placeholder="Enter Admin PIN" required><br>
            <button type="submit">Login</button>
        </form>
        <?php if (isset($error)) echo "<p style='color:red;'>$error</p>"; ?>
    </body>
    </html>
    <?php exit;
}

// Handle post deletion
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['delete_index'])) {
    $deleteIndex = (int)$_POST['delete_index'];
    $posts = file_exists($postsFile) ? json_decode(file_get_contents($postsFile), true) : [];
    if (isset($posts[$deleteIndex])) {
        array_splice($posts, $deleteIndex, 1);
        file_put_contents($postsFile, json_encode($posts, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
    }
    header("Location: ".$_SERVER['PHP_SELF']);
    exit;
}

// Handle post addition
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['thumbnail'], $_POST['link'], $_POST['caption'])) {
    $thumbnail = trim($_POST['thumbnail']);
    $link = trim($_POST['link']);
    $caption = trim($_POST['caption']);

    if (!empty($thumbnail) && !empty($link) && !empty($caption)) {
        $posts = file_exists($postsFile) ? json_decode(file_get_contents($postsFile), true) : [];
        array_unshift($posts, [
            "thumbnail" => $thumbnail,
            "link" => $link,
            "caption" => $caption
        ]);
        file_put_contents($postsFile, json_encode($posts, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
    }

    header("Location: ".$_SERVER['PHP_SELF']);
    exit;
}

// Load existing posts
$existingPosts = file_exists($postsFile) ? json_decode(file_get_contents($postsFile), true) : [];
?>

<!DOCTYPE html>
<html>
<head>
    <title>Admin Panel - Manage Posts</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f5f5f5; text-align: center; }
        input, textarea { padding: 10px; width: 90%; max-width: 400px; margin: 8px 0; font-size: 16px; border: 1px solid #ccc; border-radius: 5px; }
        button { padding: 12px 20px; background: #c3355d; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; width: 90%; max-width: 420px; }
        .gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 16px; margin-top: 20px; }
        .post-item { background: white; padding: 10px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .post-item img { width: 100%; height: auto; border-radius: 5px; cursor: pointer; transition: transform 0.2s; }
        .post-item img:hover { transform: scale(1.05); }
        .caption { font-size: 14px; margin-top: 5px; }
        .delete-button { background: #ff5555; margin-top: 8px; padding: 8px; border: none; color: white; font-size: 14px; border-radius: 5px; cursor: pointer; width: 100%; }
        form { margin-bottom: 30px; }
        hr { margin: 40px 0; border: 0; height: 1px; background: #ddd; }
    </style>
</head>
<body>
    <h2>📁 Admin Post Manager</h2>

    <form method="POST">
        <input type="text" name="thumbnail" placeholder="Thumbnail URL" required><br>
        <input type="text" name="link" placeholder="Post Link" required><br>
        <input type="text" name="caption" placeholder="Caption (e.g., #art #photo)" required><br>
        <button type="submit">Add Post</button>
    </form>

    <hr>

    <h3>📋 Existing Posts</h3>
    <div class="gallery">
        <?php foreach ($existingPosts as $index => $post): ?>
            <div class="post-item">
                <img src="<?= htmlspecialchars($post['thumbnail']) ?>" alt="Thumbnail" onclick="window.open('<?= htmlspecialchars($post['link']) ?>', '_blank')">
                <div class="caption"><?= htmlspecialchars($post['caption']) ?></div>
                <form method="POST" onsubmit="return confirm('Are you sure you want to delete this post?');">
                    <input type="hidden" name="delete_index" value="<?= $index ?>">
                    <button type="submit" class="delete-button">🗑️ Delete</button>
                </form>
            </div>
        <?php endforeach; ?>
    </div>
</body>
</html>
