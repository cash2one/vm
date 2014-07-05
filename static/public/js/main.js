function bindMenuHref() {
	$('#query_data_daily').bind('click', function(){
		window.location = $(this).attr('href');
	});	
	$('#query_data_hourly').bind('click', function(){
		window.location = $(this).attr('href');
	});
	$('#visual_data_daily').bind('click', function(){
		window.location = $(this).attr('href');
	});
	$('#visual_data_hourly').bind('click', function(){
		window.location = $(this).attr('href');
	});
	$('#node_all').bind('click', function(){
		window.location = $(this).attr('href');
	});
	$('#node_manage').bind('click', function(){
		window.location = $(this).attr('href');
	});
}

$(document).ready(function () {
	kendo.bind(document.body);
	bindMenuHref();
});