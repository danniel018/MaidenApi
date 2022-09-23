from sqlite3 import Date
from extensions import db
from sqlalchemy.dialects.mysql import INTEGER, ENUM, TIME
from .songs import commit
from datetime import date


members_songs = db.Table ('members_songs',
    db.Column('id',INTEGER(unsigned=True),primary_key=True),
    db.Column('member_id',db.ForeignKey('members.member_id')),
    db.Column('song_id',db.ForeignKey('songs.song_id')))

members_albums = db.Table ('members_albums',
    db.Column('id',INTEGER(unsigned=True),primary_key=True),
    db.Column('member_id',db.ForeignKey('members.member_id')),
    db.Column('album_id',db.ForeignKey('albums.album_id')))

live = db.Table ('live',
    db.Column('live_id',INTEGER(unsigned=True),primary_key=True),
    db.Column('song_id',db.ForeignKey('songs.song_id')),
    #db.Column('tour_id',db.ForeignKey('albums.album_id')),
    db.Column('live_album_id',db.ForeignKey('live_albums.live_album_id')))

class Albums(db.Model,commit):
    __tablename__ = 'albums'
    album_id = db.Column(INTEGER(unsigned=True), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    release_date = db.Column(db.Date(),nullable=False)
    length=db.Column(TIME(),nullable=False)
    cover = db.Column(db.String(85), nullable=False)
    #songs = db.relationship('Songs',backref='album')
    album_songs = db.relationship('Songs',back_populates='album')
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

        album = cls.query.filter_by(album_id = id).first()
        return album

   
class Songs(db.Model):
    __tablename__ = 'songs'

    song_id = db.Column(INTEGER(unsigned=True), primary_key=True)
    number_in_album = db.Column(db.Integer())
    name = db.Column(db.String(30), nullable=False)
    length = db.Column(TIME(),nullable=False)
    top_popular = db.Column(ENUM('yes','no'),nullable=False, default='no')
    album_id = db.Column(INTEGER(unsigned=True),db.ForeignKey('albums.album_id'))
    album = db.relationship('Albums',back_populates='album_songs')
    members = db.relationship('Members',secondary=members_songs,back_populates='songs')
    live_album = db.relationship('LiveAlbums',secondary=live,back_populates='songs')

    @classmethod
    def all_songs(cls,popular=False,year=None):
        
        if popular:
            return cls.query.filter_by(top_popular='yes').all()
        if year is not None:
            return cls.query.join(Albums, cls.album_id == Albums.album_id).filter((Albums.release_date >= f'{year}-01-01') & (Albums.release_date <= f'{year}-12-31')).all()
        else:
            return cls.query.all()

    @classmethod
    def songs_by_album(cls,id):

        songs = cls.query.filter_by(album_id = id).all()
        return songs

    @classmethod
    def song_by_id(cls,id):

        songs = cls.query.filter_by(song_id = id).first()
        return songs

    
class Users(db.Model,commit):
    __tablename__ = 'users'

    user_id = db.Column(INTEGER(unsigned=True), primary_key=True) 
    name = db.Column(db.String(30), nullable=False)
    mail = db.Column(db.String(50), nullable=False,unique=True)
    password = db.Column(db.String(256),nullable=False)

    @classmethod
    def get_by_email(cls,mail):

        return cls.query.filter_by(mail = mail).first()

class LiveAlbums(db.Model,commit):
    __tablename__ = 'live_albums'

    live_album_id = db.Column(INTEGER(unsigned=True), primary_key=True) 
    name = db.Column(db.String(35), nullable=False)
    release_date = db.Column(db.Date(),nullable=False)
    length=db.Column(TIME(),nullable=False)
    songs = db.relationship('Songs',secondary=live,back_populates='live_album')

    @classmethod
    def all_albums(cls):

        return cls.query.all()

    @classmethod
    def album_by_id(cls,id):

        album = cls.query.filter_by(live_album_id = id).first()
        return album

# class Live(db.Model,commit):
#     __tablename__ = 'live'

#     live_id = db.Column(INTEGER(unsigned=True), primary_key=True) 
#     song_id = db.Column(INTEGER(unsigned=True),db.ForeignKey('songs.songs_id'))
#     #tour_id = db.Column(INTEGER(unsigned=True),db.ForeignKey('tours.tour_id'))
#     live_album_id = db.Column(INTEGER(unsigned=True),db.ForeignKey('albums.album_id'))
#     length=db.Column(TIME(),nullable=False)
#     songs = db.relationship('Songs',back_populates='album_songs')