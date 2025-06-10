// api/get-posts.js
const fs = require('fs');
const path = require('path');

module.exports = async (req, res) => {
  const jsonPath = path.join(process.cwd(), 'posts.json');
  const data = fs.readFileSync(jsonPath);
  res.status(200).json(JSON.parse(data));
};
