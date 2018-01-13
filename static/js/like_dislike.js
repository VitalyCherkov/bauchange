// Получение переменной cookie по имени
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Настройка AJAX
$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

function like() {
    var like = $(this);
    var url = like.data('url');
    var pk = like.data('id');
    var dislike = like.next();
    console.log(url.url);

    $.ajax({
        url: url,
        type: 'POST',
        data: {'obj': pk},
        success: function (json) {
            dislike.find('[data-count="dislike"]').text(json.dislikes_count);
            like.find('[data-count="like"]').text(json.likes_count);
        }

    });

    return false;
}

function dislike() {
    var dislike = $(this);
    var url = dislike.data('url');
    var pk = dislike.data('id')
    var like = dislike.prev();
    console.log(url.url);


    $.ajax({
        url: url,
        type: 'POST',
        data: {'obj': pk},
        success: function (json) {
            dislike.find('[data-count="dislike"]').text(json.dislikes_count);
            like.find('[data-count="like"]').text(json.likes_count);
        }

    });

    return false;
}

$(function() {
    $('[data-action="like"]').click(like);
    $('[data-action="dislike"]').click(dislike);
});
