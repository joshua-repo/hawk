const express = require('express');
const axios = require("axios");
const router = express.Router();
const APIConf = require("../api_config");

/**
 * fetch ticker history data
 * with /aggs/ticker/<ticker_name>
 */
router.get('/appl', async (req, res, next) => {
  const data = await axios.get(`${APIConf.api_domain}${APIConf.api_version_v3}/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=${APIConf.api_key}`);
  console.log(data.data);
  res.json(data.data);
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
