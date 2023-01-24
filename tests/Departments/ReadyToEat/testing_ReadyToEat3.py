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
    actual5 = "Dal Makhani Kit + 2 Rotis  "
    actual6 = "Dal Tadka Kit + 2 Rotis  "
    actual7 = "Sambhar Kit + 2 Rotis  "
    actual8 = "Misal Kit  "
    actual9 = "Pav Bhaji Kit  "
    actual10= "Upma Kit  "
    actual11 = "Dal Palak Kit + 2 Rotis  "
    actual12 = "Lasooni Palak Kit + 2 Rotis  "
    actual13 = "Mix Vegetable Kit + 2 Rotis  "
    actual14 = "Mutter Paneer Kit + 2 Rotis  "
    actual15 = "Veg Makhnwala Kit + 2 Rotis  "
    actual16= "Sev Tomato Kit + 2 Rotis  "
    actual17 = "Aloo Mutter Kit + 2 Rotis  "
    actual18 = "Navratan Korma Kit + 2 Rotis  "
    actual19 = "Paneer Bhurji Kit + 2 Rotis  "
    actual20 = "Paneer Butter Masala Kit + 2 Rotis  "
    actual21 = "Gobi Mutter Kit + 2 Rotis  "
    actual22 = "Methi Malai Mutter Kit + 2 Rotis  "
    actual23 = "Veg Kadai Kit + 2 Rotis  "
    actual24 = "Dudhi Halwa Kit  "
    actual25 = "Moong Dal Sheera Kit  "
    actual26 = "Pineapple Sheera Kit  "
    actual27 = "Palak Paneer Kit + 2 Rotis  "
    actual28 = "Dal Makhani Kit + 2 Rotis  "
    actual29 = "Dal Tadka Kit + 2 Rotis  "
    actual30 = "Sambhar Kit + 2 Rotis  "
    actual31 = "Chicken Korma + 2 Rotis  "



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
        self.roti_page.click_Weekly3()
        # self.roti_page.click_BiWeekly2()
        # self.roti_page.click_Monthly2()
        # self.roti_page.click_Once2()
        self.roti_page.click_Selectproducts3()
        time.sleep(5)
        self.roti_page.click_Daaltadka()
        self.roti_page.click_Daalmakhni()
        self.roti_page.click_Sambharkit()
        self.roti_page.click_Misalkit()
        self.roti_page.click_PlusMisalkit()
        self.roti_page.click_PlusMisalkit()
        self.roti_page.click_Addtocart()
        time.sleep(10)


    def test_labelReadyToEat11(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady11, 'textContent')
        print(label)
        self.assertEqual(self.actual5, label)
        time.sleep(10)

    def test_labelReadyToEat12(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady12, 'textContent')
        print(label)
        self.assertEqual(self.actual6, label)
        time.sleep(10)

    def test_labelReadyToEat13(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady13, 'textContent')
        print(label)
        self.assertEqual(self.actual7, label)
        time.sleep(10)

    def test_labelReadyToEat14(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady14, 'textContent')
        print(label)
        self.assertEqual(self.actual8, label)
        time.sleep(10)

    def test_labelReadyToEat15(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady15, 'textContent')
        print(label)
        self.assertEqual(self.actual9, label)
        time.sleep(10)

    def test_labelReadyToEat16(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady16, 'textContent')
        print(label)
        self.assertEqual(self.actual10, label)
        time.sleep(10)

    def test_labelReadyToEat17(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady17, 'textContent')
        print(label)
        self.assertEqual(self.actual11, label)
        time.sleep(10)

    def test_labelReadyToEat18(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady18, 'textContent')
        print(label)
        self.assertEqual(self.actual12, label)
        time.sleep(10)

    def test_labelReadyToEat19(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady19, 'textContent')
        print(label)
        self.assertEqual(self.actual13, label)
        time.sleep(10)

    def test_labelReadyToEat20(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady20, 'textContent')
        print(label)
        self.assertEqual(self.actual14, label)
        time.sleep(10)

    def test_labelReadyToEat21(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady21, 'textContent')
        print(label)
        self.assertEqual(self.actual15, label)
        time.sleep(10)

    def test_labelReadyToEat22(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady22, 'textContent')
        print(label)
        self.assertEqual(self.actual16, label)
        time.sleep(10)

    def test_labelReadyToEat23(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady23, 'textContent')
        print(label)
        self.assertEqual(self.actual17, label)
        time.sleep(10)

    def test_labelReadyToEat24(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady24, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)
        time.sleep(10)

    def test_labelReadyToEat25(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady25, 'textContent')
        print(label)
        self.assertEqual(self.actual19, label)
        time.sleep(10)

    def test_labelReadyToEat26(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady26, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)
        time.sleep(10)

    def test_labelReadyToEat27(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady27, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)
        time.sleep(10)

    def test_labelReadyToEat28(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady28, 'textContent')
        print(label)
        self.assertEqual(self.actual22, label)
        time.sleep(10)

    def test_labelReadyToEat29(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady29, 'textContent')
        print(label)
        self.assertEqual(self.actual23, label)
        time.sleep(10)

    def test_labelReadyToEat30(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady30, 'textContent')
        print(label)
        self.assertEqual(self.actual24, label)
        time.sleep(10)

    def test_labelReadyToEat31(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady31, 'textContent')
        print(label)
        self.assertEqual(self.actual25, label)
        time.sleep(10)

    def test_labelReadyToEat32(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady32, 'textContent')
        print(label)
        self.assertEqual(self.actual26, label)
        time.sleep(10)

    def test_labelReadyToEat33(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady33, 'textContent')
        print(label)
        self.assertEqual(self.actual27, label)
        time.sleep(10)

    def test_labelReadyToEat34(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady34, 'textContent')
        print(label)
        self.assertEqual(self.actual28, label)
        time.sleep(10)

    def test_llabelReadyToEat35(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady35, 'textContent')
        print(label)
        self.assertEqual(self.actual29, label)
        time.sleep(10)

    def test_labelReadyToEat36(self):
        label = self.roti_page.get_attribute(RotiKit.labelReady36, 'textContent')
        print(label)
        self.assertEqual(self.actual30, label)
        time.sleep(10)

    def test_labelReadyToEat37(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReady37, 'textContent')
        print(label)
        self.assertEqual(self.actual31, label)
        time.sleep(10)

