import uuid
from . import db
from .models import Member


def add_member(name, id):
    member = Member(id=id, name=name, access=True)
    db.session.add(member)
    db.session.commit()
    
def delete_member(id):
    member = Member.query.get(id)
    db.session.delete(member)
    db.session.commit()
    
def modify_info(id, name):
    member = Member.query.get(id)
    member.name = name
    db.session.commit()