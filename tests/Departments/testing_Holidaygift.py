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
    actual5 = "Holiday Special - Biryani & Lassi Combo (3 Biryani & 2 Lassi)"
    actual6 = "Holiday Special - Biryani & Paneer Tikka Masala (4 Meals)"
    actual7 = "Holiday Special - Butter Chicken & Chicken Tikka Masala Combo (4 Meals)"
    actual8 = "Holiday Special - The Taste of India (4 Meals & 2 Lassi)"
    actual9 = "Holiday Special Weekly 4 Meals Plan"
    actual10= "Holiday Special Weekly 8 Meals Plan"
    actual11 = "Holiday Special Weekly 12 Meals Plan"
    actual12 = "Holiday Special Superfood Parfait - Square"
    actual13 = "Holiday Special Superfood Parfait - Rectangle"
    actual14 = "Holiday Special Le Cadeau Parfait - Square"
    actual15 = "Holiday Special Le Cadeau Parfait - Rectangle"
    actual16 = "Laumiere Diwali  Premium Collection - Rectangle Sweet Box"
    actual17 = "Holiday Special LAutomne Gourmet Nuts"
    actual18 = "Laumiere Diwali  Premium Collection - Gourmet Nuts"
    actual19 = "Mithaas Savories Snack Pack"
    actual20 = "Holidays Special Exclusive Sweet Box"
    actual21 = "Holidays Special Assorted Large Box"
    actual22 = "Holidays Special Burfi and Roll Box"
    actual23 = "Kimbala Holiday Special Chai & Coffee Gift Hamper"


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
        time.sleep(3)
        self.roti_page.click_HolidayGift()
        time.sleep(3)
        self.roti_page.click_Giftnow()
        time.sleep(5)
        self.roti_page.click_Holiday1()
        self.roti_page.click_Submit()
        self.roti_page.click_Holiday2()
        self.roti_page.click_Holiday3()
        self.roti_page.click_Holiday4()
        time.sleep(10)


    def test_labelHoliday1(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelHoliday1, 'textContent')
        print(label)
        self.assertEqual(self.actual5, label)
        time.sleep(10)

    def test_labelHoliday2(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday2, 'textContent')
        print(label)
        self.assertEqual(self.actual6, label)
        time.sleep(10)

    def test_labelHoliday3(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelHoliday3, 'textContent')
        print(label)
        self.assertEqual(self.actual7, label)
        time.sleep(10)

    def test_labelHoliday4(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday4, 'textContent')
        print(label)
        self.assertEqual(self.actual8, label)
        time.sleep(10)


    def test_labelHoliday5(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelHoliday5, 'textContent')
        print(label)
        self.assertEqual(self.actual9, label)
        time.sleep(10)

    def test_labelHoliday6(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday6, 'textContent')
        print(label)
        self.assertEqual(self.actual10, label)
        time.sleep(10)

    def test_labelHoliday7(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelHoliday7, 'textContent')
        print(label)
        self.assertEqual(self.actual11, label)
        time.sleep(10)

    def test_labelHoliday8(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday8, 'textContent')
        print(label)
        self.assertEqual(self.actual12, label)
        time.sleep(10)


    def test_labelHoliday9(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelHoliday9, 'textContent')
        print(label)
        self.assertEqual(self.actual13, label)
        time.sleep(10)

    def test_labelHoliday10(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday10, 'textContent')
        print(label)
        self.assertEqual(self.actual14, label)
        time.sleep(10)

    def test_labelHoliday11(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelHoliday11, 'textContent')
        print(label)
        self.assertEqual(self.actual15, label)
        time.sleep(10)

    def test_labelHoliday12(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday12, 'textContent')
        print(label)
        self.assertEqual(self.actual16, label)
        time.sleep(10)


    def test_labelHoliday13(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelHoliday13, 'textContent')
        print(label)
        self.assertEqual(self.actual17, label)
        time.sleep(10)

    def test_labelHoliday14(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday14, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)
        time.sleep(10)

    def test_labelHoliday15(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelHoliday15, 'textContent')
        print(label)
        self.assertEqual(self.actual19, label)
        time.sleep(10)

    def test_labelHoliday16(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday16, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)
        time.sleep(10)

    def test_labelHoliday17(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday17, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)
        time.sleep(10)

    def test_labelHoliday18(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelHoliday18, 'textContent')
        print(label)
        self.assertEqual(self.actual22, label)
        time.sleep(10)

    def test_labelHoliday19(self):
        label = self.roti_page.get_attribute(RotiKit.labelHoliday19, 'textContent')
        print(label)
        self.assertEqual(self.actual23, label)
        time.sleep(10)
