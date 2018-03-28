#encoding=utf-8
from pymysql import  connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
#-----读取db_config.ini设置-----#
base_dir=os.path.dirname(os.path.dirname(__file__))
file_path=os.path.join(base_dir,'db_config.ini')
#print (file_path)
cf=cparser.ConfigParser()
cf.read(file_path)
host=cf.get('mysqlconf','host')
port=cf.get('mysqlconf','port')
db=cf.get('mysqlconf','db')
user=cf.get('mysqlconf','user')
password=cf.get('mysqlconf','password')
charset=cf.get('mysqlconf','charset')
#-----封装MySQL基本操作---------#
class DB(object):
    def __init__(self):
        try:#连接数据库
            self.conn=connect(host=host,
                              user=user,
                              password=password,
                              db=db,
                              charset=charset,
                              cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print ("Mysql Error %d:%s"%(e.args[0],e.args[1]))
    #清除表数据
    def clear(self,table_name):
        real_sql='delete from '+table_name+';'
        #print (real_sql)
        with self.conn.cursor() as cursor:
            cursor.execute('set foreign_key_checks=0;')
            cursor.execute(real_sql)
        self.conn.commit()
    #插入表数据
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key]="'"+str(table_data[key])+"'"
        key=','.join(table_data.keys())
        value=','.join(table_data.values())
        real_sql="insert into "+table_name+"("+key+") values("+value+");"
        # print (real_sql)
        # print (key)
        # print (value)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()
    #关闭数据库连接
    def close(self):
        self.conn.close()

if __name__=='__main__':
    db=DB()
    table_name='sign_event'
    data={'id':2,'name':'苹果发布会','status':1,'`limit`':200,'address':'人民大会堂','start_time':'2018-04-01 12:00:00'}
    db.clear(table_name)
    #db.insert(table_name,data)
    db.close()
