const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();
 
app.use(express.static('static'));

router.get('/', (req, res) => {
  res
    .status(200)
    .sendFile(path.join(__dirname, 'templates', 'index.html'))
});
 
// Start the server
const PORT = process.env.PORT || 8080;
app.use('/', router);
app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}`);
  console.log('Press Ctrl+C to quit.');
});
