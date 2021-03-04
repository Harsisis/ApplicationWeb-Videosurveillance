function onShow (ip, log_level, detection, jeealert, recording, streaming) {

    document.getElementById("live").src = 'http://' + ip + '/videofeed';
    document.getElementById("ip").value = ip;
    document.getElementById("settings").src = 'http://' + ip + '/settings_window.html';

    document.getElementById("logLevel").value = log_level;

    if (detection === "True" || detection === "true") {
        document.getElementById("detectionCB").checked = true
    } else{
        document.getElementById("detectionCB").checked = false
    }
    if (jeealert === "True" || jeealert === "true") {
        document.getElementById("jalerteCB").checked = true
    } else{
        document.getElementById("jalerteCB").checked = false
    }
    if (recording === "True" || recording === "true") {
        document.getElementById("recordingCB").checked = true
    } else{
        document.getElementById("recordingCB").checked = false
    }
    if (streaming === "True" || streaming === "true") {
        document.getElementById("streamCB").checked = true
    } else{
        document.getElementById("streamCB").checked = false
    }
    console.log(detection);
    console.log(jeealert);
    console.log(recording);
    console.log(streaming);
}

function takePic (ipadr) {
    var choice = window.confirm("Voulez vous voir la photo ?");
    if (choice) {
        window.open('http://' + ipadr + '/photo.jpg');
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

function showLive (ip) {
    let live = document.getElementById("live");
    let snap = document.getElementById("snap");
    if (snap.style.display === "none") {
        live.style.display = "none";
        snap.style.display = "block";
    }
    snap.src = 'http://' + ip + '/videofeed';
}

function onStartedDownload(id) {
    console.log(`Started downloading: ${id}`);
}

function onFailed(error) {
    console.log(`Download failed: ${error}`);
}

function popup (page) {
    var w = window.open(page,'Paramètres', 'top = 560, left = 1100', 'width = 800, height = 943' );
    w.document.close();
    w.focus();
}

function fermer (page) {
    if (window.document) {
        window.close();
    }
}