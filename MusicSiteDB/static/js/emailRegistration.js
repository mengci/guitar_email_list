$(function() {
  $("#save-email-btn").click(function() {
    // todo
    // submit button click event. 
    // your ajax call should be here.
    // now it just print 123.
    var name = $("#name").val();
    var email = $("#email").val();
    var source = $("#source").val();
    var country = $("#country").val();
    var state = $("#state").val();
    var city = $("#city").val();

  	var data = {
  		"name":name,
  		"email":email,
  		"source":source,
  		"country":country,
  		"state":state,
  		"city":city,
  	};
  	$.ajax({
  		type: 'POST',
  		url: '/save',
  		data: data,
  		dataType:'json',
  		success: function(data){
  			console.log(data);
  			$('#name').val("");
  			$('#email').val("");
  			$('#source').val("");
  			$('#country').val("");
  			$('#state').val("");
  			$('#city').val("");	
  			$('#save-ack').html(data["name"] + " has been saved");
  		},
  		error:function(){},
  	});
  		
  });
});


