#coding=utf8
import unittest,time
from common_modules import *
from selenium import webdriver
from pages import *


class test_Back_End_Maoyan(unittest.TestCase):

    u''' 实现后台冒烟测试，主要验证线上环境各个账户在后台能否正常登陆，且各个功能页面能否正常打开   '''  
    def setUp(self):
        utils.init2(self)
        
        self.tmk_user_name = "zhangjianli"
        self.tmk_user_password = "zhangjianli2015"
        
        self.cr_user_name = "zhaowenli"
        self.cr_user_password = "123abc"
        
        self.cc_user_name = "wangyuntao"
        self.cc_user_password = "luck19123732"
        
        self.is_user_name = "zhaizhao"
        self.is_user_password = "zhaizhao2015"
        
        self.pt_user_name = "yushiying"
        self.pt_user_password = "Gshiying916"
        
    def test_TMK_case_1(self):
        u''' 测试线上tmk账户  " 客户管理 ——> 推荐老师管理 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"推荐老师")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"老师推荐管理":
                result = True
            else:
                result = False
                self.log.error("tmk user teacher_recommend_manage_page open fail ...")
                utils.get_shot_image(driver, "tmk_teacher_recommend_manage_page_error")
        except:
            result = False
        
        self.assertTrue(result, "tmk user teacher_recommend_manage_page open fail ...") 
            
    def test_TMK_case_2(self):
        u''' 测试线上tmk账户  " 客户管理 ——> 添加学员（聚划算） "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"添加学员（聚划算）")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"添加学生":
                result = True
            else:
                result = False
                self.log.error("tmk user add_student_page open fail ...")
                utils.get_shot_image(driver, "tmk_add_student_page_error")
        except:
            result = False
        
        self.assertTrue(result, "tmk user add_student_page open fail ...") 
    
    def test_TMK_case_3(self):
        u''' 测试线上tmk账户  " 客户管理 ——> student list "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"student list")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"会员检索":
                result = True
            else:
                result = False
                self.log.error("tmk user student_list_page open fail ...")
                utils.get_shot_image(driver, "tmk_student_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "tmk user student_list_page open fail ...") 
    
    def test_TMK_case_4(self):
        u''' 测试线上tmk账户  " 销售管理 ——> 问题列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"问题列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"":
                result = True
            else:
                result = False
                self.log.error("tmk user question_list_page open fail ...")
                utils.get_shot_image(driver, "tmk_question_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "tmk user question_list_page open fail ...")   

    def test_TMK_case_5(self):
            u''' 测试线上tmk账户  " 销售管理 ——> 学生列表 "页面打开是否正常   '''
            #登录后台系统
            login_page = login.Login()
            self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
            
            #窗口最大化，然后switch到topFrame
            default_page = default.Default(self.driver)
            default_page.select_top_module(u"销售管理")
            driver = default_page.select_left_module(u"学生列表")
            time.sleep(2)
            
            try:
                table_name = utils.find_css(driver, "tr > th[class='table_title']").text
                print "table_name --->",table_name
                if table_name == u"会员检索":
                    result = True
                else:
                    result = False
                    self.log.error("tmk user student_list_page open fail ...")
                    utils.get_shot_image(driver, "tmk_student_list_page_error")
            except:
                result = False
            
            self.assertTrue(result, "tmk user student_list_page open fail ...")   

    def test_TMK_case_6(self):
        u''' 测试线上tmk账户  " 销售管理 ——> sales2.0转1.0 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"sales2.0转1.0")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"根据用户id 或 手机号 删除对应信息":
                result = True
            else:
                result = False
                self.log.error("tmk user tm_sale_2.0_to_1.0_page open fail ...")
                utils.get_shot_image(driver, "tmk_sale_2.0_to_1.0_page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user sale_2.0_to_1.0_page open fail ...")

    def test_TMK_case_7(self):
        u''' 测试线上tmk账户  " 销售管理 ——> 注册未体验用户列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"注册未体验用户列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("tmk user tm_registed_but_no_experience_page open fail ...")
                utils.get_shot_image(driver, "tmk_registed_but_no_experience_page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user registed_but_no_experience_page open fail ...")
    
    def test_TMK_case_8(self):
        u''' 测试线上tmk账户  " 销售管理 ——> TMK Sales2.0数据报表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"TMK Sales2.0数据报表")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"搜 索":
                result = True
            else:
                result = False
                self.log.error("tmk user tm_sale2.0_data_page open fail ...")
                utils.get_shot_image(driver, "tmk_sale2.0_data_page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user sale2.0_data_page open fail ...")   
    
    def test_TMK_case_9(self):
        u''' 测试线上tmk账户  " 销售管理 ——> 体验课来源 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"体验课来源")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False 
                self.log.error("tmk user tm_experience_class_source_page open fail ...")
                utils.get_shot_image(driver, "tmk_experience_class_source_page_error")   
        except:
            result = False
               
        self.assertTrue(result, "tmk user experience_class_source_page open fail ...")
    
    def test_TMK_case_10(self):
        u''' 测试线上tmk账户  " 销售管理 ——> TM代约课列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"TM代约课列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("tmk user tm_appoint_class_page open fail ...")
                utils.get_shot_image(driver, "tmk_tm_appoint_class_page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user tm_appoint_class_page open fail ...")
            
    def test_TMK_case_11(self):
        u''' 测试线上tmk账户  " 销售管理 ——> 体验店跟进详情页面 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"体验店跟进详情页面")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("tmk user experience_shop_follow_detail_page open fail ...")
                utils.get_shot_image(driver, "tmk_experience_shop_follow_detail_page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user experience_shop_follow_detail_page open fail ...")
            
    def test_TMK_case_12(self):
        u''' 测试线上tmk账户  " 销售管理 ——> 体验店来源分配TM "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"体验店来源分配TM")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"筛选项":
                result = True
            else:
                result = False
                self.log.error("tmk user experience_shop_source_arrange_page open fail ...")
                utils.get_shot_image(driver, "tmk_experience_shop_source_arrange_page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user experience_shop_source_arrange_page open fail ...")

    def test_TMK_case_13(self):
        u''' 测试线上tmk账户  " 销售管理 ——> 联通待处理数据 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"联通待处理数据")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("tmk user unicom_data_wait_for_deal_page open fail ...")
                utils.get_shot_image(driver, "tmk_unicom_data_wait_for_deal_page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user unicom_data_wait_for_deal_page open fail ...")
            
    def test_TMK_case_14(self):
        u''' 测试线上tmk账户  " 销售管理 ——> 导入联通数据 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"导入联通数据")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("tmk user insert_into_unicom_data_page open fail ...")
                utils.get_shot_image(driver, "tmk_insert_into_unicom_data_page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user insert_into_unicom_data_page open fail ...")
            
    def test_TMK_case_15(self):
        u''' 测试线上tmk账户  " 销售管理 ——> TM转化统计 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"TM转化统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("tmk user tm_change_to_page open fail ...")
                utils.get_shot_image(driver, "tmk_tm_change_to_page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user tm_change_to_page open fail ...")
            
    def test_TMK_case_16(self):
        u''' 测试线上tmk账户  " 销售管理 ——> TM排班 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"TM排班")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"邀约客服排班":
                result = True
            else:
                result = False
                self.log.error("tmk user tm_arrange_class_page open fail ...")
                utils.get_shot_image(driver, "tmk_tm_arrange_class__page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user tm_arrange_class_page open fail ...")
    
    def aaaaaaaatest_TMK_case_16(self):
        u''' 测试线上tmk账户  " 销售管理 ——> 51talk通讯录 "页面打开是否正常   
                                这个模块比较特殊，因为三级菜单名称和二级菜单名称一样，所以需要特殊处理   或者  将其两者修改成不一样
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"51talk通讯录")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"公司人员列表":
                result = True
            else:
                result = False
                self.log.error("tmk user 51talk_telephone_book_page open fail ...")
                utils.get_shot_image(driver, "tmk_51talk_telephone_book__page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user 51talk_telephone_book_page open fail ...")
            
    def test_TMK_case_17(self):
        u''' 测试线上tmk账户  " 销售管理 ——> 电子名片 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"电子名片")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"公司人员列表":
                result = True
            else:
                result = False
                self.log.error("tmk user e-card_page open fail ...")
                utils.get_shot_image(driver, "tmk_e-card__page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user e-card_page open fail ...")
    
    def test_TMK_case_18(self):
        u''' 测试线上tmk账户  " 客服管理 ——> 取消课程统计 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"取消课程统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("tmk user cancel_class_count_page open fail ...")
                utils.get_shot_image(driver, "tmk_cancel_class_count__page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user cancel_class_count_page open fail ...")
    
    def test_TMK_case_19(self):
        u''' 测试线上tmk账户  " 系统设置管理 ——> change password "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.tmk_user_name,passwd=self.tmk_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"系统设置管理")
        driver = default_page.select_left_module(u"change password")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Change Password":
                result = True
            else:
                result = False
                self.log.error("tmk user change_password_page open fail ...")
                utils.get_shot_image(driver, "tmk_change_password__page_error")
        except:
            result = False
            
        self.assertTrue(result, "tmk user change_password_page open fail ...")
        
        
    def test_CR_case_1(self):
        u''' 测试线上cr账户  " 客户管理 ——> 每周发送老师数据 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"每周发送老师数据")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"每周自动发送老师评价数据":
                result = True
            else:
                result = False
                self.log.error("CR user send_to_teacher_data_per_week_page open fail ...")
                utils.get_shot_image(driver, "CR_send_to_teacher_data_per_week_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user send_to_teacher_data_per_week_page open fail ...")
            
    def test_CR_case_2(self):
        u''' 测试线上cr账户  " 客户管理 ——> 未成功验证手机号列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"未成功验证手机号列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"无法验证手机号用户列表":
                result = True
            else:
                result = False
                self.log.error("CR user not_success_verify_phone_number_list_page open fail ...")
                utils.get_shot_image(driver, "CR_not_success_verify_phone_number_list_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user not_success_verify_phone_number_list_page open fail ...")
            
    def test_CR_case_3(self):
        u''' 测试线上cr账户  " 客户管理 ——> 学生等级证书 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"学生等级证书")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"搜索 从2013-09-24 开始":
                result = True
            else:
                result = False
                self.log.error("CR user student_level_certificate_page open fail ...")
                utils.get_shot_image(driver, "CR_student_level_certificate_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user student_level_certificate_page open fail ...")
    
    def test_CR_case_4(self):
        u''' 测试线上cr账户  " 客户管理 ——> 添加学员（聚划算） "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"添加学员（聚划算）")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"添加学生":
                result = True
            else:
                result = False
                self.log.error("CR user add_student_page open fail ...")
                utils.get_shot_image(driver, "CR_add_student_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user add_student_page open fail ...")
            
    def test_CR_case_5(self):
        u''' 测试线上cr账户  " 客户管理 ——> student list "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"student list")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"会员检索":
                result = True
            else:
                result = False
                self.log.error("CR user student_list_page open fail ...")
                utils.get_shot_image(driver, "CR_student_list_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user student_list_page open fail ...")
    
    def test_CR_case_6(self):
        u''' 测试线上cr账户  " 销售管理 ——> 问题列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"问题列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"":
                result = True
            else:
                result = False
                self.log.error("CR user question_list_page open fail ...")
                utils.get_shot_image(driver, "CR_question_list_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user question_list_page open fail ...")
            
    def test_CR_case_7(self):
        u''' 测试线上cr账户  " 销售管理 ——> 学生列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"学生列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"会员检索":
                result = True
            else:
                result = False
                self.log.error("CR user student_list_page open fail ...")
                utils.get_shot_image(driver, "CR_student_list_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user student_list_page open fail ...")
        
    def test_CR_case_8(self):
        u''' 测试线上cr账户  " 销售管理 ——> 短息记录查询 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"短息记录查询")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"建议搜索":
                result = True
            else:
                result = False
                self.log.error("CR user message_record_search_page open fail ...")
                utils.get_shot_image(driver, "CR_message_record_search_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user message_record_search_page open fail ...")
         
    def test_CR_case_9(self):
        u''' 测试线上cr账户  " 销售管理 ——> 建议列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"建议列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"建议搜索":
                result = True
            else:
                result = False
                self.log.error("CR user advice_list_page open fail ...")
                utils.get_shot_image(driver, "CR_advice_list_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user advice_list_page open fail ...")
        
    def test_CR_case_10(self):
        u''' 测试线上cr账户  " 销售管理 ——> 个人信息 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"个人信息")
        time.sleep(2)
        
        try:
            page_content = utils.find_css(driver, "html > body").text
            print "page_content --->",page_content
            if page_content == u"您所在的组没有开启CRM用户信息收集，请联系管理员！":
                result = True
            else:
                result = False
                self.log.error("CR user personal_info_page open fail ...")
                utils.get_shot_image(driver, "CR_personal_info_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user personal_info_page open fail ...")
 
    def test_CR_case_11(self):
        u''' 测试线上cr账户  " 销售管理 ——> 推荐好友送课 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"推荐好友送课")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"按条件搜索：":
                result = True
            else:
                result = False
                self.log.error("CR user recommend_friend_and_get_class_page open fail ...")
                utils.get_shot_image(driver, "CR_recommend_friend_and_get_class_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user recommend_friend_and_get_class_page open fail ...")
                  
    def test_CR_case_12(self):
        u''' 测试线上cr账户  " 客服管理 ——> 投诉老师统计 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"投诉老师统计")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"Search":
                result = True
            else:
                result = False
                self.log.error("CR user complaint_teacher_count_page open fail ...")
                utils.get_shot_image(driver, "CR_complaint_teacher_count_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user complaint_teacher_count_page open fail ...")
                        
    def test_CR_case_13(self):
        u''' 测试线上cr账户  " 客服管理 ——> 取消课程统计 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"取消课程统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CR user cancel_class_count_page open fail ...")
                utils.get_shot_image(driver, "CR_cancel_class_count_page_error")
        except:
            result = False
            
        self.assertTrue(result, "CR user cancel_class_count_page open fail ...")
            
    def test_CR_case_14(self):
        u''' 测试线上cr账户  " 客服管理 ——> 送课历史记录 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"送课历史记录")
        time.sleep(2)

        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"统计条件":
                result = True
            else:
                result = False
                self.log.error("CR user give_free_class_history_record_page open fail ...")
                utils.get_shot_image(driver, "CR_give_free_class_history_record_page_error")
        except:
            result = False
        self.assertTrue(result, "CR user give_free_class_history_record_page open fail ...")
        
    def test_CR_case_15(self):
        u''' 测试线上cr账户  " 客服管理 ——> 服务跟进列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"服务跟进列表")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "button[type='submit']").text
            print "search_button_text --->",search_button_text
            if search_button_text == u"搜索":
                result = True
            else:
                result = False
                self.log.error("CR user service_follow_list_page open fail ...")
                utils.get_shot_image(driver, "CR_service_follow_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user service_follow_list_page open fail ...")
            
    def test_CR_case_16(self):
        u''' 测试线上cr账户  " 客服管理 ——> 用户投诉管理 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"用户投诉管理")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"Search":
                result = True
            else:
                result = False
                self.log.error("CR user user_complain_manage_page open fail ...")
                utils.get_shot_image(driver, "CR_user_complain_manage_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user user_complain_manage_page open fail ...")
      
    def test_CR_case_17(self):
        u''' 测试线上cr账户  " 客服管理 ——> 学员预约详情修改 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"学员预约详情修改")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='bg_tr']").text
            print "table_name --->",table_name
            if table_name == u"student filter":
                result = True
            else:
                result = False
                self.log.error("CR user student_appoint_detail_change_page open fail ...")
                utils.get_shot_image(driver, "CR_student_appoint_detail_change_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user student_appoint_detail_change_page open fail ...")

    def test_CR_case_18(self):
        u''' 测试线上cr账户  " 客服管理 ——> 客户服务 "页面打开是否正常   
                                因二级菜单名称  和  三级菜单名称  相同     所以此处做了特殊处理
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        frameset = utils.find_id(self.driver,"frame")
        left_frame = utils.find_name(frameset,"leftFrame")
        self.driver.switch_to_frame(left_frame)
        
        self.driver.implicitly_wait(20)
        utils.finds_link_text(self.driver, u"客户服务")[1].click()
        self.driver.implicitly_wait(5)
        
        #同理二次定位到rightFrame模块，然后switch到rightFrame
        self.driver.switch_to_default_content()
        frameset = utils.find_id(self.driver,"frame")
        right_frame = utils.find_id(frameset,"rightframe")
        self.driver.switch_to_frame(right_frame)
        time.sleep(2)
        
        try:
            table_name = utils.find_css(self.driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"筛选":
                result = True
            else:
                result = False
                self.log.error("CR user customer_service_page open fail ...")
                utils.get_shot_image(self.driver, "CR_customer_service_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user customer_service_page open fail ...")    

    def test_CR_case_19(self):
        u''' 测试线上cr账户  " 客服管理 ——> 客户服务明细 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"客户服务明细")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[align='left']").text
            print "table_name --->",table_name
            if table_name == u"Search":
                result = True
            else:
                result = False
                self.log.error("CR user customer_service_detail_page open fail ...")
                utils.get_shot_image(driver, "CR_customer_service_detail_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user customer_service_detail_page open fail ...")
  
    def test_CR_case_20(self):
        u''' 测试线上cr账户  " 客服管理 ——> 推荐老师 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"推荐老师")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"teacher filter":
                result = True
            else:
                result = False
                self.log.error("CR user recommend_teacher_page open fail ...")
                utils.get_shot_image(driver, "CR_recommend_teacher_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user recommend_teacher_page open fail ...")
        
    def aaaaaaaaaaaaaaaaatest_CR_case_21(self):
        u''' 测试线上cr账户  " 客服管理 ——> 低分课程页面 "页面打开是否正常   
                                页面打不开，显示空白页
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"低分课程页面")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"teacher filter":
                result = True
            else:
                result = False
                self.log.error("CR user low_point_class_page open fail ...")
                utils.get_shot_image(driver, "CR_low_point_class_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user low_point_class_page open fail ...")
        
    def test_CR_case_22(self):
        u''' 测试线上cr账户  " 客服管理 ——> 不活跃老师 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"不活跃老师")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"Search":
                result = True
            else:
                result = False
                self.log.error("CR user no_active_teacher_page open fail ...")
                utils.get_shot_image(driver, "CR_no_active_teacher_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user no_active_teacher_page open fail ...")
        
    def test_CR_case_23(self):
        u''' 测试线上cr账户  " 客服管理 ——> 课前联系 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"课前联系")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"筛选项":
                result = True
            else:
                result = False
                self.log.error("CR user contact_before_class_page open fail ...")
                utils.get_shot_image(driver, "CR_contact_before_class_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user contact_before_class_page open fail ...")
        
    def test_CR_case_24(self):
        u''' 测试线上cr账户  " 系统设置管理 ——> change password "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"系统设置管理")
        driver = default_page.select_left_module(u"change password")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Change Password":
                result = True
            else:
                result = False
                self.log.error("CR user change_password_page open fail ...")
                utils.get_shot_image(driver, "CR_change_password_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user change_password_page open fail ...")

    def test_CR_case_25(self):
        u''' 测试线上cr账户  " Ac管理 ——> 登录日志查询 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"Ac管理")
        driver = default_page.select_left_module(u"登录日志查询")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > td").text
            print "table_name --->",table_name
            if table_name == u"要查询的日期:":
                result = True
            else:
                result = False
                self.log.error("CR user search_login_log_page open fail ...")
                utils.get_shot_image(driver, "CR_search_login_log_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user search_login_log_page open fail ...")
        
    def test_CR_case_26(self):
        u''' 测试线上cr账户  " 中教管理 ——> 开班统计 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"中教")
        driver = default_page.select_left_module(u"开班统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"搜索":
                result = True
            else:
                result = False
                self.log.error("CR user open_class_count_page open fail ...")
                utils.get_shot_image(driver, "CR_open_class_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user open_class_count_page open fail ...")    
        
    def test_CR_case_27(self):
        u''' 测试线上cr账户  " 中教管理 ——> HBT班级查询 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"中教")
        driver = default_page.select_left_module(u"HBT班级查询")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"搜索":
                result = True
            else:
                result = False
                self.log.error("CR user HBT_class_count_page open fail ...")
                utils.get_shot_image(driver, "CR_HBT_class_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user HBT_class_count_page open fail ...")  
        
    def test_CR_case_28(self):
        u''' 测试线上cr账户  " Teacher Management ——> Follow LIst "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"Teacher Management")
        driver = default_page.select_left_module(u"Follow LIst")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CR user follow_list_page open fail ...")
                utils.get_shot_image(driver, "follow_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user follow_list_page open fail ...")
        
    def test_CR_case_29(self):
        u''' 测试线上cr账户  " Teacher Management ——> Sub Lesson Summary "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"Teacher Management")
        driver = default_page.select_left_module(u"Sub Lesson Summary")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CR user Sub_Lesson_Summary_page open fail ...")
                utils.get_shot_image(driver, "Sub_Lesson_Summary_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user Sub_Lesson_Summary_page open fail ...")    
        
    def test_CR_case_30(self):
        u''' 测试线上cr账户  " Teacher Management ——> 1.Daily Lessons "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"Teacher Management")
        driver = default_page.select_left_module(u"1.Daily Lessons")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "a > span").text
            print "table_name --->",table_name
            if table_name == u"HBT":
                result = True
            else:
                result = False
                self.log.error("CR user 1.Daily_Lessons_page open fail ...")
                utils.get_shot_image(driver, "1.Daily_Lessons_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user 1.Daily_Lessons_page open fail ...")
        
        
    def test_CR_case_31(self):
        u''' 测试线上cr账户  " Teacher Management ——> Daily_Lessons "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"Teacher Management")
        driver = default_page.select_left_module(u"Daily_Lessons")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "a > span").text
            print "table_name --->",table_name
            if table_name == u"HBT":
                result = True
            else:
                result = False
                self.log.error("CR user Daily_Lessons_page open fail ...")
                utils.get_shot_image(driver, "Daily_Lessons_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user Daily_Lessons_page open fail ...")
        
    def test_CR_case_32(self):
        u''' 测试线上cr账户  " Teacher Management ——> Daily Lesson "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cr_user_name,passwd=self.cr_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"Teacher Management")
        driver = default_page.select_left_module(u"Daily Lesson")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[align='left']").text
            print "table_name --->",table_name
            if table_name == u"  Filters":
                result = True
            else:
                result = False
                self.log.error("CR user Daily_Lesson_page open fail ...")
                utils.get_shot_image(driver, "Daily_Lesson_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CR user Daily_Lesson_page open fail ...")
        
    
    def test_CC_case_1(self):
        u''' 测试线上cc账户  " 销售管理 ——> 问题列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"问题列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"":
                result = True
            else:
                result = False
                self.log.error("CC user question_list_page open fail ...")
                utils.get_shot_image(driver, "question_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user question_list_page open fail ...")
        
    def test_CC_case_2(self):
        u''' 测试线上cc账户  " 销售管理 ——> 学生列表 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"学生列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"会员检索":
                result = True
            else:
                result = False
                self.log.error("CC user student_list_page open fail ...")
                utils.get_shot_image(driver, "student_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user student_list_page open fail ...")
        
    def test_CC_case_3(self):
        u''' 测试线上cc账户  " 销售管理 ——> 添加中教代金券 "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"添加中教代金券")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='td_bg']").text
            print "table_name --->",table_name
            if table_name == u"中教代金券类型":
                result = True
            else:
                result = False
                self.log.error("CC user add_zhongjiao_voucher_page open fail ...")
                utils.get_shot_image(driver, "add_zhongjiao_voucher_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user add_zhongjiao_voucher_page open fail ...")    
        
    def test_CC_case_4(self):
        u''' 测试线上cc账户  " 销售管理 ——> 待处理问题  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"待处理问题")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"Search":
                result = True
            else:
                result = False
                self.log.error("CC user wait_for_deal_question_page open fail ...")
                utils.get_shot_image(driver, "wait_for_deal_question_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user wait_for_deal_question_page open fail ...") 
        
    def test_CC_case_5(self):
        u''' 测试线上cc账户  " 销售管理 ——> 分级规则记录统计  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"分级规则记录统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"CC分级查询":
                result = True
            else:
                result = False
                self.log.error("CC user diff_level_role_record_count_page open fail ...")
                utils.get_shot_image(driver, "diff_level_role_record_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user diff_level_role_record_count_page open fail ...")
        
    def test_CC_case_6(self):
        u''' 测试线上cc账户  " 销售管理 ——> CC推荐学员  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"CC推荐学员")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CC user cc_recommoned_student_page open fail ...")
                utils.get_shot_image(driver, "cc_recommoned_student_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user cc_recommoned_student_page open fail ...")
        
    def test_CC_case_7(self):
        u''' 测试线上cc账户  " 销售管理 ——> 小金库  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"小金库")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CC user small_vault_page open fail ...")
                utils.get_shot_image(driver, "small_vault_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user small_vault_page open fail ...")
        
    def test_CC_case_8(self):
        u''' 测试线上cc账户  " 销售管理 ——> cc业绩排名  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"cc业绩排名")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CC user cc_result_ranking_page open fail ...")
                utils.get_shot_image(driver, "cc_result_ranking_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user cc_result_ranking_page open fail ...")
        
    def test_CC_case_9(self):
        u''' 测试线上cc账户  " 销售管理 ——> 公池选择客户  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"公池选择客户")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CC user gongchi_select_user_page open fail ...")
                utils.get_shot_image(driver, "gongchi_select_user_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user gongchi_select_user_page open fail ...")
        
    def test_CC_case_10(self):
        u''' 测试线上cc账户  " 销售管理 ——> follow list  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"follow list")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CC user follow_list_page open fail ...")
                utils.get_shot_image(driver, "follow_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user follow_list_page open fail ...")
        
    def test_CC_case_11(self):
        u''' 测试线上cc账户  " 销售管理 ——> 1.CC销售报表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"1.CC销售报表")
        time.sleep(2)
        
        try:
            today_button_text = utils.find_name(driver, "ben_day").get_attribute("value")
            print "today_button_text --->",today_button_text
            if today_button_text == u"今天":
                result = True
            else:
                result = False
                self.log.error("CC user cc_sale_report_page open fail ...")
                utils.get_shot_image(driver, "cc_sale_report_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user cc_sale_report_page open fail ...")
        
    def test_CC_case_12(self):
        u''' 测试线上cc账户  " 销售管理 ——> 2.CC通话报表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"2.CC通话报表")
        time.sleep(2)
        
        try:
            today_button_text = utils.find_name(driver, "ben_day").get_attribute("value")
            print "today_button_text --->",today_button_text
            if today_button_text == u"今天":
                result = True
            else:
                result = False
                self.log.error("CC user cc_phone_record_report_page open fail ...")
                utils.get_shot_image(driver, "cc_phone_record_report_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user cc_phone_record_report_page open fail ...")
        
    def test_CC_case_13(self):
        u''' 测试线上cc账户  " 销售管理 ——> 3.CC工作完成度  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"3.CC工作完成度")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CC user cc_work_accomplist_page open fail ...")
                utils.get_shot_image(driver, "cc_work_accomplist_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user cc_work_accomplist_page open fail ...")
        
    def test_CC_case_14(self):
        u''' 测试线上cc账户  " 销售管理 ——> 4.CC跟进及时度  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"4.CC跟进及时度")
        time.sleep(2)
        
        try:
            today_button_text = utils.find_name(driver, "ben_day").get_attribute("value")
            print "today_button_text --->",today_button_text
            if today_button_text == u"今天":
                result = True
            else:
                result = False
                self.log.error("CC user cc_follow_ontime_page open fail ...")
                utils.get_shot_image(driver, "cc_follow_ontime_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user cc_follow_ontime_page open fail ...")
        
    def test_CC_case_15(self):
        u''' 测试线上cc账户  " 销售管理 ——> 5.CC签单及时度  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"5.CC签单及时度")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"搜 索":
                result = True
            else:
                result = False
                self.log.error("CC user cc_success_order_ontime_page open fail ...")
                utils.get_shot_image(driver, "cc_success_order_ontime_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user cc_success_order_ontime_page open fail ...")
        
    def test_CC_case_16(self):
        u''' 测试线上cc账户  " 销售管理 ——> 挖宝排行榜  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"挖宝排行榜")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CC user get_treasure_ranking_page open fail ...")
                utils.get_shot_image(driver, "get_treasure_ranking_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user get_treasure_ranking_page open fail ...")
        
    def test_CC_case_17(self):
        u''' 测试线上cc账户  " 销售管理 ——> cc名下学员列表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"cc名下学员列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("CC user under_cc_student_list_page open fail ...")
                utils.get_shot_image(driver, "under_cc_student_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user under_cc_student_list_page open fail ...")
        
    def test_CC_case_18(self):
        u''' 测试线上cc账户  " 销售管理 ——> 藏金阁  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"藏金阁")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "submit").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"Search":
                result = True
            else:
                result = False
                self.log.error("CC user cangjinge_page open fail ...")
                utils.get_shot_image(driver, "cangjinge_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user cangjinge_page open fail ...")
        
    def test_CC_case_19(self):
        u''' 测试线上cc账户  " 销售管理 ——> 51talk通讯录  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        
        driver = self.driver
        #二次定位到leftFrame模块，然后switch到leftFrame
        frameset = utils.find_id(driver,"frame")
        left_frame = utils.find_name(frameset,"leftFrame")
        driver.switch_to_frame(left_frame)
        
        #WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_link_text("课程管理"), u'页面加载失败')
        driver.implicitly_wait(20)
        utils.finds_link_text(driver,u"51talk通讯录")[1].click()
        driver.implicitly_wait(5)
        
        #同理二次定位到rightFrame模块，然后switch到rightFrame
        driver.switch_to_default_content()
        frameset = utils.find_id(driver,"frame")
        right_frame = utils.find_id(frameset,"rightframe")
        driver.switch_to_frame(right_frame)
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "search_button_text --->",table_name
            if table_name == u"公司人员列表":
                result = True
            else:
                result = False
                self.log.error("CC user 51talk_telephone_book_page open fail ...")
                utils.get_shot_image(driver, "51talk_telephone_book_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user 51talk_telephone_book_page open fail ...")
        
    def test_CC_case_20(self):
        u''' 测试线上cc账户  " 销售管理 ——> 浏览订单  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"浏览订单")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "submit").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"查询":
                result = True
            else:
                result = False
                self.log.error("CC user view_order_page open fail ...")
                utils.get_shot_image(driver, "view_order_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user view_order_page open fail ...")
        
    def aaaaaaaaaaaaaatest_CC_case_21(self):
        u''' 测试线上cc账户  " 销售管理 ——> 电子名片  "页面打开是否正常   
                                该页面打不开，所以无法验证
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"电子名片")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "submit").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"查询":
                result = True
            else:
                result = False
                self.log.error("CC user view_order_page open fail ...")
                utils.get_shot_image(driver, "view_order_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user view_order_page open fail ...")
        
    def test_CC_case_22(self):
        u''' 测试线上cc账户  " 销售管理 ——> 处理订单  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"处理订单")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"search":
                result = True
            else:
                result = False
                self.log.error("CC user deal_order_page open fail ...")
                utils.get_shot_image(driver, "deal_order_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user deal_order_page open fail ...")
        
    def test_CC_case_23(self):
        u''' 测试线上cc账户  " 客服管理 ——> 推荐老师  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"推荐老师")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"teacher filter":
                result = True
            else:
                result = False
                self.log.error("CC user recommon_teacher_page open fail ...")
                utils.get_shot_image(driver, "recommon_teacher_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user recommon_teacher_page open fail ...")
        
    def test_CC_case_24(self):
        u''' 测试线上cc账户  " 系统设置管理 ——> change password  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.cc_user_name,passwd=self.cc_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"系统设置管理")
        driver = default_page.select_left_module(u"change password")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Change Password":
                result = True
            else:
                result = False
                self.log.error("CC user change_password_page open fail ...")
                utils.get_shot_image(driver, "change_password_page_error")
        except:
            result = False
        
        self.assertTrue(result, "CC user change_password_page open fail ...")
        
    def test_IS_case_1(self):
        u''' 测试线上is账户  " 销售管理 ——> 问题列表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"问题列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"":
                result = True
            else:
                result = False
                self.log.error("IS user question_list_page open fail ...")
                utils.get_shot_image(driver, "question_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user question_page open fail ...")
    
    def test_IS_case_2(self):
        u''' 测试线上is账户  " 销售管理 ——> 学生列表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"学生列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"会员检索":
                result = True
            else:
                result = False
                self.log.error("IS user student_list_page open fail ...")
                utils.get_shot_image(driver, "student_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user student_list_page open fail ...")
        
    def test_IS_case_3(self):
        u''' 测试线上is账户  " 销售管理 ——> 添加小额代金券  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"添加小额代金券")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='td_bg']").text
            print "table_name --->",table_name
            if table_name == u"代金券类型:":
                result = True
            else:
                result = False
                self.log.error("IS user add_little_vouchers_page open fail ...")
                utils.get_shot_image(driver, "add_little_vouchers_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user add_little_vouchers_page open fail ...")
        
    def test_IS_case_4(self):
        u''' 测试线上is账户  " 销售管理 ——> 添加中教代金券  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"添加中教代金券")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='td_bg']").text
            print "table_name --->",table_name
            if table_name == u"中教代金券类型":
                result = True
            else:
                result = False
                self.log.error("IS user add_zhongjiao_vouchers_page open fail ...")
                utils.get_shot_image(driver, "add_zhongjiao_vouchers_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user add_zhongjiao_vouchers_page open fail ...")
        
    def test_IS_case_5(self):
        u''' 测试线上is账户  " 销售管理 ——> 代金券申请列表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"代金券申请列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("IS user vouchers_apply_list_page open fail ...")
                utils.get_shot_image(driver, "vouchers_apply_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user vouchers_apply_list_page open fail ...")
        
    def test_IS_case_6(self):
        u''' 测试线上is账户  " 销售管理 ——> 待处理问题   "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"待处理问题")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"Search":
                result = True
            else:
                result = False
                self.log.error("IS user wait_for_deal_question_page open fail ...")
                utils.get_shot_image(driver, "wait_for_deal_question_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user wait_for_deal_question_page open fail ...")
        
    def test_IS_case_7(self):
        u''' 测试线上is账户  " 销售管理 ——> 建议列表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"建议列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"建议搜索":
                result = True
            else:
                result = False
                self.log.error("IS user advice_list_page open fail ...")
                utils.get_shot_image(driver, "advice_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user advice_list_page open fail ...")
        
    def test_IS_case_8(self):
        u''' 测试线上is账户  " 销售管理 ——> IS跟进列表(新)  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"IS跟进列表(新)")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("IS user is_follow_list(new)_page open fail ...")
                utils.get_shot_image(driver, "is_follow_list(new)_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user is_follow_list(new)_page open fail ...")
        
    def test_IS_case_9(self):
        u''' 测试线上is账户  " 销售管理 ——> IS跟进列表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"IS跟进列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("IS user is_follow_list_page open fail ...")
                utils.get_shot_image(driver, "is_follow_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user is_follow_list_page open fail ...")
        
    def test_IS_case_10(self):
        u''' 测试线上is账户  " 销售管理 ——> IS推荐会员  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"IS推荐会员")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("IS user is_recommon_user_page open fail ...")
                utils.get_shot_image(driver, "is_recommon_user_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user is_recommon_user_page open fail ...")
        
    def test_IS_case_11(self):
        u''' 测试线上is账户  " 销售管理 ——> 30天无跟进用户  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"30天无跟进用户")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"search":
                result = True
            else:
                result = False
                self.log.error("IS user 30days_no_follow_user_page open fail ...")
                utils.get_shot_image(driver, "30days_no_follow_user_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user 30days_no_follow_user_page open fail ...")
        
    def test_IS_case_12(self):
        u''' 测试线上is账户  " 销售管理 ——> IS业绩排名  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"IS业绩排名")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("IS user is_result_ranking_page open fail ...")
                utils.get_shot_image(driver, "is_result_ranking_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user is_result_ranking_page open fail ...")
        
    def test_IS_case_13(self):
        u''' 测试线上is账户  " 销售管理 ——> IS通话报表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"IS通话报表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("IS user is_phone_report_page open fail ...")
                utils.get_shot_image(driver, "is_phone_report_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user is_phone_report_page open fail ...")
        
    def test_IS_case_14(self):
        u''' 测试线上is账户  " 销售管理 ——> IS业绩分组统计  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"IS业绩分组统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("IS user is_result_count_by_group_page open fail ...")
                utils.get_shot_image(driver, "is_result_count_by_group_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user is_result_count_by_group_page open fail ...")
        
    def test_IS_case_15(self):
        u''' 测试线上is账户  " 销售管理 ——> IS学员跟进统计  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"IS学员跟进统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"search":
                result = True
            else:
                result = False
                self.log.error("IS user is_student_follow_count_page open fail ...")
                utils.get_shot_image(driver, "is_student_follow_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user is_student_follow_count_page open fail ...")
        
    def test_IS_case_16(self):
        u''' 测试线上is账户  " 销售管理 ——> sc续费率  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"sc续费率")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("IS user sc_keep_pay_ratio_page open fail ...")
                utils.get_shot_image(driver, "sc_keep_pay_ratio_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user sc_keep_pay_ratio_page open fail ...")
        
    def test_IS_case_17(self):
        u''' 测试线上is账户  " 销售管理 ——> 个人信息  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"个人信息")
        time.sleep(2)
        
        try:
            table_name = utils.find_id(driver, "ui-dialog-title-pop_div_admin_user_ext").text
            print "table_name --->",table_name
            if table_name == u"CRM用户信息收集，请完整填写，并保证真实有效":
                result = True
            else:
                result = False
                self.log.error("IS user personal_info_page open fail ...")
                utils.get_shot_image(driver, "personal_info_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user personal_info_page open fail ...")
        
    def test_IS_case_18(self):
        u''' 测试线上is账户  " 销售管理 ——> 51talk通讯录  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        
        driver = self.driver
        #二次定位到leftFrame模块，然后switch到leftFrame
        frameset = utils.find_id(driver,"frame")
        left_frame = utils.find_name(frameset,"leftFrame")
        driver.switch_to_frame(left_frame)
        
        #WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_link_text("课程管理"), u'页面加载失败')
        driver.implicitly_wait(20)
        utils.finds_link_text(driver,u"51talk通讯录")[1].click()
        driver.implicitly_wait(5)
        
        #同理二次定位到rightFrame模块，然后switch到rightFrame
        driver.switch_to_default_content()
        frameset = utils.find_id(driver,"frame")
        right_frame = utils.find_id(frameset,"rightframe")
        driver.switch_to_frame(right_frame)

        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"公司人员列表":
                result = True
            else:
                result = False
                self.log.error("IS user 51talk_phonenumber_book_page open fail ...")
                utils.get_shot_image(driver, "51talk_phonenumber_book_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user 51talk_phonenumber_book_page open fail ...")
        
    def aaaaaaaaaaaatest_IS_case_19(self):
        u''' 测试线上is账户  " 销售管理 ——> 电子名片  "页面打开是否正常
            该页面打开有问题
           '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"电子名片")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"公司人员列表":
                result = True
            else:
                result = False
                self.log.error("IS user 51talk_phonenumber_book_page open fail ...")
                utils.get_shot_image(driver, "51talk_phonenumber_book_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user 51talk_phonenumber_book_page open fail ...")
        
    def test_IS_case_20(self):
        u''' 测试线上is账户  " 销售管理 ——> 发票管理  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"发票管理")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"search":
                result = True
            else:
                result = False
                self.log.error("IS user invoice_manage_page open fail ...")
                utils.get_shot_image(driver, "invoice_manage_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user invoice_manage_page open fail ...")
        
    def test_IS_case_21(self):
        u''' 测试线上is账户  " 销售管理 ——> 点数申请列表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"点数申请列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("IS user point_apply_list_page open fail ...")
                utils.get_shot_image(driver, "point_apply_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user point_apply_list_page open fail ...")
        
    def test_IS_case_22(self):
        u''' 测试线上is账户  " 销售管理 ——> 浏览订单  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"浏览订单")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "submit").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"查询":
                result = True
            else:
                result = False
                self.log.error("IS user view_order_page open fail ...")
                utils.get_shot_image(driver, "view_order_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user view_order_page open fail ...")
        
    def test_IS_case_23(self):
        u''' 测试线上is账户  " 销售管理 ——> 处理订单  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"处理订单")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_css(driver, "input[type='submit']").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"search":
                result = True
            else:
                result = False
                self.log.error("IS user deal_order_page open fail ...")
                utils.get_shot_image(driver, "deal_order_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user deal_order_page open fail ...")
        
    def test_IS_case_24(self):
        u''' 测试线上is账户  " 客服管理 ——> 推荐老师  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客服管理")
        driver = default_page.select_left_module(u"推荐老师")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"teacher filter":
                result = True
            else:
                result = False
                self.log.error("IS user recommon_teacher_page open fail ...")
                utils.get_shot_image(driver, "recommon_teacher_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user recommon_teacher_page open fail ...")
        
    def test_IS_case_25(self):
        u''' 测试线上is账户  " 系统设置管理 ——> change password  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.is_user_name,passwd=self.is_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"系统设置管理")
        driver = default_page.select_left_module(u"change password")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Change Password":
                result = True
            else:
                result = False
                self.log.error("IS user change_password_page open fail ...")
                utils.get_shot_image(driver, "change_password_page_error")
        except:
            result = False
        
        self.assertTrue(result, "IS user change_password_page open fail ...")
        
    def test_PT_case_1(self):
        u''' 测试线上pt账户  " 客户管理 ——> student list  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"student list")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"会员检索":
                result = True
            else:
                result = False
                self.log.error("PT user student_list_page open fail ...")
                utils.get_shot_image(driver, "student_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user student_list_page open fail ...")
        
    def aaaaaaaaaaaaaatest_PT_case_2(self):
        u''' 测试线上pt账户  " 客户管理 ——> 添加学员（聚划算）  "页面打开是否正常   
        遗留问题：程序运行时，在点击进入功能页面时，总是会弹出“请先登录”提示框，不知道为什么？？？？？
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"添加学员（聚划算）")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"添加学生":
                result = True
            else:
                result = False
                self.log.error("PT user add_student(juhuasuan)_page open fail ...")
                utils.get_shot_image(driver, "add_student(juhuasuan)_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user add_student(juhuasuan)_page open fail ...")
        
    def aaaaaaaaaaaaatest_PT_case_3(self):
        u''' 测试线上pt账户  " 客户管理 ——> 添加用户(2.0)  "页面打开是否正常 
        遗留问题：程序运行时，在点击进入功能页面时，总是会弹出“请先登录”提示框，不知道为什么？？？？？
          '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"客户管理")
        driver = default_page.select_left_module(u"添加用户(2.0)")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"添加学生":
                result = True
            else:
                result = False
                self.log.error("PT user add_student(2.0)_page open fail ...")
                utils.get_shot_image(driver, "add_student(2.0)_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user add_student(2.0)_page open fail ...")
        
    def test_PT_case_4(self):
        u''' 测试线上pt账户  " 销售管理 ——> 问题列表  "页面打开是否正常   '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"问题列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"":
                result = True
            else:
                result = False
                self.log.error("PT user question_list_page open fail ...")
                utils.get_shot_image(driver, "question_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user question_list_page open fail ...")
        
    def aaaaaaaaaatest_PT_case_5(self):
        u''' 测试线上pt账户  " 销售管理 ——> 服务时效统计  "页面打开是否正常   
        遗留问题：程序运行时，在点击进入功能页面时，总是会弹出“请先登录”提示框，不知道为什么？？？？？
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"服务时效统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[align='left']").text
            print "table_name --->",table_name
            if table_name == u"Search":
                result = True
            else:
                result = False
                self.log.error("PT user sevice_aging_count_page open fail ...")
                utils.get_shot_image(driver, "sevice_aging_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user sevice_aging_count_page open fail ...")
        
    def aaaaaaaaaatest_PT_case_6(self):
        u''' 测试线上pt账户  " 销售管理 ——> 问题类型统计  "页面打开是否正常   
        遗留问题：程序运行时，在点击进入功能页面时，总是会弹出“请先登录”提示框，不知道为什么？？？？？
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"问题类型统计")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_class(driver, "search").text
            print "search_button_text --->",search_button_text
            if search_button_text == u"查询":
                result = True
            else:
                result = False
                self.log.error("PT user question_type_count_page open fail ...")
                utils.get_shot_image(driver, "question_type_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user question_type_count_page open fail ...")
        
        
    def test_PT_case_7(self):
        u''' 测试线上pt账户  " 销售管理 ——> 学生列表  "页面打开是否正常   
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"学生列表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"会员检索":
                result = True
            else:
                result = False
                self.log.error("PT user student_list_page open fail ...")
                utils.get_shot_image(driver, "student_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user student_list_page open fail ...")
        
    def test_PT_case_8(self):
        u''' 测试线上pt账户  " 销售管理 ——> IS学员课耗统计  "页面打开是否正常   
                            页面打开有问题
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"IS学员课耗统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"search":
                result = True
            else:
                result = False
                self.log.error("PT user is_student_cost_count_page open fail ...")
                utils.get_shot_image(driver, "is_student_cost_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user is_student_cost_count_page open fail ...")
        
    def test_PT_case_9(self):
        u''' 测试线上pt账户  " 销售管理 ——> 个人信息 "页面打开是否正常   
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"个人信息")
        time.sleep(2)
        
        try:
            page_count = utils.find_css(driver, "html > body").text
            print "page_count --->",page_count
            if page_count == u"您所在的组没有开启CRM用户信息收集，请联系管理员！":
                result = True
            else:
                result = False
                self.log.error("PT user personal_info_page open fail ...")
                utils.get_shot_image(driver, "personal_info_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user personal_info_page open fail ...")
        
    def aaaaaaaaaaaaaaaatest_PT_case_10(self):
        u''' 测试线上pt账户  " 销售管理 ——> 51talk通讯录 "页面打开是否正常  
        遗留问题：程序运行时，在点击进入功能页面时，总是会弹出“请先登录”提示框，不知道为什么？？？？？ 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        
        driver = self.driver
        #二次定位到leftFrame模块，然后switch到leftFrame
        frameset = utils.find_id(driver,"frame")
        left_frame = utils.find_name(frameset,"leftFrame")
        driver.switch_to_frame(left_frame)
        
        #WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_link_text("课程管理"), u'页面加载失败')
        driver.implicitly_wait(20)
        utils.finds_link_text(driver,u"51talk通讯录")[1].click()
        driver.implicitly_wait(5)
        
        #同理二次定位到rightFrame模块，然后switch到rightFrame
        driver.switch_to_default_content()
        frameset = utils.find_id(driver,"frame")
        right_frame = utils.find_id(frameset,"rightframe")
        driver.switch_to_frame(right_frame)

        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "submit").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"搜索":
                result = True
            else:
                result = False
                self.log.error("PT user 51talk_phonenumber_book_page open fail ...")
                utils.get_shot_image(driver, "51talk_phonenumber_book_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user 51talk_phonenumber_book_page open fail ...")
        
    def aaaaaaaaaaaaaatest_PT_case_11(self):
        u''' 测试线上pt账户  " 销售管理 ——> 电子名片 "页面打开是否正常   
        页面打开有问题
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"电子名片")
        time.sleep(2)
        
        try:
            page_count = utils.find_css(driver, "html > body").text
            print "page_count --->",page_count
            if page_count == u"":
                result = True
            else:
                result = False
                self.log.error("PT user personal_info_page open fail ...")
                utils.get_shot_image(driver, "personal_info_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user personal_info_page open fail ...")
        
    def aaaaaaaaaaaaaatest_PT_case_12(self):
        u''' 测试线上pt账户  " 销售管理 ——> 分班监控详情 "页面打开是否正常 
        遗留问题：程序运行时，在点击进入功能页面时，总是会弹出“请先登录”提示框，不知道为什么？？？？  
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"分班监控详情")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"PT分班监控":
                result = True
            else:
                result = False
                self.log.error("PT user monitor_detail_by_class_page open fail ...")
                utils.get_shot_image(driver, "monitor_detail_by_class_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user monitor_detail_by_class_page open fail ...")
        
    def aaaaaaaaaaaaaaaatest_PT_case_13(self):
        u''' 测试线上pt账户  " 销售管理 ——> 分班监控 "页面打开是否正常 
        遗留问题：程序运行时，在点击进入功能页面时，总是会弹出“请先登录”提示框，不知道为什么？？？？  
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"分班监控")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"PT分班监控":
                result = True
            else:
                result = False
                self.log.error("PT user monitor_by_class_page open fail ...")
                utils.get_shot_image(driver, "monitor_by_class_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user monitor_by_class_page open fail ...")
        
    def test_PT_case_13(self):
        u''' 测试线上pt账户  " 销售管理 ——> PT公告管理TL "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"PT公告管理TL")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='bg_tr'] > span[class='TableRow2']").text
            print "table_name --->",table_name
            if table_name == u"序号":
                result = True
            else:
                result = False
                self.log.error("PT user pt_notice_manage_TL_page open fail ...")
                utils.get_shot_image(driver, "pt_notice_manage_TL_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user pt_notice_manage_TL_page open fail ...")
        
    def test_PT_case_14(self):
        u''' 测试线上pt账户  " 销售管理 ——> PT公告管理 "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"PT公告管理")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='bg_tr'] > span[class='TableRow2']").text
            print "table_name --->",table_name
            if table_name == u"序号":
                result = True
            else:
                result = False
                self.log.error("PT user pt_notice_manage_page open fail ...")
                utils.get_shot_image(driver, "pt_notice_manage_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user pt_notice_manage_page open fail ...")
        
    def test_PT_case_15(self):
        u''' 测试线上pt账户  " 销售管理 ——> 学员公池 "页面打开是否正常 
        
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"学员公池")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "sub").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"搜索":
                result = True
            else:
                result = False
                self.log.error("PT user student_gongchi_page open fail ...")
                utils.get_shot_image(driver, "student_gongchi_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user student_gongchi_page open fail ...")
        
    def test_PT_case_16(self):
        u''' 测试线上pt账户  " 销售管理 ——> 回收站 "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"回收站")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "sub").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"搜索":
                result = True
            else:
                result = False
                self.log.error("PT user recycle_station_page open fail ...")
                utils.get_shot_image(driver, "recycle_station_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user recycle_station_page open fail ...")
        
    def aaaaaaatest_PT_case_17(self):
        u''' 测试线上pt账户  " 销售管理 ——> 回收站 "页面打开是否正常 
        遗留问题：程序运行时，在点击进入功能页面时，总是会弹出“请先登录”提示框，不知道为什么？？？？
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"回收站")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "sub").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"搜索":
                result = True
            else:
                result = False
                self.log.error("PT user recycle_station_page open fail ...")
                utils.get_shot_image(driver, "recycle_station_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user recycle_station_page open fail ...")
        
    def test_PT_case_18(self):
        u''' 测试线上pt账户  " 销售管理 ——> PT 销售报表 "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"PT 销售报表")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Time":
                result = True
            else:
                result = False
                self.log.error("PT user pt_sale_report_page open fail ...")
                utils.get_shot_image(driver, "pt_sale_report_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user pt_sale_report_page open fail ...")
        
    def test_PT_case_19(self):
        u''' 测试线上pt账户  " 销售管理 ——> PT 公开课 "页面打开是否正常 
        遗留问题：程序运行时，在点击进入功能页面时，总是会弹出“请先登录”提示框，不知道为什么？？？？
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"PT 公开课")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "submit").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"Search":
                result = True
            else:
                result = False
                self.log.error("PT user pt_common_class_page open fail ...")
                utils.get_shot_image(driver, "pt_common_class_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user pt_common_class_page open fail ...")
        
    def test_PT_case_20(self):
        u''' 测试线上pt账户  " 销售管理 ——> PT follow list "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"PT follow list")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"筛选条件":
                result = True
            else:
                result = False
                self.log.error("PT user pt_follow_list_page open fail ...")
                utils.get_shot_image(driver, "pt_follow_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user pt_follow_list_page open fail ...")
        
    def aaaaaaaaaaaatest_PT_case_21(self):
        u''' 测试线上pt账户  " 教务管理 ——> APP班级统计 "页面打开是否正常 
                                点击进入页面时，弹出先进行登录提示
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"APP班级统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"筛选条件":
                result = True
            else:
                result = False
                self.log.error("PT user pt_follow_list_page open fail ...")
                utils.get_shot_image(driver, "pt_follow_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user pt_follow_list_page open fail ...")
        
    def aaaaaaaaaatest_PT_case_22(self):
        u''' 测试线上pt账户  " 教务管理 ——> LC课程管理 "页面打开是否正常 
                                点击进入页面时，弹出先进行登录提示
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"APP班级统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"筛选条件":
                result = True
            else:
                result = False
                self.log.error("PT user pt_follow_list_page open fail ...")
                utils.get_shot_image(driver, "pt_follow_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user pt_follow_list_page open fail ...")
        
    def aaaaaaaaaaaatest_PT_case_23(self):
        u''' 测试线上pt账户  " 教务管理 ——> LC排班 "页面打开是否正常 
                                点击进入页面时，弹出先进行登录提示
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"销售管理")
        driver = default_page.select_left_module(u"APP班级统计")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='bg_tr'] > span[class='TableRow2']").text
            print "table_name --->",table_name
            if table_name == u"ID":
                result = True
            else:
                result = False
                self.log.error("PT user pt_follow_list_page open fail ...")
                utils.get_shot_image(driver, "pt_follow_list_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user pt_follow_list_page open fail ...")
        
    def test_PT_case_24(self):
        u''' 测试线上pt账户  " 教务管理 ——> PT老师管理 "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"教务管理")
        driver = default_page.select_left_module(u"PT老师管理")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver, "tr > th[class='bg_tr'] > span[class='TableRow2']").text
            print "table_name --->",table_name
            if table_name == u"ID":
                result = True
            else:
                result = False
                self.log.error("PT user pt_teacher_manage_page open fail ...")
                utils.get_shot_image(driver, "pt_teacher_manage_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user pt_teacher_manage_page open fail ...")
        
    def test_PT_case_26(self):
        u''' 测试线上pt账户  " 教务管理 ——> F20排班表 "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"教务管理")
        driver = default_page.select_left_module(u"F20排班表")
        time.sleep(2)
        
        try:
            link_text = utils.find_link_text(driver, u"上一周").text
            print "link_text --->",link_text
            if link_text == u"上一周":
                result = True
            else:
                result = False
                self.log.error("PT user F20_arrange_class_page open fail ...")
                utils.get_shot_image(driver, "F20_arrange_class_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user F20_arrange_class_page open fail ...")
        
    def test_PT_case_27(self):
        u''' 测试线上pt账户  " 教务管理 ——> F20课程管理 "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"教务管理")
        driver = default_page.select_left_module(u"F20课程管理")
        time.sleep(2)
        
        try:
            link_text = utils.find_link_text(driver, u"添加公开课").text
            print "link_text --->",link_text
            if link_text == u"添加公开课":
                result = True
            else:
                result = False
                self.log.error("PT user F20_class_manage_page open fail ...")
                utils.get_shot_image(driver, "F20_class_manage_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user F20_class_manage_page open fail ...")
        
    def test_PT_case_28(self):
        u''' 测试线上pt账户  " 教务管理 ——> 上课统计 "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"教务管理")
        driver = default_page.select_left_module(u"上课统计")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "submit").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"搜索":
                result = True
            else:
                result = False
                self.log.error("PT user finished_class_count_page open fail ...")
                utils.get_shot_image(driver, "finished_class_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user finished_class_count_page open fail ...")
        
    def aaaaaaaaaatest_PT_case_29(self):
        u''' 测试线上pt账户  " 教务管理 ——> PT课程评价统计 "页面打开是否正常 
        点击提示重新登录
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"教务管理")
        driver = default_page.select_left_module(u"PT课程评价统计")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver, "submit").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"搜索":
                result = True
            else:
                result = False
                self.log.error("PT user finished_class_count_page open fail ...")
                utils.get_shot_image(driver, "finished_class_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user finished_class_count_page open fail ...")
        
    def test_PT_case_30(self):
        u''' 测试线上pt账户  " 教务管理 ——> AC 公开课统计 "页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"教务管理")
        driver = default_page.select_left_module(u"AC 公开课统计")
        time.sleep(2)
        
        try:
            link_text = utils.find_link_text(driver, u"返回列表页").text
            print "link_text --->",link_text
            if link_text == u"返回列表页":
                result = True
            else:
                result = False
                self.log.error("PT user ac_common_class_count_page open fail ...")
                utils.get_shot_image(driver, "ac_common_class_count_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user ac_common_class_count_page open fail ...")
        
    def test_PT_case_31(self):
        u''' 测试线上pt账户  " 教务管理 ——> AC 公开课"页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"教务管理")
        driver = default_page.select_left_module(u"AC 公开课")
        time.sleep(2)
        
        try:
            link_text = utils.find_link_text(driver, u"添加公开课").text
            print "link_text --->",link_text
            if link_text == u"添加公开课":
                result = True
            else:
                result = False
                self.log.error("PT user ac_common_class_page open fail ...")
                utils.get_shot_image(driver, "ac_common_class_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user ac_common_class_page open fail ...")
        
    def test_PT_case_32(self):
        u''' 测试线上pt账户  " 教务管理 ——> 添加AC老师"页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"教务管理")
        driver = default_page.select_left_module(u"添加AC老师")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver,"tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"  添加ac课老师":
                result = True
            else:
                result = False
                self.log.error("PT user add_ac_teacher_page open fail ...")
                utils.get_shot_image(driver, "add_ac_teacher_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user add_ac_teacher_page open fail ...")
        
    def test_PT_case_33(self):
        u''' 测试线上pt账户  " 系统设置管理 ——> change password"页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"系统设置管理")
        driver = default_page.select_left_module(u"change password")
        time.sleep(2)
        
        try:
            table_name = utils.find_css(driver,"tr > th[class='table_title']").text
            print "table_name --->",table_name
            if table_name == u"Change Password":
                result = True
            else:
                result = False
                self.log.error("PT user change_password_page open fail ...")
                utils.get_shot_image(driver, "change_password_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user change_password_page open fail ...")
        
    def test_PT_case_34(self):
        u''' 测试线上pt账户  " Teacher Management ——> AC Utilization"页面打开是否正常 
        '''
        #登录后台系统
        login_page = login.Login()
        self.driver = login_page.login(user_name=self.pt_user_name,passwd=self.pt_user_password)
        
        #窗口最大化，然后switch到topFrame
        default_page = default.Default(self.driver)
        default_page.select_top_module(u"Teacher Management")
        driver = default_page.select_left_module(u"AC Utilization")
        time.sleep(2)
        
        try:
            search_button_text = utils.find_name(driver,"submit").get_attribute("value")
            print "search_button_text --->",search_button_text
            if search_button_text == u"Search":
                result = True
            else:
                result = False
                self.log.error("PT user AC_Utilization_page open fail ...")
                utils.get_shot_image(driver, "AC_Utilization_page_error")
        except:
            result = False
        
        self.assertTrue(result, "PT user AC_Utilization_page open fail ...")
        
    
    def tearDown(self):
        utils.teardown(self)
    #test
        
'''
if __name__ == "__main__":
    unittest.main()
'''
