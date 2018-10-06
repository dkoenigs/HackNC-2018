$(document).ready(function(){

  $('form').on('submit', function(){
      var item = $('form input');
      var todo = {item: item.val(), count: 0};
      $.ajax({
        type: 'POST',
        url: '/todo',
        data: todo,
        success: function(data){
          //do something with the data via front-end framework
          location.reload();
        }
      });
      return false;
  });

  $('ul').on('upVote', function(){
      // var item = $('form input');
      // var todo = {item: item.val(), count: };
      // $.ajax({
      //   type: 'POST',
      //   url: '/todo',
      //   data: todo,
      //   success: function(data){
      //     //do something with the data via front-end framework
      //     location.reload();
      //   }
      // });
      // return false;
      todos[0].count ++;
  });


  $('li').on('click', function(){
      // var item = $(this).text().replace(/ /g, "-");
      var item = $('form input');
      var todo = {item: "Hi", count: 66};
      $.ajax({
        type: 'POST',
        url: '/todo',
        data: todo,
        success: function(data){
          //do something with the data via front-end framework
          location.reload();
        }
      });
      return false;
  });

  // $('li').on('click', function(){
  //   var item = $(this).text().replace(/ /g, "-");
  //   $.ajax({
  //     type: 'DELETE',
  //     url: '/todo/' + item,
  //     success: function(data){
  //       //do something with the data via front-end framework
  //       location.reload();
  //     }
  //   });
});

});
