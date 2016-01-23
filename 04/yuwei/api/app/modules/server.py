# coding:utf-8
from app.models import db,Server
from app.utils import check_field_exists, process_result, check_order_by, check_limit, check_output_field, check_update_params

def create(**kwargs):
    #1获取参数
    check_field_exists(Server, kwargs)

    #2处理数据
    #print inspect.getmembers(Server, predicate=inspect.is)
    #return 1
    print kwargs
    #3实例化record
    record = Server(**kwargs)
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

    check_output_field(Server,output)
    
    check_order_by(Server, order_by)
    check_limit(limit)
    data = db.session.query(Server).order_by(order_by).limit(limit).all()
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
    check_update_params(Server, data, where)

    ret = db.session.query(Server).filter_by(**where).update(data)

    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])

    print ret
    return ret 
