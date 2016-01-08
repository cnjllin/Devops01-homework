from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager,Shell

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cmdbtest:123456@127.0.0.1/cmdbtest'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
manager = Manager(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, index=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    department_id = db.Column(db.Integer)
    is_leader = db.Column(db.Integer,default = 0, index=True)
    phone = db.Column(db.String(11))
    def __repr__(self):
        return '<User %r>' % self.username

class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50))
    superior = db.Column(db.Integer, default = 0)
    def __repr__(self):
        return '<Department %r>' % self.department_name

class Idc(db.Model):
    __tablename__ = 'idc'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    idc_name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    user_interface = db.Column(db.String(50), nullable=False)
    user_phone = db.Column(db.String(20), nullable=False)
    rel_cabinet_num = db.Column(db.Integer, nullable=False)
    pact_cabinet_num= db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Idc %r>' % self.idc_name

class Cabinet(db.Model):
    __tablename__ = 'cabinet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    idc_id = db.Column(db.Integer, nullable=False)
    power = db.Column(db.String(20))
    def __repr__(self):
        return '<Cabinet %r>' % self.name

class Manufacturers(db.Model):
    __tablename__ = 'manufacturers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Manufacturers %r>' % self.name

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Supplier %r>' % self.name

class Servertype(db.Model):
    __tablename__ = 'servertype'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    manufacturers_id = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Servertype %r>' % self.type

class Raid(db.Model):
    __tablename__ = 'raid'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return '<Raid %r>' % self.name


class Raidtype(db.Model):
    __tablename__ = 'raidtype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Raidtype %r>' % self.name

class  Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return '<Status %r>' % self.name

class  Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(20), nullable=False)
    pid = db.Column(db.Integer, default = 0, nullable=False)
    module_letter = db.Column(db.String(10), nullable=False)
    dev_interface = db.Column(db.String(100))
    op_interface = db.Column(db.String(100))
    def __repr__(self):
        return '<Product %r>' % self.service_name

class  Power(db.Model):
    __tablename__ = 'power'
    id = db.Column(db.Integer, primary_key=True)
    server_power = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return '<Power %r>' % self.server_power

class Ip_info(db.Model):
    __tablename__ = 'ip_info'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(20), nullable=False)
    mac = db.Column(db.String(20), nullable=False)
    device = db.Column(db.String(20), nullable=False)
    server_id = db.Column(db.Integer, index=True, nullable=False)
    switch_id = db.Column(db.Integer, index=True, nullable=False)
    switch_port = db.Column(db.Integer)
    def __repr__(self):
        return '<Ip_info %r>' % self.ip

class Server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.Integer)
    manufacturers = db.Column(db.String(50), index=True, nullable=False)
    manufacture_date = db.Column(db.Date)
    server_type = db.Column(db.String(20))
    st = db.Column(db.String(60), index=True)
    assets_no = db.Column(db.String(60))
    idc_id = db.Column(db.Integer)
    cabinet_id = db.Column(db.Integer)
    cabinet_pos = db.Column(db.String(10))
    expire = db.Column(db.Date)
    ups = db.Column(db.Integer)
    parter = db.Column(db.String(50))
    parter_type = db.Column(db.String(50))
    server_up_time = db.Column(db.Date)
    os_type = db.Column(db.String(20))
    os_version = db.Column(db.String(10))
    hotname = db.Column(db.String(32), index=True, nullable=False)
    inner_ip = db.Column(db.String(32), index=True, nullable=False)
    mac_address = db.Column(db.String(32))
    ip_info = db.Column(db.String(300))
    server_cpu = db.Column(db.String(250))
    server_disk = db.Column(db.String(250))
    server_mem = db.Column(db.String(250))
    raid = db.Column(db.String(10))
    raid_card_type = db.Column(db.String(50))
    remote_card = db.Column(db.String(32))
    remote_cardip = db.Column(db.String(32))
    status = db.Column(db.Integer, index=True)
    remark = db.Column(db.Text)
    last_op_time = db.Column(db.DateTime)
    last_op_people = db.Column(db.Integer)
    monitor_mail_group = db.Column(db.String(32))
    service_id = db.Column(db.Integer)
    server_purpose = db.Column(db.Integer)
    trouble_resolve = db.Column(db.Integer)
    op_interface_other = db.Column(db.Integer)
    dev_interface = db.Column(db.Integer)
    check_update_time = db.Column(db.DateTime)
    vm_status = db.Column(db.Integer, index=True, nullable=False)
    power = db.Column(db.Integer)
    host = db.Column(db.Integer, default = 0, index=True)
    def __repr__(self):
        return '<Server %r>' % self.st

class Switch(db.Model):
    __tablename__ = 'switch'
    id = db.Column(db.Integer, primary_key=True)
    switch_name = db.Column(db.String(50), nullable=False)
    switch_type = db.Column(db.String(50), nullable=False)
    manager_ip = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    idc_id = db.Column(db.Integer)
    cabinet_id = db.Column(db.Integer)
    status = db.Column(db.Integer)
    expire = db.Column(db.Date)
    remark = db.Column(db.Text)
    manufacturers = db.Column(db.Integer)
    last_op_time = db.Column(db.Date)
    last_op_people = db.Column(db.Integer)
    switch_port_nums = db.Column(db.Integer)
    def __repr__(self):
        return '<Switch %r>' % self.switch_name

if __name__ == "__main__":
    manager.run()


