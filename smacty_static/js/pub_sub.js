function publish(event){	
	event.preventDefault();
	var topic = $("#topic").val();
	var message = $("#message").val();
	$("#message").val("");
	var token = $("#pub-form").find('input[name=csrfmiddlewaretoken]').val();
	
	$.ajax({
		url  : "publish",
		type : "POST",
		data : {topic: topic, message: message, csrfmiddlewaretoken: token},
		success: function(json){
			$("#test").text(json.result);
		},
		error: function(xhr,errmsg,err){
			alert(err);
		}
	});
}

function subscribe(event){
	event.preventDefault();
	if (!($("#initiate").prop("disabled"))){
		$("#initiate").prop("disabled", true)

		$("#sub-tpc").prop("disabled", false); $('#start_sub').prop("disabled", false);

		$("#sub-result").text("");
	}

	else{
		$("#sub-result").text("Please wait....");
		var topic = $("#sub-tpc").val();
		ajax_subscribe(topic);
	}	
	
	$('#start_sub').click(function(){
		$("#sub-tpc").prop("disabled", true);
		$('#start_sub').val("wait.."); $('#start_sub').prop("disabled", true);
	})	
}

function ajax_subscribe(topic){	
	var token = $("#sub-form").find('input[name=csrfmiddlewaretoken]').val();
	
	$.ajax({
		url		: "subscribe",
		type	: "POST",
		data	: {topic : topic, csrfmiddlewaretoken: token},
		success	: function(json){
			$("#sub-result").text(json["result"]);			
		},		
		error	: function(xhr,errmsg,err){
			alert("Sub: " + err);
			$("#sub-result").text("");		
		}
	}).always(function(){		
			$("#sub-tpc").prop("disabled", false);
			$('#start_sub').val("Get Messages"); $('#start_sub').prop("disabled", false)
		});
}
	

$(document).ready(function() {
	$("#start_sub").prop("disabled", true);$("#sub-tpc").prop("disabled", true);

	$('#pub-form').on('submit', publish);
	$('#sub-form').on('submit', subscribe)
});