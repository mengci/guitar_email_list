$(function() {
  $("#search-email-btn").click(function() {
    // todo
    // submit button click event. 
    // your ajax call should be here.
    // now it just print 123.
    //var name = $("#name").val();
    //var email = $("#email").val();
    var type = $("#type").val();
    var country = $("#country").val();
    var state = $("#state").val();
    var city = $("#city").val();

  	var data = {
  		"type":type,
  		"country":country,
  		"state":state,
  		"city":city,
  	};
    // var result = {
    //   "name":name,
    //   "email":email,
    //   "type":type,
    //   "country":country,
    //   "state":state,
    //   "city":city,
    // };
  	$.ajax({
  		type: 'POST',
  		url: '/save',
  		data: data,
  		dataType:'json',
  		success: function(data){
  			console.log(data);
  			$('#type').val("");
  			$('#country').val("");
  			$('#state').val("");
  			$('#city').val("");	
  			//$('#save-ack').html(data["name"] + " has been saved");
        $('#save-ack').html(data["result"]);
  		},
  		error:function(){},
  	});
  		
  });
});


