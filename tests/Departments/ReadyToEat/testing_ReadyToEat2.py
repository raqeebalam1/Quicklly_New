import time
from resources import ui_test_class
from resources.page_objects.rotikit import RotiBox
from resources.page_objects.rotikit import RotiKit
from selenium.webdriver.support.color import Color


class TesROTIKIT(ui_test_class.UVXVXIIIClass):
    roti_page: RotiKit
    roti_page: RotiBox

    actual1 = ""
    actual2 = " Order Roti Kit"
    actual3 = "Search for products..."
    actual4 = "Thank you"
    actual5 = "Tikka Masala  "
    actual6 = "Butter Masala  "
    actual7 = "Vindaloo  "
    actual8 = "Korma  "
    actual9 = "Kadai  "
    actual10= "Goan  "
    actual11 = "Dal Makhani Kit + 2 Rotis  "
    actual12 = "Dal Tadka Kit + 2 Rotis  "
    actual13 = "Sambhar Kit + 2 Rotis  "
    actual14 = "Chicken Korma + 2 Rotis  "



    @classmethod
    def setUpClass(cls):
        super(TesROTIKIT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesROTIKIT, cls).tearDownClass()
        cls.driver.quit()


    def test_Signin(self):
        self.roti_page.select_dropdown()
        self.roti_page.click_signin()
        self.roti_page.EnterEmail("testaccount@quicklly.com")
        self.roti_page.EnterPass("123456")
        self.roti_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()

    def test_EnterZipCode(self):
        self.roti_page.zip("60611")
        self.roti_page.submit_zip()
        # self.Signin()
        search = self.roti_page.get_attribute(RotiKit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        for i in range(5):
            self.roti_page.click_RightArrow()
        time.sleep(3)
        self.roti_page.click_ReadyToEat()
        time.sleep(3)
        self.roti_page.click_Weekly2()
        # self.roti_page.click_BiWeekly2()
        # self.roti_page.click_Monthly2()
        # self.roti_page.click_Once2()
        self.roti_page.click_Selectproducts2()
        time.sleep(5)
        self.roti_page.click_Tikkamasala()
        self.roti_page.click_PlusTikkamasala()
        self.roti_page.click_Buttermasala()
        self.roti_page.click_Vindalo()
        self.roti_page.click_Addtocart()
        time.sleep(10)


    def test_labelReadyToEat1(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady1, 'textContent')
        print(label)
        self.assertEqual(self.actual5, label)
        time.sleep(10)

    def test_labelReadyToEat2(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady2, 'textContent')
        print(label)
        self.assertEqual(self.actual6, label)
        time.sleep(10)

    def test_labelReadyToEat3(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady3, 'textContent')
        print(label)
        self.assertEqual(self.actual7, label)
        time.sleep(10)

    def test_labelReadyToEat4(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady4, 'textContent')
        print(label)
        self.assertEqual(self.actual8, label)
        time.sleep(10)


    def test_llabelReadyToEat5(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady5, 'textContent')
        print(label)
        self.assertEqual(self.actual9, label)
        time.sleep(10)

    def test_labelReadyToEat6(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady6, 'textContent')
        print(label)
        self.assertEqual(self.actual10, label)
        time.sleep(10)

    def test_labelReadyToEat7(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady7, 'textContent')
        print(label)
        self.assertEqual(self.actual11, label)
        time.sleep(10)

    def test_labelReadyToEat8(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady8, 'textContent')
        print(label)
        self.assertEqual(self.actual12, label)
        time.sleep(10)


    def test_labelReadyToEat9(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady9, 'textContent')
        print(label)
        self.assertEqual(self.actual13, label)
        time.sleep(10)

    def test_labelReadyToEat10(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady10, 'textContent')
        print(label)
        self.assertEqual(self.actual14, label)
        time.sleep(10)

