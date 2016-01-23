# coding:utf-8
from app.models import db,Idc
import inspect
from app.utils import check_field_exists, process_result, check_order_by, check_limit, check_output_field, check_update_params

def create(**kwargs):
    #1获取参数
    check_field_exists(Idc, kwargs)

    #2处理数据
    #print inspect.getmembers(Idc, predicate=inspect.is)
    #return 1
    print kwargs
    #3实例化idc
    idc = Idc(**kwargs)
    #4插入到数据库
    db.session.add(idc)
    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])


    return idc.id

#查询
def get(**kwargs):
    output = kwargs.get('output', [])
#    output = ['name','phone']
    print output
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')

    check_output_field(Idc,output)
    
    check_order_by(Idc, order_by)
    check_limit(limit)
    data = db.session.query(Idc).order_by(order_by).limit(limit).all()
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
    check_update_params(Idc, data, where)

    ret = db.session.query(Idc).filter_by(**where).update(data)

    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])

    print ret
    return ret 
