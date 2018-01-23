const LIKE = 1;
const DISLIKE = -1;

function draw_comment(response) {
    var template = $('#comment-item-template').html();

    console.log('template:', template);
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

function vote_for_comment() {
    var vote = $(this);
    var url = vote.data('url');
    var action = vote.data('action');
    action = (action == 'like-comment') ? LIKE : DISLIKE;
    console.log(url);
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            'action': action
        },
        success: function (responce) {
            var parent = vote.closest('.comment-votes');
            console.log(parent)
            parent.find('[data-action="rating-comment"]').text(responce.rating);
            console.log(responce);
        }

    });
}

$(function() {
    $('[data-action="like-comment"]').click(vote_for_comment);
    $('[data-action="dislike-comment"]').click(vote_for_comment);
});


