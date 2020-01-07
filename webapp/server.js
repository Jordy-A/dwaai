const express = require('express');
const app = express();
const port = process.env.PORT || 5000;
const multer  = require('multer');
const upload = multer();

// console.log that your server is up and running
app.listen(port, () => console.log(`Listening on port ${port}`));


// routes
app.post('/recording', upload.single('audio'), function (req, res) {
  console.log(req.file);
  res.send({ result: '10' });
});
