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
    actual4 = "Jasneet K."
    actual5 = "Shikha P."
    actual6 = "Shilpa D."
    actual7 = "Cabbage Curry"
    actual8 = "Aloo Matar Curry"
    actual9 = "Veg Pulao"
    actual10 = "Shrikhand"
    actual11 = "Sabudana Khichadi"
    actual12 = "Roti"
    actual13 = "Methi Matar Malai"
    actual14 = "Matar Paneer"
    actual15 = "Maharaja Dal Baati Thali For Two"
    actual16 = "Kesar Badam Thandai (Holi Special)"
    actual17 = "Jeera Rice"
    actual18 = "Gulab Jamun"
    actual19 = "Dal Tadka"
    actual20 = "Chole"
    actual21 = "Boondi Raita"
    actual22 = "Basmati Rice"
    actual23 = "Baati"
    actual24 = "Paratha"
    actual25 = "Matar Paneer Meal for 2"
    actual26 = "Matar Paneer Meal"

    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

        
    def tiffin(self):
        time.sleep(3)
        self.depart_page.click_LeftArrow1()
        self.depart_page.click_Homemade()
        time.sleep(5)
        self.depart_page.click_Nikita()
        # self.depart_page.click_Date()
        # self.depart_page.click_ChangeSlot()
        # self.depart_page.click_Schedule()
        # self.depart_page.click_Slot()
        # self.depart_page.click_Time()
        # self.depart_page.click_Submit4()
        time.sleep(5)
        self.depart_page.select_Cabbage()
        self.depart_page.select_AloMattar()
        self.depart_page.select_VegPulao()
        self.depart_page.select_Shrikhand()
        self.depart_page.select_SabudanaKhichri()
        time.sleep(10)
        # self.depart_page.click_MiniCart2()
        # self.depart_page.click_Checkout()

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

    def test_labelCabbage(self):
        label = self.depart_page.get_attribute(Department.labelCabbage, 'innerHTML')
        print(label)
        self.assertEqual(self.actual7, label)

    def test_labelAloMatar(self):
        label = self.depart_page.get_attribute(Department.labelAloMatar, 'innerHTML')
        print(label)
        self.assertEqual(self.actual8, label)

    def test_labelVegPulao(self):
        label = self.depart_page.get_attribute(Department.labelVegPulao, 'innerHTML')
        print(label)
        self.assertEqual(self.actual9, label)

    def test_labelShrikhand(self):
        label = self.depart_page.get_attribute(Department.labelShrikhand, 'textContent')
        print(label)
        self.assertEqual(self.actual10, label)

    def test_labelSabudanaKhicdi(self):
        label = self.depart_page.get_attribute(Department.labelKhicdi, 'textContent')
        print(label)
        self.assertEqual(self.actual11, label)

    def test_labelRoti(self):
        label = self.depart_page.get_attribute(Department.labelRoti, 'textContent')
        print(label)
        self.assertEqual(self.actual12, label)

    def test_labelMeethiMatar(self):
        label = self.depart_page.get_attribute(Department.labelMatarMalai, 'textContent')
        print(label)
        self.assertEqual(self.actual13, label)

    def test_labelMatarPaeer(self):
        label = self.depart_page.get_attribute(Department.labelMatarPaneer, 'innerHTML')
        print(label)
        self.assertEqual(self.actual14, label)

    def test_labelDaalBaati(self):
        label = self.depart_page.get_attribute(Department.labelDaalBaati, 'innerHTML')
        print(label)
        self.assertEqual(self.actual15, label)

    def test_labelThandai(self):
        label = self.depart_page.get_attribute(Department.labelBadamThandai, 'innerHTML')
        print(label)
        self.assertEqual(self.actual16, label)

    def test_labelJeeraRice(self):
        label = self.depart_page.get_attribute(Department.labelJeeraRice, 'textContent')
        print(label)
        self.assertEqual(self.actual17, label)

    def test_labelGulabJamun(self):
        label = self.depart_page.get_attribute(Department.labelGulabJamun, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_labelDaalTadka(self):
        label = self.depart_page.get_attribute(Department.labelDaalTadka, 'textContent')
        print(label)
        self.assertEqual(self.actual19, label)

    def test_labelChole(self):
        label = self.depart_page.get_attribute(Department.labelChoole, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_labelBoondiRaita(self):
        label = self.depart_page.get_attribute(Department.labelBoondiRaita, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_labelBasmatiRice(self):
        label = self.depart_page.get_attribute(Department.labelBasmatiRice, 'innerHTML')
        print(label)
        self.assertEqual(self.actual22, label)

    def test_labelBaati(self):
        label = self.depart_page.get_attribute(Department.labelBaati, 'innerHTML')
        print(label)
        self.assertEqual(self.actual23, label)

    def test_labelParatha(self):
        label = self.depart_page.get_attribute(Department.labelParatha, 'innerHTML')
        print(label)
        self.assertEqual(self.actual24, label)

    def test_labelMatarPaneer2(self):
        label = self.depart_page.get_attribute(Department.labelMatar2, 'innerHTML')
        print(label)
        self.assertEqual(self.actual24, label)

    def test_labelMatarPaneeer1(self):
        label = self.depart_page.get_attribute(Department.labelMatar1, 'innerHTML')
        print(label)
        self.assertEqual(self.actual25, label)


    def test_shopWithTiffin(self):
        self.tiffin()
        time.sleep(10)
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

