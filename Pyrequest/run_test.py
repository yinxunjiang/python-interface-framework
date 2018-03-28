#encoding=utf-8
import time,sys,unittest,os
from db_fixture import test_data
from HTMLTestRunner import HTMLTestRunner
#from test_HTMLTestRunner import HTMLTestRunner
dir_path=os.path.dirname(__file__)
interface_path=os.path.join(dir_path,'interface')
#print (interface_path)
discover=unittest.defaultTestLoader.discover(interface_path,'*_test.py')

if __name__=="__main__":
    test_data.init_data()
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./report/'+now+'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='发布会管理系统接口测试',description='Implementation Example with:')
    runner.run(discover)
    fp.close()



