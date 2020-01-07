const path = require('path');
const express = require('express');
const app = express();
const port = process.env.PORT || 5000;
const multer  = require('multer');
const exec = require("child_process").exec;

// Create a DiskStorage system so that we can modify the filenames
const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, path.resolve(__dirname, 'uploads')),
  filename: (req, file, cb) => cb(null, Date.now() + '.wav'),
});

// Then initialise the multer middleware using the DiskStorage system
const upload = multer({ storage: storage })

// console.log that your server is up and running
app.listen(port, () => console.log(`Listening on port ${port}`));

// Declare the route that receives the audio file
app.post('/recording', upload.single('audio'), function (req, res) {
  // Log the file coming in
  console.log(req.file);

  // Spawn python process
  const scriptPath = path.resolve(__dirname, '..', 'mfcc', 'wav_to_mfcc.py');
  const pythonProcess = exec(`python3 "${scriptPath}" "${req.file.path}"`, (error, stdout, stderr) => {
    if (error || stderr) {
      // Log error message to console
      console.log('Received error from python: ', error, stderr);

      // Return error to front-end
      return res.sendStatus(500);
    }

    console.log('Received data from python: ', stdout);

    // Defer response
    return res.send({ mfcc: stdout });
  });
});
