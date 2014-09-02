$('.date_picker').datepicker($.datepicker.regional[ "zh-TW" ]);
var chart;
Highcharts.setOptions({                                                     
        global: {                                                               
                useUTC: false                                                       
        }                                                              
});
options = {
	chart: {
		type: 'line',
		renderTo: 'visual_view',
		alignTicks: true,
		zoomType: 'x'
	},
        title: {
		text: '分日数据曲线',
		x: -20 //center
        },
//        subtitle: {
//		text: '电压',
//		x: -20
//        },
        xAxis: {
		type: 'datetime',
		//tickmarkPlacement: 'on',
		tickPixelInterval: 100,
		//tickPixelInterval: 300,
		labels: {
			//step:1,
			formatter: function(){
				return Highcharts.dateFormat("%m-%d", this.value);
			}
		},
		gridLineWidth: 1
        },
        yAxis: {
		title: {
			text: '电压 (V)'
		},
		plotLines: [{
			value: 0,
			width: 1,
			color: '#808080'
		}],
        },
        tooltip: {
		valueSuffix: 'V'
        },
        legend: {
		layout: 'vertical',
		align: 'right',
		verticalAlign: 'middle',
		borderWidth: 0
        }//,
        //series: [
        //            {
        //                name: '数据类型',
        //                data: []
        //            }
        //        ]
};
$(function () {
	//chart = new Highcharts.Chart(options);
        $.ajax({
		url: "/get_node_id_list",
		type: "post",
		data: {	k:'v' },
		success:function(data){
			//data=[{'value':21, 'text':21},{'value':25, 'text':25},{'value':29, 'text':29}];
			//alert(data);
			for (var i = 0; i < data.length; i++) {
				var item = new Option(data[i].value, data[i].text);
				$('#node_list').append(item);
			}
			$.ajax({
				url:"/get_node_desc",
				type: 'post',
				data: {node_id: $('#node_list').val()},
				success:function(data1){
					$('#node_desc').text("在" + data1 + "附近");
				}
			});
		}
	});
});

$('#search').click(function(){
	if(isValidDate($('#start_date').val()) && isValidDate($('#end_date').val()))
	{
                //alert("getDataDaily");
		getDataDaily();
	} else {
		alert("时间不能为空");
	}
});

name_map = {
	"max_voltage": "最大电压",
	"min_voltage": "最小电压",
	"avg_voltage": "平均电压",
	"mse_voltage": "电压均方差",
	"voltage_failure_times": "失效次数",
	"voltage_exception_times": "异常次数",
	"voltage_exception_period": "异常时间"
}

function getDataDaily() {
        var start_date = $('#start_date').val();
        var end_date = $('#end_date').val();
	var data_type = $('#data_status').val();
	var node_id = $('#node_list').val();
        $.ajax({
		url:"/get_data_daily",
		type: 'post',
		data: {
                        start_date: start_date,
                        end_date: end_date,
                        data_type: data_type,
                        node_id: node_id
                },
		dataType: "json",
		success: function(data){
			//chart.series[0].name = "hhh";
			//alert(chart.series[0].name);
			//chart.series[0].setData(data);
			var s = {
				name: name_map[data_type],
				data: data
			};
			var sub_title = {
				text: name_map[data_type],
				x: -20
			};
			//chart.series[0] = s;
			//chart.redraw();
			//options['subtitle'] = sub_title;
			options.subtitle = sub_title;
			var yAxis_title = {
				text: name_map[data_type]
			};
			options.yAxis.title = yAxis_title;
			chart = new Highcharts.Chart(options);
			chart.addSeries(s);
			
		}
	});
}

$('#node_location').click(function(){
	var node_id = $('#node_list').val();
	if (node_id != null) {
		var node_id = $('#node_list').val();
		window.location.href = '/node_all_location?type=node&node_id=' + node_id;
	} else {
		alert('节点不能为空');
	}
});

$('#node_list').change(function(){
	$.ajax({
		url: "/get_node_desc",
		type: 'post',
		data: {node_id: $('#node_list').val()},
		success: function(data){
			$('#node_desc').text("在" + data + "附近");
		}
	});
});


