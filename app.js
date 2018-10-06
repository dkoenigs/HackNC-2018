var express = require('express');
/*Importing controller/a function containing the
functionality of the controller*/
var todoController = require('./controllers/todoController');


var app = express();

//Set up template engine
app.set('view engine', 'ejs');

//Static files
app.use(express.static('./public'));

//Fire controllers/make accessible
todoController(app);

//Listen to port
app.listen(3000);
console.log('Listening to port 3000');

//NOTE: when count excees single digits, there is an error!
