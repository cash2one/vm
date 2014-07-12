$(function(){
    $('.date_picker').datepicker($.datepicker.regional[ "zh-TW" ]);
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
});