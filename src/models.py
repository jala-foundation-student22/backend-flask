from src import app, db


class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    category = db.Column(db.String)
    deadline = db.Column(db.DateTime)
    status = db.Column(db.String)

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "deadline": self.deadline,
            "status": self.status,
        }


with app.app_context():
    db.create_all()
