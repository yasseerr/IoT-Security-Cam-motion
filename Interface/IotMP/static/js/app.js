
var last_update = 0

function check_images() {
    
    $.get("192.168.43.207/pir_check",
        function (data, textStatus, jqXHR) {
            console.log(data)
        }
    );

    console.log("hello woed again and again")
}
setInterval(check_images, 3000);