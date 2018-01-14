function getOppositeVote(vote) {
    if(vote.data('action') == 'like') {
        return $('[data-action="dislike"]');
    }
    else {
        return $('[data-action="like"]');
    }
}

function vote() {
    var vote = $(this);
    var url = vote.data('url');
    var pk = vote.data('id');
    console.log(url);
    var opposite = getOppositeVote(vote)
    opposite.removeClass('active');

    $.ajax({
        url: url,
        type: 'POST',
        data: pk,
        success: function (json) {
            $('[data-count="like"]').text(json.likes_count);
            $('[data-count="dislike"]').text(json.dislikes_count);

            if(json.result) {
                vote.addClass('active')
            }
            else {
                vote.removeClass('active')
            }

        }

    });

    return false;
}

$(function() {
    $('[data-action="like"]').click(vote);
    $('[data-action="dislike"]').click(vote);
});