function checkFav(){
    // Operate function on fav button
    $('#fav-button').each(function(){
    	let fav_img = $(this).attr("fav-img");
    	let unfav_img = $(this).attr("unfav-img");
    	let faved = $(this).attr("faved");
    	let string1 = 'background-image: url(';
    	let string2 = ')';
    	let string3;
    	// Determine if song is favourited or not
    	if (faved == 'yes'){
    		// If song is favourited, add faved img
    		string3 = string1.concat(fav_img, string2);
    	} else if (faved == "no"){
    		// If not favourited, add unfaved img
    		string3 = string1.concat(unfav_img, string2);
    	};
    	console.log(string3);
    	$(this).attr('style', string3);
    })
};

// AJAX - Call to fav/unfav song
$('#fav-button').click(function(){
	let button = $(this);
	let faved = $(this).attr("faved");
	let songid = $(this).attr("data-songid");
	$.get('/radiu/favourite/', { song_id: songid, favunfav: faved }, function(data){
    	if (data == 'set' & faved == "no"){
    		button.attr('faved', 'yes');
    	} else if (data == 'removed' & faved == "yes"){
    		button.attr('faved', 'no');
    	};
    	checkFav();
	});
});