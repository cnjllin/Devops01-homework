# -*- coding: utf-8 -*-
__author__ = 'linf'

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey,Date,Time,Text
# 连接数据库 
engine = create_engine("mysql://root:123456@127.0.0.1:3306/Devops?charset=utf8",encoding="utf-8", echo=True)
# 获取元数据
metadata = MetaData()
# 定义表

#用户信息表
user = Table('user', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('username', String(50),nullable=False),
		Column('email',String(50),nullable=False),
		Column('department_id',Integer,index=True),
		Column('is_leader',Integer,index=True,default = 0),
		Column('phone',String(11))
    )
	
#部门信息表
department = Table('department',metadata,
        Column('id', Integer, primary_key=True),
		Column('department_name',String(50)),
		Column('superior',Integer,default = 0)
	)


#IDC信息表
idc = Table('idc',metadata,
        Column('id', Integer, primary_key=True),
		Column('name',String(10),nullable=False),
		Column('idc_name',Integer,nullable=False),
		Column('address',String(255),nullable=False),
		Column('Phone',String(15),nullable=False),
		Column('email',String(30),nullable=False),
		Column('user_interface',String(50),nullable=False),
		Column('user_phone',String(20),nullable=False),
		Column('rel_cabinet_num',Integer,nullable=False),
		Column('pact_cabinet_num',Integer,nullable=False),
	)
	
#IDC机柜信息表
cabinet = Table('cabinet',metadata,
        Column('id', Integer, primary_key=True),
		Column('name',String(10),nullable=False),
		Column('idc_name',String(30),nullable=False,index=True),
		Column('power',String(20)),
	)


#服务器制造商表
manufacturers = Table('manufacturers',metadata,
        Column('id', Integer, primary_key=True),
		Column('name',String(50),nullable=False),
	)


#服务器供应商表
supplier = Table('supplier',metadata,
        Column('id', Integer, primary_key=True),
		Column('name',String(100),nullable=False),
	)

#服务器型号表
servertype = Table('servertype',metadata,
        Column('id', Integer, primary_key=True),
		Column('type',String(20),nullable=False),
		Column('manufacturers_id',Integer,nullable=False),
	)
	
#硬盘raid信息表
raid = Table('raid',metadata,
        Column('id', Integer, primary_key=True),
		Column('type',String(20),nullable=False),
	)


#Raid卡信号信息表
raidtype = Table('raidtype',metadata,
        Column('id', Integer, primary_key=True),
		Column('name',String(50),nullable=False),
	)

#服务器状态信息表
status = Table('status',metadata,
        Column('id', Integer, primary_key=True),
		Column('name',String(20),nullable=False),
	)
	

#业务线信息表
product = Table('product',metadata,
        Column('id', Integer, primary_key=True),
		Column('service_name',String(20),nullable=False),
		Column('pid',Integer,nullable=False),
		Column('module_letter',String(10),nullable=False),
		Column('dev_interface',String(100)),
		Column('op_interface',String(100)),
	)
	

#电源功率信息表
power = Table('power',metadata,
        Column('id', Integer, primary_key=True),
		Column('server_power',String(20),nullable=False),
	)
	

#ip信息表
ip_info = Table('ip_info',metadata,
        Column('id', Integer, primary_key=True),
		Column('ip',String(20),nullable=False),
		Column('mac',String(20),nullable=False),
		Column('device',String(20),nullable=False),
		Column('server_id',Integer,nullable=False,index=True),
		Column('switch_id',Integer,nullable=False,index=True),
		Column('switch_port',Integer,nullable=False,index=True),
	)

#服务器信息表
server = Table('server',metadata,
        Column('id', Integer, primary_key=True),
		Column('supplier',Integer,index=True),
		Column('manufacturers',String(50),nullable=False,index=True),
		Column('manufacture_date',Date),
		Column('server_type',String(20)),
		Column('st',String(60),index=True),
		Column('idc_id',Integer,index=True),
		Column('cabinet_id',Integer),
		Column('cabinet_pos',String(10)),
		Column('expire',Date),
		Column('ups',Integer),
		Column('parter',String(50)),
		Column('parter_type',String(50)),
		Column('server_up_time',Date),
		Column('os_type',String(20)),
		Column('os_version',String(20)),
		Column('hostname',String(32),nullable=False,index=True),
		Column('inner_ip',String(32),nullable=False,index=True),
		Column('mac_address',String(32)),
		Column('Ip_info',String(300)),
		Column('server_cpu',String(250)),
		Column('server_disk',String(250)),
		Column('server_mem',String(250)),
		Column('raid',String(10)),
		Column('raid_card_type',String(50)),
		Column('remote_card',String(32)),
		Column('remote_cardip',String(32)),
		Column('status',Integer,index=True),
		Column('remark',Text),
		Column('last_op_time',Time),
		Column('last_op_people',Integer),
		Column('monitor_mail_group',String(32)),
		Column('Service_id',Integer,index=True),
		Column('server_purpose',Integer,index=True),
		Column('trouble_resolve',Integer),
		Column('op_interface_other',Integer),
		Column('dev_interface',Integer),
		Column('check_update_time',Time),
		Column('vm_status',Integer,nullable=False,index=True),
		Column('power',Integer),
		Column('host',Integer,index=True,default = 0),
	)
	
	
#网络设备信息表
switch = Table('switch',metadata,
        Column('id', Integer, primary_key=True),
		Column('switch_name',String(50),nullable=False),
		Column('switch_type',String(50),nullable=False),
		Column('manager_ip',String(50),nullable=False),
		Column('category',String(50),nullable=False),
		Column('idc_id',Integer,index=True),
		Column('cabinet_id',Integer,index=True),
		Column('status',Integer,index=True),
		Column('expire',Date),
		Column('remark',Text),
		Column('manufacturers',Integer),
		Column('last_op_time',Time),
		Column('last_op_people',Integer),
		Column('switch_port_nums',Integer),
		
	)

# 创建数据表，如果数据表存在，则忽视
metadata.create_all(engine)
# 获取数据库连接
conn = engine.connect()
