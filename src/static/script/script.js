function onShow(ip, log_level, detection, jeealert, recording, streaming) {

    document.getElementById("live").src = 'http://' + ip + '/videofeed';
    document.getElementById("ip").value = ip;
    document.getElementById("settings").src = 'http://' + ip + '/settings_window.html';

    document.getElementById("logLevel").value = log_level;

    if (detection === "True" || detection === "true") {
        document.getElementById("detectionCB").checked = true
    } else {
        document.getElementById("detectionCB").checked = false
    }
    if (jeealert === "True" || jeealert === "true") {
        document.getElementById("jalerteCB").checked = true
    } else {
        document.getElementById("jalerteCB").checked = false
    }
    if (recording === "True" || recording === "true") {
        document.getElementById("recordingCB").checked = true
    } else {
        document.getElementById("recordingCB").checked = false
    }
    if (streaming === "True" || streaming === "true") {
        document.getElementById("streamCB").checked = true
    } else {
        document.getElementById("streamCB").checked = false
    }
    console.log(detection);
    console.log(jeealert);
    console.log(recording);
    console.log(streaming);
}

function onShow2(ip, log_level, detection, jeealert, recording, streaming) {

    document.getElementById("ip").value = ip;
    document.getElementById("settings").src = 'http://' + ip + '/settings_window.html';

    document.getElementById("logLevel").value = log_level;

    if (detection === "True" || detection === "true") {
        document.getElementById("detectionCB").checked = true
    } else {
        document.getElementById("detectionCB").checked = false
    }
    if (jeealert === "True" || jeealert === "true") {
        document.getElementById("jalerteCB").checked = true
    } else {
        document.getElementById("jalerteCB").checked = false
    }
    if (recording === "True" || recording === "true") {
        document.getElementById("recordingCB").checked = true
    } else {
        document.getElementById("recordingCB").checked = false
    }
    if (streaming === "True" || streaming === "true") {
        document.getElementById("streamCB").checked = true
    } else {
        document.getElementById("streamCB").checked = false
    }
    console.log(detection);
    console.log(jeealert);
    console.log(recording);
    console.log(streaming);
}


function takePic(ipadr) {
    var choice = window.confirm("Voulez vous voir la photo ?");
    if (choice) {
        window.open('http://' + ipadr + '/photo.jpg');
    }
}

function showParam() {
    let iframeParam = document.getElementById("param");
    if (iframeParam.style.display === "none") {
        iframeParam.style.display = "block";
    } else {
        iframeParam.style.display = "none";
    }

}

function showVideo(url, title) {
    let live = document.getElementById("live");
    let snap = document.getElementById("snap");
    if (snap.style.display === "none") {
        live.style.display = "none";
        snap.style.display = "block";
    }
    snap.src = url;
    document.getElementById("titleVideo").innerHTML = title;
}

function showLive(ip) {
    let live = document.getElementById("live");
    let snap = document.getElementById("snap");
    if (snap.style.display === "none") {
        live.style.display = "none";
        snap.style.display = "block";
    }
    snap.src = 'http://' + ip + '/videofeed';
    document.getElementById("titleVideo").innerHTML = "Vidéo en direct"
}

function onStartedDownload(id) {
    console.log(`Started downloading: ${id}`);
}

function onFailed(error) {
    console.log(`Download failed: ${error}`);
}

function popup(page) {
    var w = window.open(page, 'Paramètres', 'top = 560, left = 100', 'width = 600, height = 800');
    w.document.close();
    w.focus();
}

function fermer() {
    if (confirm("Êtes vous sur de vouloir fermer ? ")) {
        window.close();
    }
}