const LIKE = 1;
const DISLIKE = -1;

function draw_comment(render_dict) {
    console.log(render_dict)
    var template = $('#comment-item-template').html();

    var html = Mustache.to_html(template, render_dict);
    html = $(html);
    draw_vote_result(html, render_dict.result)
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

    draw_vote_result(parent, responce.result);
}

function do_vote() {
    var vote = $(this);
    var url = vote.data('url');
    var action = vote.data('action');
    action = (action == 'like') ? LIKE : DISLIKE;
    var type = vote.data('type');
    console.log(url);

    console.log('vote clicked');

    $.ajax({
        url: url,
        type: 'POST',
        data: {
            action: action
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

$(document).ready ( function () {
    $(document).on('click', '[data-action="like"]', do_vote);
    $(document).on('click', '[data-action="dislike"]', do_vote);
});


$( window ).load(function() {
    console.log('loaded')
    var comments = $('#post-comments-list');
    var comments_url = comments.data('url');
    var post_pk = comments.data('post');

    $.get( comments_url, {'post': post_pk} )
        .done(function( data ) {
            $.each(data.reverse(), function(i, obj) {
                draw_comment(obj)
            });
        });
});

