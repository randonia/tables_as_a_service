const express = require('express');
const path = require('path');
const { Router: APIRouter } = require('./routers/api');

const { PORT = 8000 } = process.env;

const app = express();

app.get('/', (req, res) => {
  res.sendFile(path.resolve('./static/index.html'));
});

app.get('/favicon.ico', (req, res) => {
  res.sendFile(path.resolve('./static/favicon.ico'));
});

app.use('/api', APIRouter);

app.listen(PORT, () => {
  console.log(`Service started on port ${PORT}`);
});
