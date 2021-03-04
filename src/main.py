import os
from datetime import datetime

from flask import Flask, render_template, redirect, abort, send_from_directory, request, config
from os import listdir
from os.path import isfile, join
from yaml import load, dump
import yaml


# constructeur classe vidéos
class caseVid:
    def __init__(self, linkPic, linkVid, title, date):
        self.linkPic = linkPic
        self.linkVid = linkVid
        self.title = title
        self.date = date


def get_date(video):
    return video.date


def createListVid():
    liste_files = []

    all_files = listdir(app.config["CLIENT_Files"])

    for vid in all_files:
        if vid.endswith(".mp4"):
            nom_vid = vid
            for img in all_files:
                if nom_vid[:len(nom_vid) - 3] + "jpg" == img:
                    nom_img = img
                    liste_files.append(caseVid("http://127.0.0.1:5000/get-image/" + nom_img,
                                               "http://127.0.0.1:5000/get-video/" + nom_vid,
                                               nom_vid[:len(nom_vid) - 4],
                                               datetime.fromtimestamp(
                                                   os.stat(app.config["CLIENT_Files"] + '/' + nom_vid).st_ctime)))
    liste_files.sort(key=get_date, reverse=True)
    return liste_files


# Flask
app = Flask(__name__)

# app.config Gauthier
# app.config["CLIENT_Files"] = "D:/Bureau/travail/0_PROJETS/ApplicationWeb-Videosurveillance/src/static/client/files"
# path_yaml = 'D:/Bureau/travail/0_PROJETS/ApplicationWeb-Videosurveillance/src/config.yaml'

# app.config Yann
# app.config["CLIENT_Files"] = "H:/IUT/Portfolio/ApplicationWeb-Videosurveillance/src/static/client/files"
# path_yaml = ''

# app.config Nicolas
app.config["CLIENT_Files"] = "C:/Users/nicoc/PycharmProjects/ApplicationWeb-Videosurveillance/src/static/client/files"
path_yaml = 'C:/Users/nicoc/PycharmProjects/ApplicationWeb-Videosurveillance/src/config.yaml'

# app.config Antoine
# app.config["CLIENT_Files"] = "C:/Users/Tonio/Desktop/Projetlol/ApplicationWeb-Videosurveillance/src/static/client/files"
# path_yaml = ''

# app.config Docker
app.config["CLIENT_Files"] = "static/client/files"


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
    with open(path_yaml) as file:
        config_yaml = yaml.full_load(file)
    config_yaml['ip_address'] = request.form.get("ip", "")
    config_yaml['log_level'] = request.form.get("logLevel", "Faible")
    config_yaml['purge'] = request.form.get("purge", 25)
    config_yaml['detection'] = True if request.form.get('detection', False) else False
    config_yaml['jeealert'] = True if request.form.get('jalerte', False) else False
    config_yaml['recording'] = True if request.form.get('recording', False) else False
    config_yaml['streaming'] = True if request.form.get('stream', False) else False

    with open(path_yaml, 'w') as wfile:
        yaml.dump(config_yaml, wfile)

    return redirect("/")


@app.route("/")
def home():
    with open(path_yaml) as file:
        config_yaml = yaml.full_load(file)
    return render_template("main.html",
                           videos=createListVid(),
                           ip_camera=config_yaml['ip_address'],
                           purge=config_yaml['purge'],
                           detection=config_yaml['detection'],
                           jeealert=config_yaml['jeealert'],
                           log_level=config_yaml['log_level'],
                           recording=config_yaml['recording'],
                           streaming=config_yaml['streaming'])


def getURL():
    return request.base_url


@app.route("/settings/")
def settings():
    with open(path_yaml) as file:
        config_yaml = yaml.full_load(file)
    return render_template("param.html",
                           ip_camera=config_yaml['ip_address'],
                           purge=config_yaml['purge'],
                           detection=config_yaml['detection'],
                           jeealert=config_yaml['jeealert'],
                           log_level=config_yaml['log_level'],
                           recording=config_yaml['recording'],
                           streaming=config_yaml['streaming'])


if __name__ == "__main__":
    app.run()
