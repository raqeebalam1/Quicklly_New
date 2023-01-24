import time
from resources import ui_test_class
from resources.page_objects.IndianSauces import IndianMealKitAndSauces
from resources.page_objects.IndianSauces import Sauces
from selenium.webdriver.support.color import Color

class TesINDIANSAUCES(ui_test_class.UVXVXVClass):
    sauces_page: IndianMealKitAndSauces
    sauces_page: Sauces

    actual1 = "EXPLORE OUR MENUS"
    actual2 = "Sauces"
    actual3 = "Search for products..."
    actual4 = "Meal Kit"
    actual5 = "Sauces"
    actual6 = "EFFORTLESS COOKING: HOW IT WORKS?"
    actual7 = "Step 1."
    actual8 = "Step 2."
    actual9 = "Step 3."
    actual10 = "Step 4."
    actual11 = "From Fridge to Pot: 2 - 3 mins"
    actual12 = "Set Pot to Cook: 1 min"
    actual13 = "Relax: 15+ mins"
    actual14 = "Enjoy!"
    actual15 = "OUR FOOD PHILOSOPHY"
    actual16 = " Indian Food Subscription Box"
    actual17 = "Nationwide"
    actual18 = "Bay Area"
    actual19 = "#000000"
    actual20 = "Meal Kit"
    actual21 = "Sauces"
    actual22 = "Eat Everything"
    actual23 = "Nut Free Meal Kit"
    actual24 = "Vegan Meal Kit"
    actual25 = "Vegan Meal Kit"
    actual26 = "Indian Instant Pot"
    actual27 = "Thank you"
    actual28 = "Tikka Masala  "
    actual29 = "Butter Masala  "
    actual30 = "Vindaloo  "
    actual31 = "Korma  "
    actual32 = "Kadai  "
    actual33 = "Goan  "

    @classmethod
    def setUpClass(cls):
        super(TesINDIANSAUCES, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANSAUCES, cls).tearDownClass()
        cls.driver.quit()

    def Payment(self):
        time.sleep(2)
        self.sauces_page.click_MiniCart()
        self.sauces_page.click_Checkout()
        self.sauces_page.click_Checkout2()
        self.sauces_page.click_payment1()
        time.sleep(5)
        self.sauces_page.click_Pay()
        thankYou = self.sauces_page.get_attribute(IndianMealKitAndSauces.ThankYou, 'innerHTML')
        print(thankYou)

    def Signin(self):
        self.sauces_page.select_dropdown()
        self.sauces_page.click_signin()
        self.sauces_page.EnterEmail("testaccount@quicklly.com")
        self.sauces_page.EnterPass("123456")
        self.sauces_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)

    def test_EnterZipCode(self):
        self.sauces_page.zip("60611")
        self.sauces_page.submit_zip()
        self.Signin()
        search = self.sauces_page.get_attribute(IndianMealKitAndSauces.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        time.sleep(5)
        for i in range(9):
            time.sleep(2)
            self.sauces_page.click_RightArrow()
        self.sauces_page.click_MealKit()
        self.sauces_page.click_Readytoeat()
        self.sauces_page.click_Selectproducts()
        self.sauces_page.click_Oragnicsauces()
        # self.sauces_page.click_Sauces()
        # label = self.sauces_page.get_attribute(IndianMealKitAndSauces.instantPot, 'innerHTML')
        # print(label)
        # self.assertEqual(self.actual2, label)
        self.sauces_page.click_Tikkamasala()
        self.sauces_page.click_Buttermasala()
        self.sauces_page.click_Vindaloo()
        self.sauces_page.click_Korma()
        time.sleep(10)
        # self.Payment()

    def test_labelSeeti(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Tikkamasala, 'innerHTML')
        print(label)
        self.assertEqual(self.actual28, label)

    def test_labelBiryani(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Buttermasala, 'innerHTML')
        print(label)
        self.assertEqual(self.actual29, label)

    def test_labelPaneer(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Vindaloo, 'innerHTML')
        print(label)
        self.assertEqual(self.actual30, label)

    def test_labelMasMeat(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Korma, 'innerHTML')
        print(label)
        self.assertEqual(self.actual31, label)

    def test_labelPalak(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Kadai, 'innerHTML')
        print(label)
        self.assertEqual(self.actual32, label)

    def test_labelChana(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Goan, 'innerHTML')
        print(label)
        self.assertEqual(self.actual33, label)
