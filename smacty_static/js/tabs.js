function content_for_tab(tab_name, event){
	var tabs = $("#tabs")[0].children

	$("#tab_content").html("<p>Please Wait...!!!</p>")

	for (var i = 0; i < tabs.length;i++){
		if ((tabs[i].id) == tab_name){
			$("#"+tabs[i].id).addClass("active_tab");
		}
		else{
			$("#"+tabs[i].id).removeClass();
			$("#"+tabs[i].id).addClass("inactive_tab");
		}
	}
	tab_content = get_tab_content(tab_name);
}

function get_tab_content(tab_name){	
	$.ajax({
		type	: "GET",
		url		: "tab",
		data	: {tab_name: tab_name},
		success	: function(html){
			$("#tab_content").html(html);
			return html;
		},
		error	: function(xhr){
			alert(xhr.status + " : " + xhr.statusText)
		},
	})
}

$(document).ready(function() {
	
})