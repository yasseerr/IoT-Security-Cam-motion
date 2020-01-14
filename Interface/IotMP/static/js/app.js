var last_update = 0

function check_images() {
    host_url = $("#url_holder").attr('url_data');
    $('#card_holder').load(host_url);

    console.log("hello word again and again")
}
setInterval(check_images, 3000);