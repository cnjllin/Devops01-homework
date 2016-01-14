#_*_coding:utf-8_*_
from app.models import *
def check_field_exists(obj,data,field_none=[]):
    for field in data.keys():
        if not hasattr(obj,field):
            raise Exception('params error')
            
        if not data.get(field,None):
            if data[field] not in field_none:
                raise Exception('{} is not Null')

def process_result(**kwargs):
    print 'xxxxxxxxxxxxxxxxxxxx'
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')
    if not isinstance(output, list):
        raise Exception('output mast is list')
    for field in output:
        if not hasattr(Ip_Info, field):
            raise Exception('meiyou zhe ge ziduan'.format(field))
    data = db.session.query(Ip_Info).order_by(order_by).limit(limit).all()
    db.session.close()
    print '--------------------'
    ret = []
    black = ['_sa_instance_state']
    for obj in data:
        print obj
        if output:
            tmp = {}
            for f in output:
                tmp[f] = getattr(obj,f)
            ret.append(tmp)
        else:
            tmp = obj.__dict__
            for p in black:
                try:
                    tmp.pop(p)
                except:
                    pass
            ret.append(tmp)
    return ret

