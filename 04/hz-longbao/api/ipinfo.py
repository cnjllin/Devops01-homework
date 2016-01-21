#_*_coding:utf-8_*_
from app.models import db, IpInfo , Server, Switch
from app.utils import *
import inspect

def create(**params):
    # 1. 获取参数信息
    check_field_exists(IpInfo, params)

    print inspect.getmembers(IpInfo,predicate=inspect.ismethod(id))

    # 传参的个数需要验证
    obj = IpInfo(**params)

    # 插入到数据库
    db.session.add(obj)

    try:
        db.session.commit()
    except Exception,e:
        print e.message.split()[1]
        raise Exception(e.message.split(") ")[1])
    return obj.id

def get(**params):
    output = params.get('output',[])
    limit = params.get('limit',10)
    order_by = params.get('order_by','id desc')

    if not isinstance(output, list):
        raise Exception("output必须为列表")

    for field in output:
        if not hasattr(IpInfo,field):
            raise Exception("{}这个输出字段不存在".format(field))

    check_output_field(IpInfo,output)
    check_order_by(IpInfo,order_by)
    check_limit(limit)
    data = db.session.query(IpInfo).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = process_result(data, output)
    return ret

def update(**params):
    data = params.get('data',{})
    where = params.get('where',{})

    check_update_params(IpInfo,data,where)

    if data.get("server_id",None):
        check_value_exists(Server, "id", data.get("server_id",None))
    if data.get("switch_id",None):
        check_value_exists(Switch, "id", params.get("switch_id",None))

    ret = db.session.query(IpInfo).filter_by(**where).update(data)
    try:
        db.session.commit()
    except Exception,e:
        print e.message.split()[1]
        raise Exception(e.message.split(") ")[1])

    return ret