$(document).ready(function(){
    $('#btn-sim').click(function(){
        var url = $(this).data('url');
        window.location.href = url;
    });
});