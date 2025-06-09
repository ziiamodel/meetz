<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Admin Post Manager</title>
  <style>
    body { font-family: Arial; padding: 20px; }
    input, button { margin: 5px 0; padding: 10px; width: 300px; max-width: 90%; }
    .post { display: flex; gap: 10px; align-items: center; border-bottom: 1px solid #ccc; padding: 10px 0; }
    img { width: 100px; height: auto; }
    .delete-btn { background: red; color: white; border: none; padding: 5px 10px; cursor: pointer; }
  </style>
</head>
<body>
  <h1>📁 Admin Post Manager</h1>

  <!-- Add Post -->
  <div>
    <input type="text" id="thumbnail" placeholder="Thumbnail URL" required><br>
    <input type="text" id="link" placeholder="Post Link" required><br>
    <input type="text" id="caption" placeholder="Caption e.g. #art #photo" required><br>
    <button onclick="addPost()">Add Post</button>
  </div>

  <hr />

  <!-- Post List -->
  <h2>📋 Existing Posts</h2>
  <div id="postList"></div>

  <script>
    async function loadPosts() {
      const res = await fetch('/api/get_posts');
      const posts = await res.json();
      const list = document.getElementById('postList');
      list.innerHTML = '';
      posts.forEach((post, index) => {
        const div = document.createElement('div');
        div.className = 'post';
        div.innerHTML = `
          <img src="${post.thumbnail}" alt="Thumbnail" />
          <strong>${post.caption}</strong>
          <button class="delete-btn" onclick="deletePost(${index})">Delete</button>
        `;
        list.appendChild(div);
      });
    }

    async function addPost() {
      const thumbnail = document.getElementById('thumbnail').value;
      const link = document.getElementById('link').value;
      const caption = document.getElementById('caption').value;

      await fetch('/api/add_post', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ thumbnail, link, caption })
      });

      loadPosts();
      document.getElementById('thumbnail').value = '';
      document.getElementById('link').value = '';
      document.getElementById('caption').value = '';
    }

    async function deletePost(index) {
      if (!confirm("Are you sure?")) return;
      await fetch(`/api/delete_post?index=${index}`, { method: 'DELETE' });
      loadPosts();
    }

    // Initial Load
    loadPosts();
  </script>
</body>
</html>
