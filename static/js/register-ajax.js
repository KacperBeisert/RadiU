// AJAX - Query to search for songs
$('#suggestion').keyup(function(){
	var query = $(this).val();
	// If query not empty
	if (query.length > 0){
		$.get('/radiu/search/', {suggestion: query}, function(data){
    		if (data[0]){
    			var items = [];
    			$.each(data, function(index, song){
    				items.push('<a class="dropdown-item" song_id="' + song.id +'">' + song.title + ' - ' + song.artist + '</a>');
    			});
    			$('.card').html( items.join('') );
    		} else{
    			$('.card').html('<a class="dropdown-item">No results matching that criteria</a>');
    		};
            // Show dropdown
            $('.card').show();
            registerResults();
	    });
	} else{
		$('.card').hide();
	}
});

// On click away from searchbar, hide dropdown
$(document).click(function(){
    $('.card').hide();
});

// On click on searchbar, deselect text
$('#suggestion').click(function(){
    $('#suggestion').removeClass("selected");
});

function registerResults(){
	$('.dropdown-item').click(function(){
		let song_id = $(this).attr("song_id");
		let song_name = $(this).html();
		$('#suggestion').val(song_name);
		$('#suggestion').addClass("selected");
		$('#id_hidden_favourite_song').val(song_id);
	})
}