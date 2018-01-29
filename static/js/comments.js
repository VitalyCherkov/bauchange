const LIKE = 1;
const DISLIKE = -1;

function draw_comment(response) {
    console.log(response)
    var template = $('#comment-item-template').html();

    var html = Mustache.to_html(template, response);
    $('#post-comments-list').prepend(html);

}

function add_comment_form() {
    var form = $('#add-comment-form');
    var url = form.data('url');

    var post_pk = {
        'post': form.data('post')
    };
    var data = form.serialize() + '&' + $.param(post_pk);

    form.each(function(){
        this.reset();
    });

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        success: function(response){
            draw_comment(response);
        }
    });

    return false;
}

function draw_vote_result(vote_block, result) {
    var like = vote_block.find('[data-action="like"]');
    var dislike = vote_block.find('[data-action="dislike"]');
    like.removeClass('active');
    dislike.removeClass('active');

    console.log(LIKE)

    switch (parseInt(result, 10)){
        case LIKE:
            like.addClass('active');
            break;
        case DISLIKE:
            dislike.addClass('active');
            break;
    }
}

function vote_for_comment() {
    var vote = $(this);
    var url = vote.data('url');
    var action = vote.data('action');
    action = (action == 'like') ? LIKE : DISLIKE;
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            'action': action
        },
        success: function (responce) {
            console.log(responce)
            var parent = vote.closest('.comment-votes');
            parent.find('[data-action="rating"]').text(responce.rating);
            draw_vote_result(parent, responce.result)
        }
    });
}

$(function() {
    $('[data-action="like"]').click(vote_for_comment);
    $('[data-action="dislike"]').click(vote_for_comment);
});


