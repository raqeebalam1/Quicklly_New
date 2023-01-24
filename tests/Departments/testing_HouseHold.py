import time
from resources import ui_test_class
from resources.page_objects.department import Department
from resources.page_objects.department import Dept
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TesDEPARTMENT(ui_test_class.UVIIClass):

    depart_page: Dept
    depart_page: Department

    actual1 = "Thank you"
    actual2 = "Your Account"
    actual3 = "Search for products..."
    actual4 = "Jiffy Foil Utility Pan 2 Count"
    actual5 = "Jiffy Foil Utility Pan 2 Count"
    actual6 = "Hem Vanilla Incense 20 Count"
    actual7 = "Essential Everyday Foam Cups 51 Count"
    actual8 = "Red Candle 1 Count"
    actual9 = "Handi Foil Pie Pans 10 Inch 2 Count"

    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def HouseHold(self):
        time.sleep(5)
        self.depart_page.click_HouseHold()
        time.sleep(2)
        self.depart_page.click_AddJiffyFoilPan()
        time.sleep(1)
        self.depart_page.click_AddHemVanilla()
        time.sleep(1)
        self.depart_page.click_AddCandle()
        time.sleep(1)
        self.depart_page.click_RightArrow2()
        self.depart_page.click_AddDawnFloz()
        time.sleep(10)
        # self.Payment()
        # self.depart_page.click_MiniCart()
        # time.sleep(2)
        # self.depart_page.click_Checkout()
        # time.sleep(2)
        # self.depart_page.click_Proceedtocheckout()
        # time.sleep(2)
        # self.test_SignIN()
        # time.sleep(3)
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()
        # time.sleep(10)

    def test_labelVanilla(self):
        time.sleep(10)
        label = self.depart_page.get_attribute(Department.labelVanila, 'textContent')
        print(label)
        self.assertEqual(self.actual4, label)

    def test_labelJiffyfoil(self):
        time.sleep(10)
        label = self.depart_page.get_attribute(Department.labelJiffy, 'textContent')
        print(label)
        self.assertEqual(self.actual5, label)

    def test_labelHandifoil(self):
        time.sleep(10)
        label = self.depart_page.get_attribute(Department.labelHandi, 'textContent')
        print(label)
        self.assertEqual(self.actual6, label)

    def test_labelCups(self):
        time.sleep(10)
        label = self.depart_page.get_attribute(Department.labelCups, 'textContent')
        print(label)
        self.assertEqual(self.actual7, label)

    def test_labelRedcandle(self):
        time.sleep(10)
        label = self.depart_page.get_attribute(Department.labelCandle, 'textContent')
        print(label)
        self.assertEqual(self.actual8, label)

    def test_labelHandifoilpie(self):
        time.sleep(10)
        label = self.depart_page.get_attribute(Department.labelPie, 'textContent')
        print(label)
        self.assertEqual(self.actual9, label)

    def test_EnterZipCode(self):
        self.depart_page.zip("60611")
        self.depart_page.submit_zip()
        search = self.depart_page.get_attribute(Department.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIN(self):
        self.depart_page.select_dropdown()
        self.depart_page.click_signin()
        self.depart_page.EnterEmail("testaccount@quicklly.com")
        self.depart_page.EnterPass("123456")
        self.depart_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        # AccountLabel = self.depart_page.get_attribute(Department.Account, 'innerHTML')
        # print(AccountLabel)
        # self.assertEqual(self.actual2, AccountLabel)



    # def test_ShopWithHouseHold(self):
    #     self.HouseHold()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def Payment(self):
        time.sleep(5)
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        time.sleep(3)
        # self.depart_page.click_ProceedtoCheckout()
        # time.sleep(5)
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.test_SignIN()
        # time.sleep(5)
        # self.depart_page.click_Pay()
        # time.sleep(3)
        # thankYou = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(thankYou)