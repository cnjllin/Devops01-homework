# coding:utf-8
from app.models import db, IpInfo, Server, Switch
#from app.utils import check_field_exists, process_result, check_order_by, check_limit, check_output_field, check_update_params
from app.utils import *

def create(**kwargs):
    #1获取参数
    check_field_exists(IpInfo, kwargs)
    check_value_exists(Server, "id", kwargs.get("server_id", None))
    check_value_exists(Switch, "id", kwargs.get("switch_id", None))

    #2处理数据
    #print inspect.getmembers(IpInfo, predicate=inspect.is)
    #return 1
    print kwargs
    #3实例化record
    record = IpInfo(**kwargs)
    #4插入到数据库
    db.session.add(record)
    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])


    return record.id

#查询
def get(**kwargs):
    output = kwargs.get('output', [])
#    output = ['name','phone']
    print output
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')

    check_output_field(IpInfo,output)
    
    check_order_by(IpInfo, order_by)
    check_limit(limit)
    data = db.session.query(IpInfo).order_by(order_by).limit(limit).all()
    #                      表     排序
    db.session.close()
    ret = process_result(data, output)
    return ret



#update
def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})

    print data
    print where
    #验证传入的信息
    check_update_params(IpInfo, data, where)

    if data.get("server_id", None):
        check_value_exists(Server, "id", data.get("server_id", None))
    if data.get("switch_id", None):
        check_value_exists(Switch, "id", kwargs.get("switch_id", None))


    ret = db.session.query(IpInfo).filter_by(**where).update(data)

    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])

    print ret
    return ret 
