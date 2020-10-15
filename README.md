# NicePrice
![alt text](https://github.com/hamedpa/NicePrice/raw/master/cover/cryptocurrency_plain_7%20(1).jpg)

API and telegram bot for retrieving price of digital currencies and metals

<h3>Features</h3>

1- access data in json format

2- don't need any token (free)


<h2>Download</h2>
  
  <p>download project with below commad</p>
  
    git clone https://github.com/hamedpa/NicePrice

<h2>Requirements</h2>

  <p>install requirements with below commad</p>
  
    npm i && pip install -r requirements.txt

<h2>Usage</h2>

<p>first step : you should run below commad for running API</p>

    nodemon index.js

<p>that's it API is ready</p>

<p>for get all prices of digital currencies you need to send request to below address</p>

    http://localhost:3000/digital_currencies

<p>output (JSON format) look like this</p>

    "digital_currencies":[
          {
             "asset":"BTC",
             "price":"$11,421.00",
             "market cap":"$211.47B",
             "total exchange volume":"$19.04B",
             "returns 24h":"0.41%",
             "total supply":"18.52M",
             "category":"Currency",
             "value proposition":"Digital gold"
          },
          
<p>if you looking for specific digital currency information  you will need to enter asset like bellow address</p>
    
      http://localhost:3000/digital_currencies/ETH
      
<p>and the result like this</p>

      {
     "digital_currencies":{
        "asset":"ETH",
        "price":"$382.76",
        "market cap":"$43.25B",
        "total exchange volume":"$9.58B",
        "returns 24h":"0%",
        "total supply":"113.00M",
        "category":"Software platform",
        "value proposition":"Global computer"
        }
      }
    
