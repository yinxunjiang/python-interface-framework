#encoding=utf-8
import sys
#sys.path.append('../db_fixture')
from db_fixture.mysql_db import DB

#创建测试数据
datas={
    #发布会数据
    'sign_event':[
        {'id':1,'name':'红米发布会','`limit`':1000,'status':1,'address':'北京会展中心','start_time':'2018-05-01 14:00:00'},
        {'id':2,'name':'黑米发布会','`limit`':0,'status':1,'address':'北京会展中心','start_time':'2018-05-01 14:00:00'},
        {'id':3,'name':'白米发布会','`limit`':1000,'status':0,'address':'北京会展中心','start_time':'2018-05-01 14:00:00'},
        {'id':4,'name':'黄米发布会','`limit`':1000,'status':1,'address':'北京会展中心','start_time':'2016-05-01 14:00:00'},
        {'id':5,'name':'紫米发布会','`limit`':2,'status':1,'address':'北京会展中心','start_time':'2018-06-01 14:00:00'},
        {'id':6,'name':'绿米发布会','`limit`':200,'status':1,'address':'北京会展中心','start_time':'2018-03-01 14:00:00'},
                  ],
    #嘉宾表数据
    'sign_guest':[
        {'id':1,'realname':'Alen','phone':13588881234,'email':'alen@qq.com','sign':0,'event_id':1},
        {'id':2,'realname':'Blen','phone':13588881235,'email':'blen@qq.com','sign':1,'event_id':1},
        {'id':3,'realname':'Clen','phone':13588881235,'email':'clen@qq.com','sign':0,'event_id':5},
        {'id':4,'realname':'Dlen','phone':13588881236,'email':'dlen@qq.com','sign':0,'event_id':5},
    ]
}

#将测试数据插入表
def init_data():
    db=DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()

if __name__=="__main__":
    init_data()
