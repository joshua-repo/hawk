const express = require('express');
const axios = require("axios");
const router = express.Router();
const APIConf = require("../api_config");

/**
 * fetch ticker history data
 * with /aggs/ticker/<ticker_name>
 */
router.get('/appl', async (req, res, next) => {
  try {
    const data = await axios.get(`${APIConf.api_domain_polygon}${APIConf.api_version_v3}/reference/dividends?ticker=AAPL&limit=1&apiKey=${APIConf.api_key_polygon}`);
    res.json(data.data.results);
  } catch(err) {
    next();
  }
  
});

/** 
 * fetch tickers 
 * query param @limit
 * query param @active
 * */ 

router.get("/tickers", async (req, res, next) => {
  const data = await axios.get(`${APIConf.api_domain}${APIConf.api_version_v3}/reference/tickers?active=true&limit=100&apiKey=${APIConf.api_key}`);
  res.json(data.data);

});

module.exports = router;
