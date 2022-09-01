from extensions import db
from sqlalchemy.dialects.mysql import INTEGER, ENUM, TIME
from .songs import commit


members_songs = db.Table ('members_songs',
    db.Column('id',INTEGER(unsigned=True),primary_key=True),
    db.Column('member_id',db.ForeignKey('members.member_id')),
    db.Column('song_id',db.ForeignKey('songs.song_id')))

members_albums = db.Table ('members_albums',
    db.Column('id',INTEGER(unsigned=True),primary_key=True),
    db.Column('member_id',db.ForeignKey('members.member_id')),
    db.Column('album_id',db.ForeignKey('albums.album_id')))

class Albums(db.Model,commit):
    __tablename__ = 'albums'
    album_id = db.Column(INTEGER(unsigned=True), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    release_date = db.Column(db.Date(),nullable=False)
    songs = db.relationship('Songs',backref='album')
    members = db.relationship('Members',secondary=members_albums,back_populates='albums') 

    def queried_data(self):
        data = {'album_id':self.album_id,'name':self.name,
        'release_date':str(self.release_date)}

        return data

    @classmethod
    def all_albums(cls):

        return cls.query.all()

    @classmethod
    def album_by_id(cls,id):

        member = cls.query.filter_by(album_id = id).first()
        return member

   
class Songs(db.Model):
    __tablename__ = 'songs'

    song_id = db.Column(INTEGER(unsigned=True), primary_key=True)
    number_in_album = db.Column(db.Integer())
    name = db.Column(db.String(30), nullable=False)
    length = db.Column(TIME(),nullable=False)
    album_id = db.Column(INTEGER(unsigned=True),db.ForeignKey('albums.album_id'))
    members = db.relationship('Members',secondary=members_songs,back_populates='songs')

    @classmethod
    def all_songs(cls):

        return cls.query.all()

    @classmethod
    def songs_by_id(cls,id):

        songs = cls.query.filter_by(album_id = id).all()
        return songs