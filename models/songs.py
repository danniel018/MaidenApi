from extensions import db
class commit:
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete (self):
        db.session.delete(self)
        db.session.commit()