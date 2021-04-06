from flask import Flask, request, render_template, redirect
from app import app, db
from app.models import Band, Video

@app.route("/")
def video_list():
    videos = Video.query.all()
    bands = Band.query.all()
    return render_template("videos.html", videos=videos, bands=bands)


@app.route("/video/", methods=["POST"])
def add_video():
    title = request.form["title"]
    genre = request.form["genre"]
    songs = request.form["songs"]
    if not title:
        return "Error"

    book = Book(title=title, genre=genre, songs=songs)
    db.session.add(book)
    db.session.commit()
    return redirect("/")


@app.route("/band/", methods=["POST"])
def add_band():
    band_name = request.form["band_name"]
    if not band_name:
        return "Error"

    band = Band(band_name=band_name)
    db.session.add(band)
    db.session.commit()
    return redirect("/")


@app.route("/assign/", methods=["POST"])
def assign_video():
    video_id = request.form["video_id"]
    band_id = request.form["band__id"]

    video = Video.query.get(video_id)
    video.band_id = band_id

    db.session.add(video)
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:video_id>")
def delete_video(video_id):
    video = Video.query.get(video_id)
    if not video:
        return redirect("/")

    db.session.delete(video)
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:band_id>")
def delete_author(band_id):

    band = Band.query.get(band_id)
    if not band:
        return redirect("/")

    db.session.delete(band)
    db.session.commit()
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)