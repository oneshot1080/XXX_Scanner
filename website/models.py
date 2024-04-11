from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    name: Mapped[str] = mapped_column()
    id: Mapped[str] = mapped_column(primary_key=True)
    access: Mapped[bool] = mapped_column()