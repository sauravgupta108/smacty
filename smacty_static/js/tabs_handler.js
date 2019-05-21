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
				alert("Error.....123...")
			},
		});
	};
	/*{light_id: "SL001", street_number: 1, health: 1, running_status: "True", zone: "zone001"}*/
	this.show_modal = function(light_detail_str){
		 var json_string = light_detail_str.replace(/True/g, "'True'");
		 json_string = json_string.replace(/False/g, "'False'");
		 
		 var light = JSON.parse(json_string.replace(/'/g, '"'))
		 
		 $("div#light_id").text(light['light_id']);
		 $("div#light_location").text("Location: " + light['street_number'] + "," + light['zone']);

		 if (light["running_status"] === "True"){
		 	$("input#light_on").prop("checked", true); $("input#light_off").prop("checked", false);
		 }

		 else if (light["running_status"] === "False"){
		 	$("input#light_on").prop("checked", false); $("input#light_off").prop("checked", true);
		 }

		 else{
		 	$("input#light_on").hide(); $("input#light_off").hide();
		 }
		 
		 if(light["health"] === 1){
		 	$("div#light_health_bad").hide(); $("div#light_health_ok").show();
		 }

		 else {
		 	$("div#light_health_bad").show(); $("div#light_health_ok").hide();
		 }

		 $("div#light_details").modal({});
	}

	this.light_switch = function(switch_position){
		console.log(switch_position);
	}
};

var dustbin = new function(){
	this.dustbins = function(){
		$("div#entity_content").html("<p>Loading...</p>")		
		$.ajax({
			url : "dustbins",
			success : function(data){
				$("div#entity_content").html(data);				
			},
			error : function(){
				alert("Error........")
			},
		});
	};

	this.dustbin_filters = function(){
		console.log("Dustbin filters")
	};
};

var water_tank = new function(){
	this.tanks = function(){
		$("div#entity_content").html("<p>Loading...</p>")		
		$.ajax({
			url : "tanks",
			success : function(data){
				$("div#entity_content").html(data);				
			},
			error : function(){
				alert("Error........")
			},
		});
	};
	this.water_tank_filters = function(){
		console.log("Water Tank filters")
	};
};
