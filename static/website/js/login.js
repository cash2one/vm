function login_init() {
    $('#login_btn').click(function(){
        var user_name = $('#username').val().trim();
        var password = $('#password').val().trim();
        var checkcode = $('#checkcode').val().trim();
        if (user_name == '' || password == '' || checkcode == '') {
            return;
        } else {
            $.ajax({
                url: '/login/',
                type: 'POST',
                async: false,//同步
                cache: false,
                timeout: 2000,
                data: {'username':user_name, 'password':password, 'checkcode':checkcode},
                dataType: "json",
                success: function(data){
                    if (data.errno == 0){
                        //alert("登陆成功!");
                        window.location.href="/query_data_daily";
                    } else {
                        if (data.errno == 3) {
                            alert("用户名或密码不能为空!");
                        } else if (data.errno == -4) {
                            alert("该账户已被禁用，请联系管理员");
                        } else if (data.errno == 1) {
                            alert("用户名不存在");
                        } else if (data.errno == 2) {
                            alert("密码错误");
                        } else if (data.errno == 5) {
                            //code
                            alert("验证码不能为空");
                        } else if (data.errno == 6) {
                            //code
                            alert("验证码错误");
                        }
                    }
                }
            });
        }
    });
}

$(function() {
    login_init();
});