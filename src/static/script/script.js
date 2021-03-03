function onShow (ip, log_level, detection, jeealert, recording, streaming) {
    //get ip from yaml
    if (ip === null){
        IP = 'http://192.168.68.103:8080/videofeed';
    } else {
        IP = 'http://' + ip + '/videofeed';
    }
    document.getElementById("live").src = IP;
    document.getElementById("ip").value = IP;

    document.getElementById("logLevel").value = log_level;

    document.getElementById("detectionCB").checked = detection;
    document.getElementById("jalerteCB").checked = jeealert;
    document.getElementById("recordingCB").checked = recording;
    document.getElementById("streamCB").checked = streaming;
}

function editYaml() {
    //edit yaml
    IP = document.getElementById("ip").value;
    console.log(IP);
}

function getLiveIP () {
    return 'http://' + IP + ':8080/videofeed';
}

function takePic () {
    var choice = window.confirm("Voulez vous voir la photo ?");
    if (choice) {
        window.open('http://' + IP + ':8080/photo.jpg');
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

function showVideo (url) {
    let live = document.getElementById("live");
    let snap = document.getElementById("snap");
    if (snap.style.display === "none") {
        live.style.display = "none";
        snap.style.display = "block";
    }
    snap.src = url;
}

function onStartedDownload(id) {
    console.log(`Started downloading: ${id}`);
}

function onFailed(error) {
    console.log(`Download failed: ${error}`);
}

