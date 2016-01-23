# coding:utf-8
from app.models import *

def check_field_exists(obj, data, field_none=[]):
    #验证字段是否合法
    #验证字段不能为空
    #data需要验证的数据
    #field_none 可以为空字段

    for field in data.keys():
        if not hasattr(obj, field):
            #验证字段是否存在
            raise Exception("params error: {}".format(field))
        if not data.get(field, None):  #空的也都是假的，所以把not放前面
           #验证字段是否none
            if data[field] not in field_none:
                raise Exception("{0} not null".format(data[field]))



def process_result(data, output):
    black = ["_sa_instance_state"]
    ret = []
    for obj in data:
        if output:
            tmp = {}
            for f in output:
                tmp[f] = getattr(obj, f)
            ret.append(tmp)
        else:
            tmp  = obj.__dict__
            for p in black:#可能多个
                try:
                    tmp.pop(p)
                except:
                    pass
            #tmp.pop('_sa_instance_state')
            ret.append(tmp)
    return ret


def check_order_by(obj, order_by=''):
    order_by = order_by.split()
    if len(order_by) != 2:         #传2个参数，如没有2个参数就报异常
        raise Exception("order by params wrong")

    field,order = order_by
    
    order_list = ["asc","desc"]
    #处理后，传大小写都可以
    if order.lower() not in order_list:
        raise Exception("order_list format is wrong ,should be: {0}".format(order_list))

    if not hasattr(obj, field.lower()):
        raise Exception("order_list field not in table")

def check_limit(limit):
    if not str(limit).isdigit():
        raise Exception("limit must number")

def check_output_field(obj, output=[]):
    if not isinstance(output, list): #判断列表
        raise Exception("output1 must list")

    for field in output:
        if not hasattr(obj, field):
            raise Exception("{0} is not existed".format(field))
            #raise Exception("output2这个输出字段不存在".format(field))


def check_update_params(obj, data, where):
    if not data:
        raise Exception("no need") #没有需要的

    for field in data.keys():
        if not hasattr(obj, field):
            raise Exception("need update {0} this field is not exist".format(field))


    if not where:
        raise Exception("need where condition")

#必须传id
#    if where.get('id', None) is None:
    if not where.get('id', None):
        raise Exception("need id as condition")

    try:
        id = int(where['id'])
        if id <= 0:
            raise Exception("condition id value not < 0")

    except ValueError:
        raise Exception("condition id value must be int")

def check_value_exists(obj, name, value):
#def process_idc_exists(idc_id):
    #from app.models import db
    where = {name: value}
    ret = db.session.query(obj).filter_by(**where).first()
    #只有1条记录或为空，不可能存在2条记录是出错的
    print ret
    if not ret:
        raise Exception("{0}not exist".format(value))
