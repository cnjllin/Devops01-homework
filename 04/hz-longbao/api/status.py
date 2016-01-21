#_*_coding:utf-8_*_
from app.models import db, Status
from app.utils import check_field_exists,process_result,check_order_by,check_limit,check_output_field,check_update_params
import inspect

def create(**params):
    # 1. 获取参数信息
    check_field_exists(Status, params)

    print inspect.getmembers(Status,predicate=inspect.ismethod(id))

    # 传参的个数需要验证
    obj = Status(**params)

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
        if not hasattr(Status,field):
            raise Exception("{}这个输出字段不存在".format(field))

    check_output_field(Status,output)
    check_order_by(Status,order_by)
    check_limit(limit)
    data = db.session.query(Status).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = process_result(data, output)
    return ret

def update(**params):
    data = params.get('data',{})
    where = params.get('where',{})

    check_update_params(Status,data,where)
    ret = db.session.query(Status).filter_by(**where).update(data)
    try:
        db.session.commit()
    except Exception,e:
        print e.message.split()[1]
        raise Exception(e.message.split(") ")[1])

    return ret