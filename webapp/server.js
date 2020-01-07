const express = require('express');
const app = express();
const port = process.env.PORT || 5000;
const multer  = require('multer');

// Create a DiskStorage system so that we can modify the filenames
const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, 'uploads/'),
  filename: (req, file, cb) => cb(null, Date.now() + '.wav'),
});

// Then initialise the multer middleware using the DiskStorage system
const upload = multer({ storage: storage })

// console.log that your server is up and running
app.listen(port, () => console.log(`Listening on port ${port}`));

// Declare the route that receives the audio file
app.post('/recording', upload.single('audio'), function (req, res) {
  console.log(req.file);
  res.send({ express: 'ok' });
});
