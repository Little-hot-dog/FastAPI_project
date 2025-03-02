from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func

from typing import List, Dict

class RawData(Base):
    __tablename__ = "raw_data" #Название таблицы

    id = Column(Integer, primary_key=True, index=True) #index=True - позволяет искать по данному параметру
    host = Column(String, index=True)
    data = Column(JSON)
    time_date = Column(DateTime(timezone=True), server_default=func.now())

class SystemInfo(Base):
    __tablename__ = "system_info"  # Название таблицы

    id = Column(Integer, primary_key=True, index=True)
    host = Column(String, index=True)
    param = Column(String, index=True)
    value = Column(String, index=True)



    # osver = Column(String)  # A
    # dhcp_addr = Column(String)#A В списке от Артема был указан как "addr"
    # kav_ver = Column(String)  #A
    # kav_base = Column(String)  # A
    # ufw_on = Column(String)  #A
    # ufw_rules = Column(String)  #L
    # shares = Column(String)  # A
    # samba = Column(String)  # L
    # pw_rules = Column(String)  # L
    # pw_deny = Column(String)  #L
    # ssh_root = Column(String)  #LI
    # ssh_allow = Column(String)  #L
    # sudo_pw = Column(String)  #A
    # pw_empty = Column(String)  #L
    # syn = Column(String)  #L
    # ipv6 = Column(String)  #A
    # telnet = Column(String)  #L
    # r7_ver = Column(String)  # A
    # last_in = Column(String)  #L
    # last_out = Column(String)  #L
    # dns = Column(String)  #A
    # cdrom = Column(String)  #A
    # pw_limit = Column(String)  #A
    # pw_days = Column(String)  #A
    # pw_change = Column(String)  #A
    # last_boot = Column(String)  #A
    # board = Column(String)  #A
    # cpu = Column(String)  #A
    # mac = Column(String)  #A
    # mem = Column(JSON)  #A
    # noautorun = Column(String)  # W
    # kav_srv = Column(String)  #A
    # sysdisk= Column(String)  #W
    # pdisk = Column(JSON)  #A
    # lan = Column(JSON)  #A
    # kav_svc = Column(String)  #A
    # indsvc = Column(String)  #W
    # userlogf = Column(String)  #A
    # la = Column(String)  #W
    # pwdlimit_ad= Column(String)  #W
    # pwdlast = Column(String)  #W
    # inet = Column(String)  #A
    # crypto = Column(String)  #A
    # zip = Column(String)  #W
    # adobe = Column(String)  #W
    # lua = Column(String)  #W
    # root_size = Column(String)  #L
    # root_free = Column(String)  #A
    # kaa_ver = Column(String)  #A
    # kav_scan = Column(String)  #A
    # kaa_svc = Column(String)  #A
    # policy = Column(String)  #A
    # ssh = Column(String)  #L
    # ldiskc = Column(String)  #W
    # pkg_upg = Column(String)  #L
    # r7_org = Column(String)  #L
    # litoria = Column(String)  #L
    # kernel = Column(String)  #L
    # ad_join = Column(String)  #L
    # libre = Column(String)  #L
    # wine = Column(String)  #L
    # yandex = Column(String)  #L
    # vkteams = Column(String)  #L
    # firefox = Column(String)  #L
    # scrn = Column(String)  #A







