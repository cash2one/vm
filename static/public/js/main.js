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
	$('#admin').bind('click', function(){
		window.location = $(this).attr('href');
	});
	$('#node_manage').bind('click', function(){
		window.location = $(this).attr('href');
	});
}

function logout_init() {
	$('#logout').click(function() {
		$.ajax({
                url: '/logout/',
                type: 'POST',
                async: false,//Í¬²½
                cache: false,
                timeout: 2000,
                //data: {'username':user_name, 'password':password},
                //dataType: "json",
                success: function(data){
			window.location.href="/login_page";
                }
            });
	});
}

$(document).ready(function () {
	kendo.bind(document.body);
	bindMenuHref();
	logout_init();
});