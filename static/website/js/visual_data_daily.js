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
		text: '分时数据曲线',
		x: -20 //center
        },
        subtitle: {
		text: '电压',
		x: -20
        },
        xAxis: {
		type: 'datetime',
		tickmarkPlacement: 'on',
		tickPixelInterval: 100,
		labels: {
			step:1,
			formatter: function(){
				return Highcharts.dateFormat("%H:%M:%S", this.value);
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
        },
        series: [
                    {
                        name: '电压',
                        data: []
                    }
                ]
};
$(function () {
	chart = new Highcharts.Chart(options);
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
                alert("getDataDaily");
		getDataDaily();
	} else {
		alert("时间不能为空");
	}
});

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
			chart.series[0].setData(data);
			
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


