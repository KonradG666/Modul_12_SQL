from app import db

class Band(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   band = db.Column(db.String(15), index=True, nullable=True)
   formation = db.Column(db.String(15), index=True, nullable=True)
   videos = db.relationship("Video", backref="band", lazy="dynamic")

   def __str__(self):
       return f"{self.band}"

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), index=True, nullable=True)
    genre = db.Column(db.String(15), index=True, nullable=True)
    songs = db.Column(db.Integer, index=True, nullable=True)
    band_id = db.Column(db.Integer, db.ForeignKey("band.id"))


    def __str__(self):
        return f"{self.title}"