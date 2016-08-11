from app import db

class Base(db.Model):
  __abstract__ = True
  id = db.Column(db.Integer, primary_key=True)
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

  def __init__(self, **kwargs):
    for k, v in kwargs.iteritems():
      if hasattr(self, k):
        setattr(self, k, v)

class Gps(Base):
  __tablename__ = 'gps'
  sensor = db.Column(db.String(255))
  value = db.Column(db.Integer)

  def __repr__(self):
    return '<Gps %s>' % (self.email)