from extensions import db
from sqlalchemy.dialects.mysql import INTEGER, ENUM
from .albums import members_songs, members_albums

from .songs import commit

class Members(db.Model,commit):
    __tablename__ = 'members'
    member_id = db.Column(INTEGER(unsigned=True), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.Date(),nullable=False)
    active = db.Column(ENUM('yes','no'),default='yes')
    songs = db.relationship('Songs',secondary= members_songs,back_populates='members')
    albums = db.relationship('Albums',secondary=members_albums,back_populates='members')
    
    def queried_data(self):
        data = {'member_id':self.member_id,'name':self.name,'birthday':str(self.date_of_birth),
        'active':self.active}

        return data

    @classmethod
    def all_members(cls):

        return cls.query.all()

    @classmethod
    def member_by_id(cls,id):

        member = cls.query.filter_by(member_id = id).first()
        return member

    @classmethod
    def member_songs(cls,id):
        songs= cls.query.filter_by(member_id = id).first()
    
    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()
        
    def delete (self):
        db.session.delete(self)
        db.session.commit()