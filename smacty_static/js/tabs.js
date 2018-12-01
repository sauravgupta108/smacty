function content_for_tab(tab_name, event){
	var a = '#'+tab_name;
	var tabs = $("#tabs")[0].children

	for (var i = 0; i < tabs.length;i++){
		if ((tabs[i].id) == tab_name){
			$("#"+tabs[i].id).addClass("active_tab");
		}
		else{
			$("#"+tabs[i].id).removeClass();
			$("#"+tabs[i].id).addClass("inactive_tab");
		}
	}
	tab_content = get_tab_content(tab_name)
}

function get_tab_content(tab_name){
	$.ajax({
		url		: "<>",
		type	: "GET",
		data	: {tab: tab_name},
		success	: function(html){
		},
		error	: function(xhr,errmsg,err){
			alert(err)
		},

	})
}

$(document).ready(function() {
	
})