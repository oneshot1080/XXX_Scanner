from . import db
from .models import Member

def is_registered_member(id):
    return Member.query.filter_by(id=id).first()
