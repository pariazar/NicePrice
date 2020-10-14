const digital_currencies = require('express').Router();

const all = require('./all');
const single = require('./single');
const findObject = require('../../utils/findObject');

digital_currencies.param('asset', findObject('digital_currencies'));

digital_currencies.get('/', all);
digital_currencies.get('/:asset', single);

module.exports = digital_currencies;
