function process_results(tab, event){
	$("#results").html("<p>Wait...!!</p")

	var aa = $("#filters :text");
	var bb = $("#filters > select");
	var variables = {};
	variables.tab_name = tab;
	for(i=0;i<aa.length;i++){
		if (aa[i].name == "zone" && aa[i].value != ""){ 
			variables.zn = aa[i].value;
		}
		if (aa[i].name == "street" && aa[i].value != ""){ 
			variables.sn = aa[i].value;
		}
		if (aa[i].name == "fill_percnt" && aa[i].value != ""){ 
			variables.fp = aa[i].value;
		}
	}
	for(j=0;j<bb.length;j++){
		if (bb[j].name == "health" && bb[j].value != ""){ 
			variables.ls = bb[j].value;
		}
		if (bb[j].name == "running" && bb[j].value != ""){ 
			variables.rs = bb[j].value;
		}		
		if (bb[j].name == "filled" && bb[j].value != ""){
			variables.fs = bb[j].value;
		}
	}
		
	$.ajax({
		type	: "GET",
		url		: "tab",
		data	: variables,
		success	: function(html){
			$("#results").html(html);
			return html;
		},
		error	: function(xhr){
			alert(xhr.status + " : " + xhr.statusText)
		},
	})
}