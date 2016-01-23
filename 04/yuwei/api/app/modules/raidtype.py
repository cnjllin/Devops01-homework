# coding:utf-8
from app.models import db,RaidType
import inspect
from app.utils import check_field_exists, process_result, check_order_by, check_limit, check_output_field, check_update_params

def create(**kwargs):
    #1获取参数
    check_field_exists(RaidType, kwargs)

    #2处理数据
    #print inspect.getmembers(RaidType, predicate=inspect.is)
    #return 1
    print kwargs
    #3实例化record
    record = RaidType(**kwargs)
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

    check_output_field(RaidType,output)
    
    check_order_by(RaidType, order_by)
    check_limit(limit)
    data = db.session.query(RaidType).order_by(order_by).limit(limit).all()
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
    check_update_params(RaidType, data, where)

    ret = db.session.query(RaidType).filter_by(**where).update(data)

    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])

    print ret
    return ret 
