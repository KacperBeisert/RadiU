$('#edit-button').click(function(){
    toggle()
});

function toggle(){
    $('#user_form').toggle();
    $('#edit-button').toggle();
}

$('#close').click(function(){
    toggle()
});