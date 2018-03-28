#encoding=utf-8
import unittest,os,requests,json
from db_fixture import test_data

class AddGuestTest(unittest.TestCase):
    '''添加发布会'''
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/api/add_guest/'

    def test_add_guest_all_null(self):
        '''所有参数为空'''
        payload={'eid':'','realname':'','phone':'','email':''}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        #print (r.json())
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')
    def test_add_guest_eid_not_exist(self):
        '''eid不存在'''
        payload={'eid':100,'realname':'deby','phone':'14000000001','email':'deby@qq.com'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'event id null')

    def test_add_guest_event_not_active(self):
        '''活动未激活'''
        payload={'eid':3,'realname':'deby','phone':'14000000001','email':'deby@qq.com'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],10023)
        self.assertEqual(self.result['message'],'event status is not available')
    def test_add_guest_event_full(self):
        '''活动人满了'''
        payload={'eid':5,'realname':'jack','phone':'14000000002','email':'jack@qq.com'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],10024)
        self.assertEqual(self.result['message'],'event number is full')

    def test_add_guest_event_over(self):
        '''活动结束了'''
        payload={'eid':6,'realname':'jack','phone':'14000000003','email':'jack@qq.com'}
        r=requests.post(self.base_url,data=payload)
        #print (r.json())
        self.result=r.json()
        self.assertEqual(self.result['status'],10025)
        self.assertEqual(self.result['message'],'event has started')

    def test_add_guest_phone_repeat(self):
        '''手机号重复'''
        payload={'eid':1,'realname':'jack','phone':'13588881234','email':'jack@qq.com'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],10026)
        self.assertEqual(self.result['message'],'the event guest phone number repeat')

    def test_add_guest_success(self):
        '''添加成功'''
        payload={'eid':1,'realname':'张富贵','phone':'14000000001','email':'zhang@qq.com'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'add guest success')
    def tearDown(self):
        print (self.result)

if __name__=='__main__':
    test_data.init_data()
    unittest.main()
