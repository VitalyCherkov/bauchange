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

    console.log(LIKE);

    switch (parseInt(result, 10)){
        case LIKE:
            like.addClass('active');
            break;
        case DISLIKE:
            dislike.addClass('active');
            break;
    }
}

function comment_vote_success(responce, current) {
    var parent = current.closest('.comment-votes');
    parent.find('[data-action="rating"]').text(responce.rating);
    draw_vote_result(parent, responce.result)
}

function post_vote_success(responce, current) {
    var parent = current.closest('.post-votes');

    var likes_text = parent.find('[data-count="like"]');
    likes_text.text(responce.likes);

    var dislikes_text = parent.find('[data-count="dislike"]');
    dislikes_text.text(responce.dislikes);

    var like = parent.find('[data-action="like"]');
    var dislike = parent.find('[data-action="dislike"]');

    like.removeClass('active');
    dislike.removeClass('active');

    switch (parseInt(responce.result, 10)){
        case LIKE:
            like.addClass('active');
            break;
        case DISLIKE:
            dislike.addClass('active');
            break;
    }

}

function do_vote() {
    var vote = $(this);
    var url = vote.data('url');
    var action = vote.data('action');
    action = (action == 'like') ? LIKE : DISLIKE;
    var type = vote.data('type');

    console.log('vote clocked');

    $.ajax({
        url: url,
        type: 'POST',
        data: {
            'action': action
        },
        success: function (responce) {
            console.log(responce);
            if(type == 'post') {
                post_vote_success(responce, vote);
            }
            else {
                comment_vote_success(responce, vote);
            }
        }
    });
}

$(function() {
    $('[data-action="like"]').click(do_vote);
    $('[data-action="dislike"]').click(do_vote);
});


