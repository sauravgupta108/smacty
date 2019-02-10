var light = new function(){
	this.lights = function(){
		$("div#entity_content").html("<p>Loading...</p>")		
		$.ajax({
			url : "lights",
			success : function(data){
				$("div#entity_content").html(data);				
			},
			error : function(){
				alert("Error........")
			},
		});
	};

	this.light_filters = function(){
		var ll_filters = {}; var flg = 0;		
		
		if($("#lt_street_number").val() != ""){
			var street = Number($("#lt_street_number").val())
			if(!street || (street <= 0)){
				$("#lt_street_number").val("")
				alert("Street Number must be a Positive Integer");			
			}
			else{ ll_filters.street_number = street; }
		}
		
		var lt_health_status = $("#lt_health_status").val()
		if(lt_health_status != -1){ ll_filters.health_status = lt_health_status; }
		else{ ll_filters.health_status = -1 }
		
		var lt_running_status = $("#lt_running_status").val()
		if(lt_running_status != -1){ ll_filters.running_status = lt_running_status; }
		else{ ll_filters.running_status = -1 }
		
		var lt_zone = $("#lt_zone").val()
		if(lt_zone != ""){ ll_filters.zone = lt_zone }
		
		$.ajax({
			url : "lights",
			data: ll_filters,
			success : function(data){
				$("div#entity_content").html(data);

				// Set status to previous as before 
				if(ll_filters.street_number){ $("#lt_street_number").val(ll_filters.street_number); }
				$("#lt_health_status").val(ll_filters.health_status);
				$("#lt_running_status").val(ll_filters.running_status);
				$("#lt_zone").val(ll_filters.zone)
			},
			error : function(){
				alert("Error........")
			},
		});
	};
};

var dustbin = new function(){
	this.dustbins = function(){
		$("div#entity_content").html("<p>Dustbins</p>")
	};
};

var water_tank = new function(){
	this.tanks = function(){
		$("div#entity_content").html("<p>Water Tanks</p>")
	};
};