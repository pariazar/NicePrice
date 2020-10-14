module.exports = (req, res) => {
  const digital_currencies = req.digital_currencies;

  res.status(200).json({ digital_currencies });
};
