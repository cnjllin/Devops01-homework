#/usr/bin/env python
#_*_coding:utf8_*_
class User(db.Model):
	'''
		用户信息表
			用户名，拼音 
			用户名，中文 
			邮件 
			所在部门
			是否是 leader 0不是、1是
	'''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=True)
    username = db.Column(db.String(50),nullable=True)
    email = db.Column(db.String(50),nullable=True)
    department_id = db.Column(db.Integer,index=True)
    is_leader = db.Column(db.Integer,index=True,default=0)
    def __repr__(self):
        return '<User % r>' % self.name


class Idc(db.Model):
	'''
		IDC 信息表
			IDC 字母简称
			idc 名称（中文）
			IDC 详细地址
			客服电话
			实际机柜数
			合同机柜数
	'''
	__tablename__ = 'idc'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10),nullable=True)
	idc_name = db.Column(db.String(30),nullable=True)
	address = db.Column(db.String(255),nullable=True)
	phone = db.Column(db.String(15),nullable=True)
	rel_cabinet_num = db.Column(db.Integer,nullable=True)
	pact_cabinet_num = db.Column(db.Integer,nullable=True)
	def __repr__(self):
        return '<User % r>' % self.name


class Cabinet(db.Model):
	'''
		IDC 机柜信息表
			机柜名
			所处的机房(IDC信息表的ID)
			机柜功率 
	'''
	__tablename__ = 'cabinet'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10),nullable=True)
	idc_id = db.Column(db.Integer, index=True,nullable=True)
	power = db.Column(db.String(20))
	def __repr__(self):
        return '<User % r>' % self.name
		
class Manufacturers(db.Model):
	'''
		服务器制造商表
			制造商名称
	'''
	__tablename__ = 'manufacturers'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable=True)

class Supplier(db.Model):
	'''
		服务器供应商表
			服务器供应商名称
	'''
	__tablename__ = 'supplier'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100),nullable=True)

class ServerType(db.Model):
	'''
		服务器型号表
			型号
			制造商(服务器制造商表的ID)
	'''
	__tablename__ = 'servertype'
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(20),nullable=True)
	manufacturers_id = db.Column(db.Integer, index=True,nullable=True)

class Raid(db.Model):
	'''
		硬盘 raid 信息表
			Raid 信息（raid1、raid5）
	'''
	__tablename__ = 'raid'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20),nullable=True)

class RaidType(db.Model):
	'''
		Raid 卡型号信息表
			Raid 卡型号
	'''
	__tablename__ = 'raidtype'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable=True)
		
class Status(db.Model):
	'''
		服务器状态信息表
			服务器状态(上线、备机、坏)
	'''
	__tablename__ = 'status'
	id = db.Column(db.Integer, primary_key=True)	
	name = db.Column(db.String(20),nullable=True)

class Product(db.Model):
	'''
		业务线信息表
			业务/产品名

	'''
	__tablename__ = 'product'
	id = db.Column(db.Integer, primary_key=True)
	server_name = db.Column(db.String(20),nullable=True)

class Power(db.Model):
	'''
		电源功率信息表
			功率值
	'''
	__tablename__ = 'power'
	id = db.Column(db.Integer, primary_key=True)
	server_power = db.Column(db.String(20),nullable=True)

class Ip_Info(db.Model):
	'''
		ip 信息表
			IP 地址
			Mac 地址
			设备名
			所在服务器(服务器信息表ID)
			所在网络设备(交换机 id)
			所在端口(交换机端口)
	'''
	__tablename__ = 'ip_info'
	id = db.Column(db.Integer, primary_key=True)
	ip = db.Column(db.String(20),nullable=True)
	mac = db.Column(db.String(20),nullable=True)
	device = db.Column(db.String(20),nullable=True)
	server_id = db.Column(db.Integer, index=True,nullable=True)
	switch_id = db.Column(db.Integer, index=True,nullable=True)
	switch_port = db.Column(db.Integer,nullable=True)

class Server(db.Model):
	'''
		服务器信息表
			供应商(Supplier 表的id)
			制造商 
			出厂日期
			服务器类型
			sn号
			自定义资产号
			所属 idc 
			所在机柜
			机柜内位置
			机器上架日期 
			操作系统类型
			操作系统版本 
			主机名
			内网 
			mac地址
			IP信息
			cpu型号
			硬盘信息
			内存信息
			Raid级别
			RAID 卡型号 
			远程管理卡类型
			远程管理卡IP
			服务器状态
			备注
			故障处理人(User 表的 id)
			上次检测时间
			是否是虚拟机
			电源功率(power表的id)
			宿主机(Server表vm_status的id，默认1)
	'''
	__tablename__ = 'server'
	id = db.Column(db.Integer, primary_key=True)
	supplier = db.Column(db.Integer, index=True)
	manufacturers = db.Column(db.String(50), index=True,nullable=True)
	server_type = db.Column(db.String(20))
	st = db.Column(db.String(60),index=True)
	assets_no = db.Column(db.String(60))
	idc_id = db.Column(db.Integer, index=True)
	cabinet_id = db.Column(db.Integer)
	cabinet_pos = db.Column(db.String(10))
	server_up_time = db.Column(db.Date)
	os_type = db.Column(db.String(20))
	os_version = db.Column(db.String(10))
	hostname = db.Column(db.String(32), index=True,nullable=True)
	inner_ip = db.Column(db.String(32), index=True,nullable=True)
	ip_info = db.Column(db.String(300))
	server_cpu = db.Column(db.String(250))
	server_disk = db.Column(db.String(250))
	server_mem = db.Column(db.String(250))
	raid = db.Column(db.String(10))
	raid_card_type = db.Column(db.String(10))
	remote_card = db.Column(db.String(32))
	remote_cardip = db.Column(db.String(32))
	status = db.Column(db.Integer, index=True)
	cabinet_id = db.Column(db.Integer, index=True)
	status = db.Column(db.Integer, index=True)
	remark = db.Column(db.Text)
	trouble_resolve = db.Column(db.Integer)
	check_update_time = db.Column(db.DateTime)
	vm_status = db.Column(db.Integer, index=True,nullable=True)
	power = db.Column(db.Integer)
	host = db.Column(db.Integer,index=True,default=1)

class Switch(db.Model):
	'''
		网络设备信息表
			网络设备名
			网络设备型号
			管理IP
			所在 IDC
			所在机柜
			状态
			备注
			端口数
	'''
	__tablename__ = 'switch'
	id = db.Column(db.Integer, primary_key=True)
	switch_name = db.Column(db.String(60),nullable=True)
	switch_type = db.Column(db.String(60),nullable=True)
	manager_ip = db.Column(db.String(60),nullable=True)
	idc_id = db.Column(db.Integer, index=True)
	cabinet_id = db.Column(db.Integer, index=True)
	status = db.Column(db.Integer, index=True)
	remark = db.Column(db.Text)
	switch_port_nums = db.Column(db.Integer)

		

