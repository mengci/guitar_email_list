$(function() {
  $("#search-email-btn").click(function() {
    // todo
    // submit button click event. 
    // your ajax call should be here.
    // now it just print 123.
    //var name = $("#name").val();
    //var email = $("#email").val();
    var type = $("#type option:selected").val().toLowerCase();
    var country = $("#country").val().toLowerCase();
    var state = $("#state").val().toLowerCase();
    var city = $("#city").val().toLowerCase();

  	var data = {
  		"type":type,
  		"country":country,
  		"state":state,
  		"city":city,
  	};

    console.log(data);
  	$.ajax({
  		type: 'POST',
  		url: '/search',
  		data: data,
  		dataType:'json',
  		success: function(data){
  			console.log(data);
  			//$('#save-ack').html(data["name"] + " has been saved");
        var emailsArr = data["result"];
        var emailList = emailsArr.join();

        $('#search-result-ret').html(emailList);
        $('#search-result-ret').select();
  		},
  		error:function(){},
  	});
  		
  });
});


