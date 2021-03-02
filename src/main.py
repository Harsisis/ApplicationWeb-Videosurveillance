from flask import Flask, render_template, abort, send_from_directory


# constructeur classe vidéos
class caseVid:
    def __init__(self, linkPic, linkVid, title):
        self.linkPic = linkPic
        self.linkVid = linkVid
        self.title = title


def createListVid():
    v1 = caseVid("http://127.0.0.1:5000/get-image/backgroundOBS.png", "http://127.0.0.1:5000/get-video/deamon.mp4",
                 "vidéo du gamin")
    v2 = caseVid("http://127.0.0.1:5000/get-image/backgroundOBS.png", "http://127.0.0.1:5000/get-video/franklin.mp4",
                 "vidéo du monsieur qui dance")
    v3 = caseVid("http://127.0.0.1:5000/get-image/backgroundOBS.png", "http://127.0.0.1:5000/get-video/deamon.mp4",
                 "vidéo")
    v4 = caseVid("http://127.0.0.1:5000/get-image/backgroundOBS.png", "http://127.0.0.1:5000/get-video/deamon.mp4",
                 "vidéo")

    list = [v1, v2, v3, v4]

    return list


# Flask
app = Flask(__name__)

# app.config Gauthier
app.config["CLIENT_IMAGES"] = "D:/Bureau/travail/0_PROJETS/ApplicationWeb-Videosurveillance/src/static/client/img"
app.config["CLIENT_VIDEOS"] = "D:/Bureau/travail/0_PROJETS/ApplicationWeb-Videosurveillance/src/static/client/vid"


@app.route("/get-image/<image_name>")
def get_image(image_name):
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=image_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)


@app.route("/get-video/<video_name>")
def get_video(video_name):
    try:
        return send_from_directory(app.config["CLIENT_VIDEOS"], filename=video_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)


@app.route("/")
def home():
    return render_template("main.html", videos=createListVid())


if __name__ == "__main__":
    app.run()
