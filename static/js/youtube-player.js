// This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// This function creates an <iframe> and YouTube player after the API code downloads.
var player;
var video_id = $("#player").attr("video_id");
function onYouTubeIframeAPIReady(){
    player = new YT.Player('player', {
	    videoId: video_id,
	});
}

$(window).resize(function(){
    sizing();
});

$(document).ready(function(){
    sizing();
})

// Resize player at small device breakpoint
function sizing(){
    if ($( window ).width() < 767.98) {
        $('#player').css("height", "50.625vw");
        $('#player').css("width", "90vw");
    } else {
        $('#player').css("height", "28.125vw");
        $('#player').css("width", "50vw");
    }
}