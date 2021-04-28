const express = require('express');

const router = express.Router();

const { dongers, tables, tiny } = require('../dongrs.json');

router.get('/tables/flip', (req, res) => {
  const selectedFlip = tables.flip[Math.floor(Math.random() * tables.flip.length)];
  res.status(200).send(selectedFlip);
});

router.get('/tables/fix', (req, res) => {
  const selectedFix = tables.fix[Math.floor(Math.random() * tables.fix.length)];
  res.status(200).send(selectedFix);
});

router.get('/dongers/rand', (req, res) => {
  const selectedDonger = dongers[Math.floor(Math.random() * dongers.length)];
  res.status(200).send(selectedDonger);
});

function shittify(input) {
  if (!input || !input.length) {
    return 'no';
  }
  const result = input.split('').map(char => {
    console.log('Testing char=%s', char);
    if (char.match(/[a-zA-Z0-9]/)) {
      return `:${char.toLowerCase()}_:`;
    }
    return ' ';
  });
  return result.join('');
}

router.get('/shittify/:phrase([a-zA-Z0-9%20]+)', (req, res) => {
  const { phrase } = req.params;
  if (!phrase || !phrase.length) {
    res.status(400).send('no');
    return;
  }

  res.status(200).send(shittify(phrase));
});

function tinify(input) {
  if (!input || !input.length) {
    return 'no';
  }
  return input.split('').map(char => tiny[char.toLowerCase()] || char).join('');
}

router.get('/tinify/:phrase([a-zA-Z0-9%20]+)', (req, res) => {
  const { phrase } = req.params;
  if (!phrase || !phrase.length) {
    res.status(400).send('no');
    return;
  }

  res.status(200).send(tinify(phrase));
});

module.exports = {
  Router: router,
}
