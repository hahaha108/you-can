from application import db

class Videos(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(50),nullable=False)
    title = db.Column(db.String(500),nullable=False)
    url = db.Column(db.String(500),nullable=False)
    site = db.Column(db.String(50),nullable=False)