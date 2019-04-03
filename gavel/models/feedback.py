from gavel.models import db
from datetime import datetime

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    annotator_id = db.Column(db.Integer, db.ForeignKey('annotator.id'))
    annotator = db.relationship('Annotator', foreign_keys=[annotator_id], uselist=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item = db.relationship('Item', foreign_keys=[item_id], uselist=False)
    feedback_type = db.Column(db.String(10))
    feedback = db.Column(db.String(250))
    time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, annotator, item, feedback_type, feedback):
        self.annotator = annotator
        self.item = item
        self.feedback_type = feedback_type
        self.feedback = feedback
