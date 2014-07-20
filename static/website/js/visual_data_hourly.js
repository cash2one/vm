//左侧Javascript代码
$('.date_picker').datepicker($.datepicker.regional[ "zh-TW" ]);
	var chart;
	Highcharts.setOptions({                                                     
            global: {                                                               
                useUTC: false                                                       
            }                                                                       
        }); 
	$(function () {
    //$('#container').highcharts({
	chart = new Highcharts.Chart({
		chart: {
			type: 'line',
			renderTo: 'visual_view',
			alignTicks: true,
			zoomType: 'x'
			//type: 'logarithmic'
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
            //categories: ['Jan123456789', 'Feb123456789', 'Mar123456789', 'Apr123456789', 'May123456789', 'Jun123456789','Jul123456789', 'Aug123456789', 'Sep123456789', 'Oct123456789', 'Nov123456789', 'Dec123456789'],
			//tickPositions: [0,1,2,3,4,5,8],
			type: 'datetime',
			tickmarkPlacement: 'on',
			tickPixelInterval: 100,
			//tickInterval: 2,
			labels: {
				step:1,
				formatter: function(){
					return Highcharts.dateFormat("%M:%S", (new Date()).getTime());
				}
			//staggerLines: 2
			},
			gridLineWidth: 1
        },
		/*xAxis: {  
                            // X轴分类  
                            categories: ['苹果', '桔子', '梨子', '香蕉', '李子'],  
                            // 坐标轴的标签  
                            labels:{  
                                // 标签位置  
                                align: 'center',  
                                // 标签格式化  
                                formatter: function(){  
                                    return this.value;  
                                },  
                                // 标签旋转度数  
                                rotation: 20,  
                                // 标签交错显示的行数  
                                staggerLines: 1  
                            },  
                            // X轴的步进值，决定隔多少个显示一个  
                            tickInterval: 1,  
                            // 坐标轴标题  
                            title: {  
                                text: '水果分类'  
                            }  
                        },  */
        yAxis: {
            title: {
                text: '电压 (V)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }],
			//max:100
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
        series: [{
            name: '电压',
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
        }/*, {
            name: 'New York',
            data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
        }, {
            name: 'Berlin',
            data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
        }, {
            name: 'London',
            data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
        }*/]
    });
});
function add()
{
	//chart.series[0].addPoint([20,50], true, true);
	//alert(chart.yAxis[0].min);
	var min = chart.yAxis[0].min - 50;
	var max = chart.yAxis[0].max + 50;
	//chart.yAxis[0].min = chart.yAxis[0].min * 2;
	//chart.yAxis[0].max = chart.yAxis[0].max * 2;
	//chart.yAxis[0].update();
	chart.yAxis[0].setExtremes(min, max);
	//chart.redraw();
}	
function change()
{
	chart.series[0].setData([[1,10],[2,5],[3,8]]);
}

$('#search').click(function(){
	//alert("search");
	getDataHourly();
	});

$('#download').click(function(){
	alert("download");});

function getDataHourly(){
	$.ajax({
		url:"/get_data_hourly",
		dataType:"json",
		success:function(data){
			//alert(data);
			chart.series[0].setData(data);
		}
		});
}