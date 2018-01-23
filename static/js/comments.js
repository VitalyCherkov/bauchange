function draw_comment(response) {
    var template =
        "<div class=\"comment row\">\n" +
        "    <div class=\"comment-author-photo col\">\n" +
        "        <img src=\"/bauchange_fish/img/user_empty.png\" class=\"rounded\">\n" +
        "    </div>\n" +
        "    <div class=\"comment-content col\">\n" +
        "        <p class=\"comment-author\">{{ username }}</p>\n" +
        "        <p class=\"comment-text\">\n" +
        "            {{ text }}\n" +
        "        </p>\n" +
        "        <div class=\"comment-footer\">\n" +
        "            <span class=\"comment-pub-date meta\">{{ pub_date }}</span>\n" +
        "            <span class=\"comment-votes btn-group float-right\" role=\"group\">\n" +
        "                    <button type=\"button\" class=\"btn btn-sm btn-outline-success\">+</button>\n" +
        "                    <button type=\"button\" class=\"btn btn-sm btn-light\" disabled>{{ rating }}</button>\n" +
        "                    <button type=\"button\" class=\"btn btn-sm btn-outline-danger\">-</button>\n" +
        "                </span>\n" +
        "        </div>\n" +
        "        <div class=\"dropdown-divider\"></div>\n" +
        "    </div>\n" +
        "</div>";

    var data = {
        text: response.text,
        pub_date: response.pub_date,
        rating: response.rating
    };

    console.log(data)
    console.log('template:', template);
    var html = Mustache.to_html(template, data);
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


