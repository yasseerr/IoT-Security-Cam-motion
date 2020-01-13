
var last_update = 0

function check_images() {
    $('#card_holder').load("http://localhost:8000/refresh");

    console.log("hello woed again and again")
}
setInterval(check_images, 3000);