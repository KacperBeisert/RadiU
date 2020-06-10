// On document load - Check likes
$(document).ready(function(){
	checkLikes()
	checkFav()
});

function checkLikes(){
    // Loop through each like button
    $('.like-button').each(function(){
    	let like_img = $(this).attr("like-img");
    	let unlike_img = $(this).attr("unlike-img");
    	let liked = $(this).attr("liked");
    	let string1 = 'background-image: url(';
    	let string2 = ')';
    	let string3;
    	// Determine if song is liked or not
    	if (liked == 'yes'){
    		// If song is liked, add liked img
    		string3 = string1.concat(like_img, string2);
    	} else if (liked == "no"){
    		// If not liked, add unliked img
    		string3 = string1.concat(unlike_img, string2);
        };
    	$(this).attr('style', string3);
    })
};

// AJAX - Call to like/unlike song
$('.like-button').click(function(){
	let button = $(this);
	let liked = $(this).attr("liked");
	let songid = $(this).attr("data-songid");
	let likes = parseInt($(this).attr("likes"));
	$.get('/radiu/like/', { song_id: songid, addsub: liked }, function(data){
		if (data == 'add' & liked == "no"){
			button.attr('liked', 'yes');
			likes += 1
		} else if (data == 'sub' & liked == "yes"){
			button.attr('liked', 'no');
			likes -= 1;
		};
		button.attr('likes', likes);
		let element = "#like_count_".concat(songid);
		$(element).html(likes);
		checkLikes();
	});
});

// AJAX - Query to search for songs
$('#suggestion').keyup(function(){
	var query = $(this).val();
	var parent = $(this).parent('.dropdown');
	// If query not empty
	if (query.length > 0){
		$.get('/radiu/search/', {suggestion: query}, function(data){
    		if (data[0]){
    			var items = [];
    			$.each(data, function(index, song){
    				items.push('<a class="dropdown-item" href="/radiu/song/' + song.slug + '">' + song.title + ' - ' + song.artist + '</a>');
    			});
    			$('#search-results').html( items.join('') );
    		} else{
    			$('#search-results').html('<a class="dropdown-item" href="">No results matching that criteria!</a>');
    		};
	    });
	    // Show dropdown
	    $('#search-results').addClass("show");
	} else{
	    // Hide dropdown
	    $('#search-results').removeClass("show");
	};
});

// On click away from searchbar, hide dropdown
$(document).click(function(){
    $('#search-results').removeClass("show");
});

// Above won't work on searchbar itself!
$('#search-results').click(function(e){
    e.stopPropagation();
});