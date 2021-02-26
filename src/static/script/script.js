
function takePic () {
    var choice = window.confirm("Voulez vous voir la photo ?")
    if (choice) {
        window.open('http://192.168.68.103:8080/photo.jpg')
    }
}

function showParam () {
    let iframeParam = document.getElementById("param");
    if (iframeParam.style.display === "none") {
        iframeParam.style.display = "block";
    } else {
        iframeParam.style.display = "none";
    }
}

function showActivity () {
    let div = document.getElementById("activity");
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function onStartedDownload(id) {
    console.log(`Started downloading: ${id}`);
}

function onFailed(error) {
    console.log(`Download failed: ${error}`);
}

