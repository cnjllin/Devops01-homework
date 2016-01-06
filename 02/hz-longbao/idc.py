from app.models import Server
from app import db

def init(**params):
    return "nihao"

def get(**params):

    print 'hello %s' %params.get('name')
    return 'hello %s' % Server.query.filter_by(ip='10.2.100.2').first().ip


def create(**params):

    server = Server(ip='10.2.100.2',cabinet_id='223',sn='DDASS')
    db.session.add(server)
    db.session.commit()
    return 'add data'

def update(**params):
    server = Server.query.first()
    server.ip = '192.168.1.100'
    db.session.commit()
    return 'update data'

