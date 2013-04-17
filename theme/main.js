function main() {
    var D = document,
        redditElems = D.getElementsByClassName('reddit-btn');

    for (var i = 0, len = redditElems.length; i < len; ++i) {
        var el = redditElems[i];
        setupRedditBtn(el);
    }
}

function setupRedditBtn(el) {
    // From http://www.reddit.com/static/button/button1.js
    var base_url = 'https:' == document.location.protocol ?
            'https://redditstatic.s3.amazonaws.com' :
            'http://www.reddit.com/static';

    var html='<iframe src="' + base_url + '/button/button1.html?width=120';

    // TODO: Use canonical url here.
    html += '&url=' +
        encodeURIComponent(window.reddit_url || window.location.href);

    if (window.reddit_title)
        html += '&title=' + encodeURIComponent(window.reddit_title);
    if (window.reddit_target)
        html += '&sr=' + encodeURIComponent(window.reddit_target);
    if (window.reddit_css)
        html += '&css=' + encodeURIComponent(window.reddit_css);
    if (window.reddit_bgcolor)
        html += '&bgcolor=' + encodeURIComponent(window.reddit_bgcolor);
    if (window.reddit_bordercolor)
        html += '&bordercolor=' + encodeURIComponent(window.reddit_bordercolor);
    if (window.reddit_newwindow)
        html += '&newwindow=' + encodeURIComponent(window.reddit_newwindow);

    html += '" height=20 width=120 scrolling=no frameborder=0></iframe>';
    el.insertAdjacentHTML('afterend', html);
    el.parentNode.removeChild(el);
}

main();
