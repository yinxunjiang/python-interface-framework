#encoding=utf-8
import unittest,os,requests
from db_fixture import test_data

class AddEventTest(unittest.TestCase):
    '''添加发布会'''
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/api/add_event/'

    def test_add_event_all_null(self):
        '''所有参数为空'''
        payload={'eid':'','name':'','limit':'','address':'','start_time':''}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error!')
    def test_add_event_eid_exist(self):
        '''id已经存在'''
        payload={'eid':1,'name':'嘿嘿嘿发布会','limit':200,'address':'中关村','start_time':'2018-5-1 12:00:00'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'event id already exists')
    def test_add_event_name_exist(self):
        '''名称已经存在'''
        payload={'eid':6,'name':'红米发布会','limit':200,'address':'中关村','start_time':'2018-5-1 12:00:00'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],10023)
        self.assertEqual(self.result['message'],'event name already exists')
    def test_add_event_data_type_error(self):
        '''日期格式错误'''
        payload={'eid':7,'name':'苹果发布会','limit':200,'address':'中关村','start_time':'2018'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],10024)
        self.assertIn('start_time format error.',self.result['message'])
    def test_add_event_success(self):
        '''添加成功'''
        payload={'eid':6,'name':'红米100发布会','limit':200,'address':'中关村','start_time':'2018-5-1 12:00:00'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],2001)
        self.assertEqual(self.result['message'],'add event success')
    def tearDown(self):
        print (self.result)

if __name__=='__mian__':
    test_data.init_data()
    unittest.main()
