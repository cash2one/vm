function datepicker_init() {
    $('.date_picker').datepicker($.datepicker.regional[ "zh-TW" ]);
}

function dataTable_init() {
    var mytable = $('#mytable').dataTable({
        "language": {
            "lengthMenu": "每页显示 _MENU_ 条记录",
            "zeroRecords": "没有任何数据",
            "info": "当前页面 _PAGE_ 页面数 _PAGES_",
            "infoEmpty": "没有任何数据",
            "infoFiltered": "(filtered from _MAX_ total records)",
            "search": "搜索"
        },
        "fnRowCallback": function(nRow, aData, iDisplayIndex, iDisplayIndexFull) {
            var $nRow = $(nRow);
            if (aData[8] > 0 || aData[9] > 0) {
                $nRow.css({"color": "red"});
            }
            return nRow;
        }
    });
    return mytable;
}

function select_init() {
    $('#monitor_type').change(function() {
        var mt = $(this).val();
        /* 恒电位仪*/
        if (mt == 'h') {
            // step 1. 在查询类型中加入"电位"
            $('#search_type').append('<option value="potential">电位</option>');
            // step 2. 把"数据状态"禁止掉
            
        /* 采集器 */    
        } else if (mt == 'c') {
            // step 1. 在查询类型中删除"电位"
            $('#search_type option[value="potential"]').remove();
        }
        //alert($(this).find('option:selected').text());
    });
}

function query_init(mytable) {
    $('#search_btn').bind('click', function(){
        /* step 1. 检查输入 */
        var start_date = $('#start_date').val();
        var end_date = $('#end_date').val();
        if (!isValidDate(start_date) || !isValidDate(end_date)) {
            alert('日期输入有误, 请检查！');
            return;
        }
        if (start_date > end_date) {
            alert('开始日期必须不超过结束日期');
            return;
        }
        start_date = start_date.replace(/\//g, '-');
        end_date = end_date.replace(/\//g, '-');
        /* step 2. 获得表单值 */
        var monitor_type = $('#monitor_type').val(); // m or c
        var search_type = $('#search_type').val(); // voltage, current or potential
        var data_status = $('#data_status').val(); // all, normal, except
        var node = $('#node_list').val(); 
        sent_data = {
            'monitor_type': monitor_type,
            'search_type': search_type,
            'data_status': data_status,
            'node_list': node,
            'start_date': start_date,
            'end_date': end_date
        };
        $.ajax({
            url: '/query_data_daily_search',
            type: "POST",
            async: false,
            cache: false,
            timeout: 2000,
            data: sent_data,
            dataType: "json",
            success: function(res){
                mytable.fnClearTable();
                if (res.error == 1 || res.result.length == 0) {
                    alert('这段时间没有数据!');
                } else {
                    //temp
                    infos = [];
                    for (var i = 0; i < res.result.length; i++) {
                        var info = [];
                        for (var j = 0; j < res.result[i].length; j++) {
                            info.push(res.result[i][j]);
                            if (j == 1) {
                                info.push(5000);
                                if (search_type == 'voltage') {
                                    info.push('电压');   
                                } else if (search_type == 'current') {
                                    info.push('电流');
                                } else {
                                    info.push('电位');
                                }
                            }
                        }
                        infos.push(info);
                    } // temp
                    console.log(infos);
                    mytable.fnAddData(infos);
                }
            }
        });
    });
}

$(function(){
    datepicker_init();
    var mytable = dataTable_init();
    select_init();
    query_init(mytable);
});