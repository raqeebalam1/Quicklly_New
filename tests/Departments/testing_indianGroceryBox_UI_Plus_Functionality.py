import time
from resources import ui_test_class
from resources.page_objects.indiangrocerybox import IndianGrocery
from resources.page_objects.indiangrocerybox import IndianGroceryBox
from selenium.webdriver.support.color import Color


class TesINDIANGROCERY(ui_test_class.UVXVXIIClass):
    grocerybox_page: IndianGroceryBox
    grocerybox_page: IndianGrocery

    actual1 = "Organic Grocery Box Subscription"
    actual2 = "Organic Grocery Box Subscription"
    actual3 = "Search for products..."
    actual4 = "Shipping"
    actual5 = "Minimum Order"
    actual6 = "Free"
    actual7 = "$0.00"
    actual8 = "What we Deliver"
    actual9 = "Authentic Indian Products"
    actual10 = "Unbeatable Prices"
    actual11 = "Customized Grocery Box"
    actual12 = "How it works"
    actual13 = "1. Build your organic grocery box"
    actual14 = "2. Select products"
    actual15 = "3. Set your frequency"
    actual16 = "Order Customized Organic Grocery Box"
    actual17 = "#f9660d"
    actual18 = "Organic Products"
    actual19 = "Thank you"
    actual20 = "Organic Kala Chana"
    actual21 = "Organic Chana Dal"
    actual22 = "Organic Chickpea Kabuli"
    actual23 = "Organic Tur Dal (Pigeon Pea Split)"
    actual24 = "Organic Urad Gota (White whole)"
    actual25 = "Organic Urad Gota (White whole)"
    actual26 = "Organic Masoor Dal (Red Lentils Split)"
    actual27 = "Organic Masoor Dal (Red Lentils Split)"
    actual28 = "Organic Green Moong Whole"
    actual29 = "Organic Green Moong Whole"
    actual30 = "Organic Moong Dal"
    actual31 = "Organic Moong Dal"
    actual32 = "Organic Panchratan Dal"
    actual33 = "Organic Yellow Split Dalia"
    actual34 = "Organic Rice Poha"
    actual35 = "Organic Idli Rava"
    actual36 = "Organic Dalia Wheat"
    actual37 = "Organic Finger Millet Flour (Ragi Atta)"
    actual38 = "Organic Rice Flour"
    actual39 = "Organic Gram Flour (Chana Besan)"
    actual40 = "Organic Jowar Flour"
    actual41 = "Organic Sugar (Raw & Unrefined)"
    actual42 = "Organic Sugar Brown (Raw & Unrefined)"
    actual43 = "Organic Mustard Oil"
    actual44 = "Organic Peanut Oil 1 Liter"
    actual45 = "Organic Sonamasoori Rice"
    actual46 = "Organic Rajma Chitra (Red)"
    actual47 = "Organic Chana Dal"

    @classmethod
    def setUpClass(cls):
        super(TesINDIANGROCERY, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANGROCERY, cls).tearDownClass()
        cls.driver.quit()

    def Payment(self):
        time.sleep(3)
        # self.grocerybox_page.click_OrganicIndianGrocery()
        self.grocerybox_page.click_MiniCart()
        self.grocerybox_page.click_Checkout()
        self.grocerybox_page.click_ProceedtoCheckout()
        time.sleep(3)
        self.grocerybox_page.click_payment1()
        time.sleep(5)
        self.grocerybox_page.click_Pay()
        time.sleep(3)
        thankYou = self.grocerybox_page.get_attribute(IndianGroceryBox.ThankYou, 'innerHTML')
        print(thankYou)
        self.assertEqual(self.actual19, thankYou)

    def Signin(self):
        self.grocerybox_page.select_dropdown()
        self.grocerybox_page.click_signin()
        self.grocerybox_page.EnterEmail("testaccount@quicklly.com")
        self.grocerybox_page.EnterPass("123456")
        self.grocerybox_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)

    def test_EnterZipCode(self):
        self.grocerybox_page.zip("60611")
        self.grocerybox_page.submit_zip()
        self.Signin()
        search = self.grocerybox_page.get_attribute(IndianGroceryBox.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        time.sleep(5)
        for i in range(7):
            time.sleep(1)
            self.grocerybox_page.click_RightArrow()
        self.grocerybox_page.click_indianGrocery()
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.indianGroceryLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)

    def test_Grocery(self):
        time.sleep(5)
        # self.grocerybox_page.click_Biweekly2()
        # self.grocerybox_page.click_buildABox()
        self.grocerybox_page.click_AddRagi()
        self.grocerybox_page.click_AddWholemillets()
        self.grocerybox_page.click_AddToCart()
        time.sleep(10)

    def test_labelFlours(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelFlour, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_labelMillets(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelMillets, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_labelPulses(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelPulses, 'textContent')
        print(label)
        self.assertEqual(self.actual22, label)

    def test_labelRice(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelRice, 'textContent')
        print(label)
        self.assertEqual(self.actual23, label)

    def test_labelSpices(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelSpices, 'textContent')
        print(label)
        self.assertEqual(self.actual24, label)

    def test_labelRaggi(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelRaggi, 'textContent')
        print(label)
        self.assertEqual(self.actual25, label)

    def test_labelAtta(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelAtta, 'textContent')
        print(label)
        self.assertEqual(self.actual26, label)

    def test_labelMillets2(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelMillets2, 'textContent')
        print(label)
        self.assertEqual(self.actual27, label)

    def test_labelBajra(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelBajra, 'textContent')
        print(label)
        self.assertEqual(self.actual28, label)

    def test_labelOrganicGreen(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelgreen2, 'textContent')
        print(label)
        self.assertEqual(self.actual29, label)

    def test_labelOrganicMoongDaal(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelmoong, 'textContent')
        print(label)
        self.assertEqual(self.actual30, label)

    def test_labelOrganicMoongDaal_4lb(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelmoong2, 'textContent')
        print(label)
        self.assertEqual(self.actual31, label)

    def test_labelOrganicPanchratanDal(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelpanchratan, 'textContent')
        print(label)
        self.assertEqual(self.actual32, label)

    def test_labelOrganicDalia(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labeldalia, 'textContent')
        print(label)
        self.assertEqual(self.actual33, label)

    def test_labelOrganicPoha(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelpoha, 'textContent')
        print(label)
        self.assertEqual(self.actual34, label)

    def test_labelOrganicRava(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelrava, 'textContent')
        print(label)
        self.assertEqual(self.actual35, label)

    def test_labelOrganicDaliaWheat(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelwheat, 'textContent')
        print(label)
        self.assertEqual(self.actual36, label)

    def test_labelOrganicMilletFlour(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelmilletFlour, 'textContent')
        print(label)
        self.assertEqual(self.actual37, label)

    def test_labelOrganicRice(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelriceflour, 'textContent')
        print(label)
        self.assertEqual(self.actual38, label)

    def test_labelOrganicGram(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelgramflour, 'textContent')
        print(label)
        self.assertEqual(self.actual39, label)

    def test_labelOrganicJowar(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labeljowarflour, 'textContent')
        print(label)
        self.assertEqual(self.actual40, label)

    def test_labelOrganicSugar(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelsugar, 'textContent')
        print(label)
        self.assertEqual(self.actual41, label)

    def test_labelOrganicBrownSugar(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelbrownsugar, 'textContent')
        print(label)
        self.assertEqual(self.actual42, label)

    def test_labelMustardOil(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelmustardoil, 'textContent')
        print(label)
        self.assertEqual(self.actual43, label)

    def test_labelPeanutoil(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelpeanutoil, 'textContent')
        print(label)
        self.assertEqual(self.actual44, label)

    def test_labelSanomasoriRice(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelsanomasori, 'textContent')
        print(label)
        self.assertEqual(self.actual45, label)

    def test_labelOrganicRajma(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelrajma, 'textContent')
        print(label)
        self.assertEqual(self.actual46, label)

    def test_labelOrganicChana(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelchanadal, 'textContent')
        print(label)
        self.assertEqual(self.actual47, label)

