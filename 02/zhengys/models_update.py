#!/usr/bin/env python
#coding:utf-8
#update:2016-01-18

class User(db.Model):               # 用户信息表.
    __tablename__       =   "user"
    id                  =   db.Column(db.Integer, autoincrement=True, primary_key=True)
    name                =   db.Column(db.String(50), nullable=False)
    username            =   db.Column(db.String(50), nullable=False)
    email               =   db.Column(db.String(50), nullable=False)
    department_id       =   db.Column(db.Integer, index=True) 
    is_leader           =   db.Column(db.Integer, index=True, default=0)
    phone               =   db.Column(db.String(11))

    def __repr__(self):             #返回一个具有可读性的字符串表示模型,可在调试和测试时使用。
        return '<User %r>' % self.name

class Department(db.Model):         # 部门信息表.
    __tablename__       =   "department"
    id                  =   db.Column(db.Integer, autoincrement=True, primary_key=True)
    department_name     =   db.Column(db.String(50))
    superior            =   db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Department %r>' % self.department_name
    
class Idc(db.Model):                # IDC信息表
    __tablename__       = "idc"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name                = db.Column(db.String(10), index=True, nullable=False, unique=True)
    idc_name            = db.Column(db.String(30), nullable=False)
    address             = db.Column(db.String(255), nullable=False)
    Phone               = db.Column(db.String(15), nullable=False)
    email               = db.Column(db.String(30), nullable=False)
    user_interface      = db.Column(db.String(50), nullable=False)
    user_phone          = db.Column(db.String(20), nullable=False)
    rel_cabinet_num     = db.Column(db.Integer, nullable=False)
    pact_cabinet_num    = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Idc %r>' % self.name

class Cabinet(db.Model):            # IDC机柜信息表
    __tablename__       = "cabinet"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name                = db.Column(db.String(30), nullable=False)
    idc_id              = db.Column(db.Integer, index=True, nullable=False)
    power               = db.Column(db.String(20))

    def __repr__(self):
        return '<Idc %r>' % self.name

class Manufacturers(db.Model):      # 服务器制造商表
    __tablename__       = "manufacturers"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name                = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Idc %r>' % self.name

class Supplier(db.Model):           # 服务器供应商表 
    __tablename__       = "supplier"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True) 
    name                = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Idc %r>' % self.name

class Servertype(db.Model):         # 服务器型号表
    __tablename__       = "servertype"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True) 
    type                = db.Column(db.String(20), nullable=False)
    manufacturers_id    = db.Column(db.Integer, index=True, nullable=False)

    def __repr__(self):
        return '<Idc %r>' % self.id
    

class Raid(db.Model):               # 硬盘Raid信息表
    __tablename__       = "raid"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True) 
    name                = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Idc %r>' % self.name

class Raidtype(db.Model):           # Raid卡型号信息表
    __tablename__       = "raidtype"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True) 
    name                = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Idc %r>' % self.name

class Status(db.Model):             # 服务器状态信息表
    __tablename__       = "status"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True) 
    name                = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Idc %r>' % self.name

class Product(db.Model):            # 业务线信息表
    __tablename__       = "product"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True) 
    service_name        = db.Column(db.String(20), nullable=False)
    pid                 = db.Column(db.Integer, nullable=False, default=0)
    module_letter       = db.Column(db.String(10), nullable=False)
    dev_interface       = db.Column(db.String(100))
    op_interface        = db.Column(db.String(100))

    def __repr__(self):
        return '<Idc %r>' % self.service_name

class Power(db.Model):              # 电源功率信息表
    __tablename__       = "power"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True) 
    server_power        = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Idc %r>' % self.id

class Ip(db.Model):                 # ip信息表
    __tablename__       = "ip_info"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ip                  = db.Column(db.String(20), nullable=False)
    mac                 = db.Column(db.String(20), nullable=False)
    device              = db.Column(db.String(20), nullable=False)
    server_id           = db.Column(db.Integer, index=True, nullable=False)
    switch_id           = db.Column(db.Integer, index=True, nullable=False)
    switch_port         = db.Column(db.Integer)

    def __repr__(self):
        return '<Idc %r>' % self.ip

class Server(db.Model):             # 服务器信息表
    __tablename__       = "server"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True)
    supplier            = db.Column(db.Integer, index=True)
    manufacturers       = db.Column(db.String(50), index=True, nullable=False)
    manufacture_date    = db.Column(db.Date)
    server_type         = db.Column(db.String(20))
    st                  = db.Column(db.String(60), index=True)
    assest_no           = db.Column(db.String(60))
    idc_id              = db.Column(db.Integer, index=True)
    cabinet_id          = db.Column(db.Integer)
    cabinet_pos         = db.Column(db.String(10))
    expire              = db.Column(db.Date)
    ups                 = db.Column(db.Integer)
    parter              = db.Column(db.String(50))
    parter_type         = db.Column(db.String(50))
    server_up_time      = db.Column(db.Date)
    os_type             = db.Column(db.String(20))
    os_version          = db.Column(db.String(10))
    hostname            = db.Column(db.String(32), index=True, nullable=False)
    inner_ip            = db.Column(db.String(32), index=True, nullable=False)
    mac_address         = db.Column(db.String(32))
    Ip_info             = db.Column(db.String(300))
    server_cpu          = db.Column(db.String(250))
    server_disk         = db.Column(db.String(250))
    server_mem          = db.Column(db.String(250))
    raid                = db.Column(db.String(10))
    raid_card_type      = db.Column(db.String(50))
    remote_card         = db.Column(db.String(32))
    remote_cardip       = db.Column(db.String(32))
    status              = db.Column(db.Integer, index=True)
    remark              = db.Column(db.Text)
    last_op_time        = db.Column(db.DateTime)
    last_op_people      = db.Column(db.Integer)
    monitor_mail_group  = db.Column(db.String(32))
    Service_id          = db.Column(db.Integer, index=True)
    server_purpose      = db.Column(db.Integer, index=True)
    trouble_resolve     = db.Column(db.Integer)
    op_interface_other  = db.Column(db.Integer)
    dev_interface       = db.Column(db.Integer)
    check_update_time   = db.Column(db.DateTime)
    vm_status           = db.Column(db.Integer, index=True, nullable=False)
    power               = db.Column(db.Integer)
    host                = db.Column(db.DateTime, index=True, default=0)

    def __repr__(self):
        return '<Idc %r>' % self.supplier

class Switch(db.Model):             # 网络设备信息表
    __tablename__       = "switch"
    id                  = db.Column(db.Integer, autoincrement=True, primary_key=True)
    switch_name         = db.Column(db.String(50), nullable=False)
    switch_type         = db.Column(db.String(50), nullable=False)
    manager_ip          = db.Column(db.String(50), nullable=False)
    category            = db.Column(db.String(50), nullable=False)
    idc_id              = db.Column(db.Integer, index=True)
    cabinet_id          = db.Column(db.Integer, index=True)
    status              = db.Column(db.Integer, index=True)
    expire              = db.Column(db.Date)
    remark              = db.Column(db.Text)
    manufacturers       = db.Column(db.Integer)
    last_op_time        = db.Column(db.DateTime)
    last_op_people      = db.Column(db.Integer)
    switch_port_nums    = db.Column(db.Integer)

    def __repr__(self):
        return '<Idc %r>' % self.switch_name
