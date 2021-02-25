
function takePic () {
    var choice = window.confirm("Voulez vous voir la photo ?")
    if (choice) {
        // var downloadUrl = "http://192.168.68.103:8080/photo.jpg";
        // var downloading = browser.downloads.download({
        //     url : downloadUrl,
        //     filename : 'my-image-again.png',
        //     conflictAction : 'uniquify'
        // });
        // downloading.then(onStartedDownload, onFailed);

        window.open('http://192.168.68.103:8080/photo.jpg')
    }
}

function showParam () {
    var iframeParam = document.getElementById("param");
    if (iframeParam.style.display === "none") {
        iframeParam.style.display = "block";
    } else {
        iframeParam.style.display = "none";
    }
}

function onStartedDownload(id) {
    console.log(`Started downloading: ${id}`);
}

function onFailed(error) {
    console.log(`Download failed: ${error}`);
}

