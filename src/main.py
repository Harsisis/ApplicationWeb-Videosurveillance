from flask import Flask, render_template, abort, send_from_directory, request, config
from os import listdir
from os.path import isfile, join
from yaml import load, dump
import yaml


# constructeur classe vidéos
class caseVid:
    def __init__(self, linkPic, linkVid, title):
        self.linkPic = linkPic
        self.linkVid = linkVid
        self.title = title


def createListVid():
    global liste_files

    v1 = caseVid("http://127.0.0.1:5000/get-image/backgroundOBS.png", "http://127.0.0.1:5000/get-video/deamon.mp4",
                 "vidéo du gamin")
    v2 = caseVid("http://127.0.0.1:5000/get-image/backgroundOBS.png", "http://127.0.0.1:5000/get-video/franklin.mp4",
                 "vidéo du monsieur qui dance")
    v3 = caseVid("http://127.0.0.1:5000/get-image/backgroundOBS.png", "http://127.0.0.1:5000/get-video/deamon.mp4",
                 "vidéo dzadaz dada")
    v4 = caseVid("http://127.0.0.1:5000/get-image/backgroundOBS.png", "http://127.0.0.1:5000/get-video/deamon.mp4",
                 "vidéo azdfvfdggegeg")

    liste_files = [v1, v2, v3, v4]

    all_files = listdir(app.config["CLIENT_Files"])

    for vid in all_files:
        if vid.endswith(".mp4"):
            nom_vid = vid
            for img in all_files:
                if nom_vid[:len(nom_vid) - 3] + "png" == img:
                    nom_img = img
                    liste_files.append(caseVid("http://127.0.0.1:5000/get-image/" + nom_img,
                                               "http://127.0.0.1:5000/get-video/" + nom_vid,
                                               nom_vid[:len(nom_vid) - 4]))

    return liste_files


# Flask
app = Flask(__name__)

# app.config Gauthier
#app.config["CLIENT_Files"] = "D:/Bureau/travail/0_PROJETS/ApplicationWeb-Videosurveillance/src/static/client/files"

# app.config Nicolas
app.config["CLIENT_Files"] = "C:/Users/nicoc/PycharmProjects/ApplicationWeb-Videosurveillance/src/static/client/files"

@app.route("/get-image/<image_name>")
def get_image(image_name):
    try:
        return send_from_directory(app.config["CLIENT_Files"], filename=image_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)


@app.route("/get-video/<video_name>")
def get_video(video_name):
    try:
        return send_from_directory(app.config["CLIENT_Files"], filename=video_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)


@app.route("/update_config/", methods=['POST'])
def update_config():
    request.form.get('config', '')
    with open('D:/Bureau/travail/0_PROJETS/ApplicationWeb-Videosurveillance/src/config.yaml', 'w') as wfile:
        config_yaml = yaml.dump(config, wfile)


@app.route("/")
def home():
    with open(r'D:\Bureau\travail\0_PROJETS\ApplicationWeb-Videosurveillance\src\config.yaml') as file:
        config_yaml = yaml.full_load(file)
    return render_template("main.html",
                           videos=createListVid(),
                           ip_camera=config['ip_address'],
                           purge=config['purge'],
                           detection=config['detection'],
                           jeealert=config['jeealert'],
                           log_level=config['log_level'],
                           recording=config['recording'],
                           streaming=config['streaming'])


if __name__ == "__main__":
    app.run()
