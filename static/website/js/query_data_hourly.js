function datepicker_init() {
    $('.date_picker').datepicker($.datepicker.regional[ "zh-TW" ]);
}

function dataTable_init() {
    $('#mytable').dataTable({
        "language": {
            "lengthMenu": "每页显示 _MENU_ 条记录",
            "zeroRecords": "没有任何数据",
            "info": "当前页面 _PAGE_ 页面数 _PAGES_",
            "infoEmpty": "没有任何数据",
            "infoFiltered": "(filtered from _MAX_ total records)",
            "search": "搜索"
        }
    });
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

function query_init() {
    $('#search_btn').bind('click', function(){
        /* step 1. 检查输入 */
        var query_date = $('#query_date').val();
        alert(query_date);
        if (! isValidDate(query_date)) {
            alert('日期输入有误, 请检查！');
            return;
        }
        /* step 2. 获得表单值 */
        var monitor_type = $('#monitor_type').val();
        var search_type = $('#search_type').val();
        var node = $('#node_list').val();
        alert(query_date);
        alert(monitor_type);
        alert(search_type);
        alert(data_status);
        alert(node);
    });
}


$(function(){
    datepicker_init();
    dataTable_init();
    select_init();
    query_init();
});