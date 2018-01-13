function vote() {
    var vote = $(this);
    var url = vote.data('url');
    var pk = vote.data('id')
    console.log(url.url);


    $.ajax({
        url: url,
        type: 'POST',
        data: pk,
        success: function (json) {
            $('[data-count="dislike"]').text(json.dislikes_count);
            $('[data-count="like"]').text(json.likes_count);
        }

    });

    return false;
}

$(function() {
    $('[data-action="like"]').click(vote);
    $('[data-action="dislike"]').click(vote);
});
