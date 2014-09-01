function table_node_search() {
	var node_id = $('#node_list').val();
	$.ajax({
		url:"/get_node_info",
		type: 'post',
		data: {node_id: node_id},
		success:function(info){
			sContent =  
				"<tr>" +
				"<td>" + info.node_id + "</td>" +  
				"<td>" + info.alias + "</td>" +  
				"<td>" + info.desc + "</td>" + 
				"<td>" + info.company_name + "</td>" + 
				"<td>" + info.net_name + "</td>" +  
				"<td>" + info.max_voltage + "</td>" + 
				"<td>" + info.min_voltage + "</td>" + 
				"<td>" + info.max_current + "</td>" + 
				"<td>" + info.min_current + "</td>" + 
				"<td>" + info.latitude + "</td>" + 
				"<td>" + info.longitude + "</td>" + 
				"<td>" + info.sim_id + "</td>" + 
				"<td>" + info.expire_time + "</td>" + 
				"<td>" + info.create_time + "</td>" + 
				"</tr>";
			$('#mytable tbody').html(sContent);
		}
	});
}

function table_net_search() {
	var net_name = $('#net_list').val();
	$.ajax({
		url:"/get_nodes_info",
		type: 'post',
		data: {net_name: net_name},
		success: function(data){
			var sContent = "";
			$.each(data,function(n,info) {
				sContent += 
					"<tr>" +
					"<td>" + info.node_id + "</td>" +  
					"<td>" + info.alias + "</td>" +  
					"<td>" + info.desc + "</td>" + 
					"<td>" + info.company_name + "</td>" + 
					"<td>" + info.net_name + "</td>" +  
					"<td>" + info.max_voltage + "</td>" + 
					"<td>" + info.min_voltage + "</td>" + 
					"<td>" + info.max_current + "</td>" + 
					"<td>" + info.min_current + "</td>" + 
					"<td>" + info.latitude + "</td>" + 
					"<td>" + info.longitude + "</td>" + 
					"<td>" + info.sim_id + "</td>" + 
					"<td>" + info.expire_time + "</td>" + 
					"<td>" + info.create_time + "</td>" + 
					"</tr>";
			});
			$('#mytable tbody').html(sContent);
		}
	});
}

function map_node_search() {
	var node_id = $('#node_list').val();
	$.ajax({
		url:"/get_node_info",
		type: 'post',
		data: {node_id: node_id},
		success:function(info){
                    //alert(info.company_name);
                    sContent = "<table border='1'>" + 
                                "<tr>" +
                                "	<th colspan='4'>" + info.company_name + "</th>" + 
                                "</tr>" + 
                                "<tr>" + 
                                "	<td>节点网</td>" + 
                                "	<td colspan='3'>" + info.net_name + "</td>" + 
                                "</tr>" + 
                                "<tr>" + 
                                "	<td>节点</td><td>" + info.node_id + "</td>" + 
                                "	<td>别名</td><td>" + info.alias + "</td>" + 
                                "</tr>" + 
                                "<tr>" +
                                "	<td>描述</td>" +
                                "	<td colspan='3'>" + info.desc + "</td>" + 
                                "</tr>" + 
                                "<tr>" + 
                                "	<td>电压上限</td><td>" + info.max_voltage + "</td>" + 
                                "	<td>电压下限</td><td>" + info.min_voltage + "</td>" + 
                                "</tr>" + 
                                "<tr>" + 
                                "	<td>电流上限</td><td>" + info.max_current + "</td>" + 
                                "	<td>电流下限</td><td>" + info.min_current + "</td>" + 
                                "</tr>" + 
                                "<tr>" + 
                                "	<td>纬度</td><td>" + info.latitude + "</td>" + 
                                "	<td>经度</td><td>" + info.longitude + "</td>" + 
                                "</tr>" + 
                                "<tr>" +
                                "	<td>SIM卡号</td>" + 
                                "	<td colspan='3'>" + info.sim_id + "</td>" + 
                                "</tr>" + 
                                "<tr>" + 
                                "	<td>有效期</td>" + 
                                "	<td colspan='3'>" + info.expire_time + "</td>" + 
                                "</tr>" + 
                                "<tr>" + 
                                "	<td>创建日期</td>" + 
                                "	<td colspan='3'>" + info.create_time + "</td>" + 
                                "</tr>" + 
                                "</table>";
                        var map = new BMap.Map("dituContent");
                        var infoWindow = new BMap.InfoWindow(sContent);
                        var point = new BMap.Point(info.latitude, info.longitude);    // 创建点坐标
                        var points = [point];
                        var marker = new BMap.Marker(point);
                        map.centerAndZoom(point,7);// 初始化地图,设置中心点坐标和地图级别。
                        map.addOverlay(marker);
                        map.enableScrollWheelZoom();                           //启用滚轮放大缩小
                        map.setViewport(points);
                        marker.addEventListener("click", function(){          
                                this.openInfoWindow(infoWindow);
                                //图片加载完毕重绘infowindow
                                document.getElementById('imgDemo').onload = function (){
                                       infoWindow.redraw();   //防止在网速较慢，图片未加载时，生成的信息框高度比图片的总高度小，导致图片部分被隐藏
                                }
                        });
		}
	});
}

function map_net_search() {
	var net_name = $('#net_list').val();
			$.ajax({
			    url:"/get_nodes_info",
			    type: 'post',
			    data: {net_name: net_name},
			    success: function(data){
				//alert(data[0].name);
				//alert(data[1].name);
				var map = new BMap.Map("dituContent");
				var points = []
				//alert(data[0].company_name);
				//for (var i in data) {
				$.each(data,function(n,info) {  
				    //alert(info["company_name"]);
				    var sContent = "<table border='1'>" + 
					"<tr>" +
					"	<th colspan='4'>" + info.company_name + "</th>" + 
					"</tr>" + 
					"<tr>" + 
					"	<td>节点网</td>" + 
					"	<td colspan='3'>" + info.net_name + "</td>" + 
					"</tr>" + 
					"<tr>" + 
					"	<td>节点</td><td>" + info.node_id + "</td>" + 
					"	<td>别名</td><td>" + info.alias + "</td>" + 
					"</tr>" + 
					"<tr>" +
					"	<td>描述</td>" +
					"	<td colspan='3'>" + info.desc + "</td>" + 
					"</tr>" + 
					"<tr>" + 
					"	<td>电压上限</td><td>" + info.max_voltage + "</td>" + 
					"	<td>电压下限</td><td>" + info.min_voltage + "</td>" + 
					"</tr>" + 
					"<tr>" + 
					"	<td>电流上限</td><td>" + info.max_current + "</td>" + 
					"	<td>电流下限</td><td>" + info.min_current + "</td>" + 
					"</tr>" + 
					"<tr>" + 
					"	<td>纬度</td><td>" + info.latitude + "</td>" + 
					"	<td>经度</td><td>" + info.longitude + "</td>" + 
					"</tr>" + 
					"<tr>" +
					"	<td>SIM卡号</td>" + 
					"	<td colspan='3'>" + info.sim_id + "</td>" + 
					"</tr>" + 
					"<tr>" + 
					"	<td>有效期</td>" + 
					"	<td colspan='3'>" + info.expire_time + "</td>" + 
					"</tr>" + 
					"<tr>" + 
					"	<td>创建日期</td>" + 
					"	<td colspan='3'>" + info.create_time + "</td>" + 
					"</tr>" + 
					"</table>";
					//alert(sContent);
					var infoWindow = new BMap.InfoWindow(sContent);
					var point = new BMap.Point(info.latitude, info.longitude);    // 创建点坐标
					var marker = new BMap.Marker(point);
					map.addOverlay(marker);
					marker.addEventListener("click", function(){          
					   this.openInfoWindow(infoWindow);
					   //图片加载完毕重绘infowindow
					   document.getElementById('imgDemo').onload = function (){
					       infoWindow.redraw();   //防止在网速较慢，图片未加载时，生成的信息框高度比图片的总高度小，导致图片部分被隐藏
					   }
					});
					points.push(point);
				});
				map.enableScrollWheelZoom();
				map.setViewport(points);
			    }
			});
}

$(function(){
	var type = $('#node_range_list').val();
	if (type == '1') {
		$('#net_list').attr('disabled', true);
		$('#node_list').attr('disabled', false);
	}
	if (type == '2') {
		$('#net_list').attr('disabled', false);
		$('#node_list').attr('disabled', true);
	}
	map_node_search();
});

$('#data_status').change(function(){
	var view_type = $('#data_status').val();
	if (view_type == '1') {
		$('#content_div').html(
			"<div class=\"panel-heading\">全景视图</div>" +
			"<div class=\"panel-body\">" + 
			"<div id=\"dituContent\" style=\"min-width:700px;height:400px;overflow: visible\"></div>" + 
			"</div>"
		);
		var type = $('#node_range_list').val();
		if (type == '1') {//节点
			map_node_search();
		} else if (type == '2') {
			map_net_search();
		}
		
	} else if (view_type == '2') {
		//code
		$('#content_div').html(
			"<div class=\"panel-heading\">节点信息列表</div>" + 
			"<table id=\"mytable\" class=\"table table-striped table-bordered\" cellspacing=\"0\">" + 
			"<thead>" + 
			"<tr>" + 
			"<th>节点</th>" + 
			"<th>别名</th>" + 
			"<th>描述</th>" +
			"<th>单位</th>" +
			"<th>节点网</th>" + 
			"<th>电压上限</th>" + 
			"<th>电压下限</th>" +
			"<th>电流上限</th>" +
			"<th>电流下限</th>" +
			"<th>纬度</th>" +
			"<th>经度</th>" +
			"<th>SIM卡号</th>" +
			"<th>有效期</th>" +
			"<th>创建时间</th>" +
			"</tr>" + 
			"</thead>" +
			"<tbody>" + 
			"</tbody>" +
			"</table>"
		);
		var type = $('#node_range_list').val();
		if (type == '1') {
			//code
			table_node_search();
		} else if (type == '2') {
			//code
			table_net_search();
		}
	}
});

$('#node_range_list').change(function(){
	var type = $('#node_range_list').val();
	if (type == '1') {
		$('#net_list').attr('disabled', true);
		$('#node_list').attr('disabled', false);
	}
	if (type == '2') {
		$('#net_list').attr('disabled', false);
		$('#node_list').attr('disabled', true);
	}
});

$('#search').click(function(){
	var type = $('#node_range_list').val();
	var view_type = $('#data_status').val(); 
	if (type == '1') { //节点
                //alert('节点');
		if (view_type == '1') {
			map_node_search();
		} else if (view_type == '2') {
			table_node_search();
		}
	} else if(type == '2'){//节点网
		if (view_type == '1') {
			map_net_search();
		} else if (view_type == '2') {
			table_net_search();
		}
	} else {
            alert('error');
        }
});