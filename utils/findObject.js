/* eslint no-param-reassign: 0 */
const data = require('../digital_currencies.json');

module.exports = type => {
  return (req, res, next, value) => {
    const typePlural = `${type}`;
    const obj = data[typePlural].find(t => t.asset.includes(value));

    if (obj) {
      req[type] = obj;
      next();
    } else {
      res.status(404).send(`Invalid ${type} ID`);
    }
  };
};
