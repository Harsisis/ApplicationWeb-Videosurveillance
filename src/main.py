from flask import Flask, render_template, abort, send_from_directory

app = Flask(__name__)

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
    return render_template("main.html")


if __name__ == "__main__":
    app.run()
