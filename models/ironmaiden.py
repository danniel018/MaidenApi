from extensions import db
from sqlalchemy.dialects.mysql import INTEGER, ENUM

# members_songs = db.Table ('members_songs',
#     db.Column('id',INTEGER(unsigned=True),primary_key=True),
#     db.Column('member_id',db.ForeignKey('members.member_id')),
#     db.Column('song_id',db.ForeignKey('songs.song_id')))

class Members(db.Model):
    __tablename__ = 'members'
    member_id = db.Column(INTEGER(unsigned=True), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.Date(),nullable=False)
    active = db.Column(ENUM('yes','no'),default='yes')
    #songs = db.relationship('Songs',secondary= members_songs,back_populates='members')

    @classmethod
    def all_members(cls):

        return cls.query.all()