#_*_coding:utf-8_*_
from app.models import db,Power
from app.utils import check_field_exists,process_result
def create(**kwargs):
    check_field_exists(Power,kwargs)
    obj = Power(**kwargs)
    db.session.add(obj)
    db.session.commit()
    return obj.id

def get(**kwargs):
    ret = process_result(**kwargs)
    return ret
        

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})
    if not data:
        raise Exception('meiyou xuyaode')
    for field in data.keys():
        if not hasattr(Power, field):
            raise Exception('xuyao gengxin de {}ziduan bucunzai'.format(field))
        if not where:
            raise Exception('xuyao tigong where tiaojian')
        if where.get('id', None) is None:
            raise Exception('xuyao tigong id zuowei tiaojian')
        try:
            id = int(where['id'])
            if id <= 0:
                raise Exception('id buneng shi fushu')
        except ValueError:
            raise Exception('id bixun shi int')
        ret = db.session.query(Power).filter_by(**where).update(data)
        db.session.commit()
        return ret

