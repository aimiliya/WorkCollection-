import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(60)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

        # 应用邀请他输入一个代办应用
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # 他在一个文本框中输入了‘Buy peacock feathers’
        # 伊迪斯的爱好是使用家蝇做鱼饵
        inputbox.send_keys('Buy peacock feathers')

        # 他按回车后更新了页面  # 待办表格中显示“Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页面中又显示其它文本框，输入其他内容
        #  他输入了‘Use peacock feathers to make a fly’
        #  伊迪斯做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，他的清单中显示了两个待办事项
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 伊迪斯想知道这个网站是否会记住他的清单

        # 他看到网站为他生成唯一的url
        #  而且页面中有一些文字解说这个功能
        self.fail('Finish test!')
        # 他访问那个url，发现他的待办事项还在

        # 他满意的去睡觉了


if __name__ == '__main__':
    unittest.main(warnings='ignore')
