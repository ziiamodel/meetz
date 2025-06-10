// api/save-posts.js
const fs = require('fs');
const path = require('path');

module.exports = async (req, res) => {
  const jsonPath = path.join(process.cwd(), 'posts.json');
  fs.writeFileSync(jsonPath, JSON.stringify(req.body, null, 2));
  res.status(200).json({ success: true });
};
