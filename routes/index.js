const routes = require('express').Router();
const currencies = require('./digital_currencies');

routes.use('/digital_currencies', currencies);

routes.get('/', (req, res) => {
  res.status(200).json({ message: 'Connected!' });
});

module.exports = routes;
