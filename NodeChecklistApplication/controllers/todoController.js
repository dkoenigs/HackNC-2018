//Exporting this to be accessible in app.js
var bodyParser = require('body-parser');
var mongoose = require('mongoose');



//Connecting to the database!
mongoose.connect('mongodb://dkoenigs:HiBye123@ds127781.mlab.com:27781/dkoenigs_todo');
//Create a schema - like a blueprint for the database
var todoSchema = new mongoose.Schema({
  item: String, count: Number
});
var Todo = mongoose.model('Todo', todoSchema);
//Test item
// var itemOne = Todo({item: 'get a bike'}).save(function(err){
//   if (err) throw err;
//   console.log('item saved');
// })




//var data = [{item: 'get milk'},{item: 'walk dog'},{item: 'kick some footballs'}];
var urlencodedParser = bodyParser.urlencoded({extended: false});

module.exports = function(app){

  app.get('/todo', function(req, res){
    //Get data from mongodb and pass it to the view
    Todo.find({}, function(err, data){
      if (err) throw err;
      res.render('todo', {todos: data}); //Only renders 'data'
    });
  });

  app.post('/todo', urlencodedParser, function(req, res){
    //Get data from the view and add it to mongodb
    var newTodo = Todo(req.body).save(function(err, data){
      if (err) throw err;
      res.json(data);
    })
  });

  app.delete('/todo/:item', function(req, res){
    //Delete the requested item from mongodb
    //We find the desired item object by replacing any '-' with "" which will yield
    //the desired 'item', which we will then remove from the list...
    //Will try to get only the string following the 'count'...
    //Look for the string with '---' over it... convert that to '   ' but exclude
    //the beginning 4 chars to account for the counter variable... then assign to
    //property of item and match this object with one in the data base and delete


    Todo.find({item: (req.params.item.replace(/\-/g, " ")).substr(4)}).remove(function(err, data){
      if (err) throw err;
      res.json(data);
    });
  });

}
