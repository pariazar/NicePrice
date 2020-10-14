// Bring in our dependencies
const app = require('express')();
const routes = require('./routes');
var cron = require('node-cron');
const rateLimit = require("express-rate-limit");
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
 
const PORT = process.env.PORT || 3000;
app.use(limiter);

//  Connect all our routes to our application
app.use('/', routes);

// Turn on that server!
app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}`);
});

//Update prices every 1 minutes
cron.schedule('*/1 * * * *', () => {
  console.log('running a task every minute');
        
  
    var spawn = require("child_process").spawn; 
      
  
    var process = spawn('python',["./python_script/getCost.py"
                            ] ); 
  
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    } ) 
});