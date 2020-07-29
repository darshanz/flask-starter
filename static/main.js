$(document).ready(function(){
    $("#hello").click(function(){
      $("#response").html("...")
      $.get("/hello", function(data, status){
        $("#response").html(data)
    });
    });
    
  }); 