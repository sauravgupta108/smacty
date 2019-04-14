var setup = new function(){
	this.apply_active = function(name){
		var i =0;
		navs = $("div#nav_bar ul li");
		
		for (i;i<navs.length;i++){
			$("#"+navs[i].id).removeClass("active");

			if (navs[i].id === name){
				$("#"+navs[i].id).addClass("active");
			}			
		}
	}
}
	
