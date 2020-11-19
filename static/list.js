// ウィンドウのスクロール位置を記憶
$(window).scroll(function() {
    $('#scroll-amount').text($(this).scrollTop() + 'px');
    localStorage.setItem('scroll', $(this).scrollTop())
});

// ウィンドウをロードしたときに記憶したスクロール位置へ移動
$(window).ready(function() {
    $(window).scrollTo(localStorage.getItem('scroll'));
});

$('.like').click(function(){
    var id;
    id = $(this).attr("data_id");
    $.ajax(
        {
            type:"GET",
            url: "like",
            data:{
                star: id
                }
        })
    });