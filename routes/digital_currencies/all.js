const data = require('../../digital_currencies.json');

module.exports = (req, res) => {
  const digital_currencies = data.digital_currencies;
  res.status(200).json({ digital_currencies });
};
