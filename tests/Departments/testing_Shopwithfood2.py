import time
from resources import ui_test_class
from resources.page_objects.chaiDepartment import ChaiAndCoffee
from resources.page_objects.chaiDepartment import CACD
from selenium.webdriver.support.color import Color


class TesCHAIDEPARTMENT(ui_test_class.UVXVIXClass):
    chai_page: CACD
    chai_page: ChaiAndCoffee

    actual1 = "Thank you"
    actual2 = "Your Account"
    actual3 = "Search for products..."
    actual4 = "Alu Tikka Chhole Chaat"
    actual5 = "Chicken Chhoela"
    actual6 = "Chicken Momo"
    actual7 = "Dahi Bhalla"
    actual8 = "Dilliwali Alu Tikka"
    actual9 = "Goat Chop"
    actual10 = "Gobhi 65"
    actual11 = "Onion Bhaji"
    actual12 = "Samosa Chaat"
    actual13 = "Vegetable Samosa"
    actual14 = "Butter Chicken"
    actual15 = "Cashew Chicken Tikka Masala"
    actual16 = "Chicken Bhuna"
    actual17 = "Chicken Chilli"
    actual18 = "Chicken Curry"
    actual19 = "Chicken Kadhai"
    actual20 = "Chicken Madras"
    actual21 = "Chicken Saag"
    actual22 = "Chicken Shahi Korma"
    actual23 = "Chicken Vindaalu"
    actual24 = "Heritage Goat"
    actual25 = "Lahsuni Chicken Korma"
    actual26 = "Lamb Curry"
    actual27 = "Lamb Korma"
    actual28 = "Lamb Madras"
    actual29 = "Lamb Masala"
    actual30 = "Lamb Saag"
    actual31 = "Lamb Vindaalu"
    actual32 = "Chicken Dum Biryani"
    actual33 = "Goat Dum Biryani"
    actual34 = "Lamb Dum Biryani"
    actual35 = "Shrimp Dum Biryani"
    actual36 = "Vegetable Dum Biryani"
    actual37 = "Chicken Tikka"
    actual38 = "Tandoori Boti Kebab"
    actual39 = "Tandoori Chicken"
    actual40 = "Tandoori Vegetables"
    actual41 = "Alu Gobhi"
    actual42 = "Alu Matar"
    actual43 = "Baingan Bharta"
    actual44 = "Bhindi Masala"
    actual45 = "Chana Masala"
    actual46 = "Dal Makhani"
    actual47 = "Dal Tadka"
    actual48 = "Makhamali Aalu"
    actual49 = "Matar Paneer"
    actual50 = "Mushroom Jalfreizi"
    actual51 = "Mushroom Kadhai"
    actual52 = "Paneer Chilli"
    actual53 = "Paneer Tikka Masala"
    actual54 = "Punjabi Jeera Alu"
    actual55 = "Saag Paneer"
    actual56 = "Vegetable Korma"
    actual57 = "Vegetable Madras"
    actual58 = "Vegetable Vindaalu"
    actual59 = "Goan Fish Curry"
    actual60 = "Shrimp Curry"
    actual61 = "Shrimp Masala"
    actual62 = "Shrimp Saag"
    actual63 = "Butter Naan"
    actual64 = "Garlic Naan"
    actual65 = "Gruyere Cheese Naan"
    actual66 = "Mirchi Masala Naan"
    actual67 = "Tandoori Roti"
    actual68 = "Boondi Raita"
    actual69 = "Saffron Rice"
    actual70 = "Vegetable Pickles"
    actual71 = "Yoghurt"
    actual72 = "Black Forest Gateau"
    actual73 = "Gajar Ka Halwa"
    actual74 = "Coke"
    actual75 = "Coke Zero"
    actual76 = "Limca"
    actual77 = "Mango Lassi"
    actual78 = "Sprite"
    actual79 = "Thums Up"


    @classmethod
    def setUpClass(cls):
        super(TesCHAIDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCHAIDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.chai_page.zip("60611")
        self.chai_page.submit_zip()
        time.sleep(2)
        self.test_Signin()
        time.sleep(5)
        search = self.chai_page.get_attribute(ChaiAndCoffee.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_Signin(self):
        self.chai_page.select_dropdown()
        self.chai_page.click_signin()
        self.chai_page.EnterEmail("testaccount@quicklly.com")
        self.chai_page.EnterPass("123456")
        self.chai_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)

    def test_clickChaiDepartment(self):
        time.sleep(5)
        self.chai_page.click_food()
        time.sleep(5)
        self.chai_page.click_Vajra()
        self.chai_page.click_Alutikka()
        self.chai_page.click_Addtocart()
        self.chai_page.click_Submit()
        self.chai_page.click_Chickencholea()
        self.chai_page.click_Addtocart()
        self.chai_page.click_Submit()
        self.chai_page.click_Gobhi65()
        self.chai_page.click_Addtocart()
        self.chai_page.click_Submit()
        self.chai_page.click_Vegsamosa()
        self.chai_page.click_Addtocart()
        self.chai_page.click_Submit()
        # # self.chai_page.click_MiniCart()
        # # self.chai_page.click_Checkout()
        # # self.chai_page.click_payment1()
        # # time.sleep(5)
        # # self.chai_page.click_Pay()
        time.sleep(30)


    def test_label1(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label1, 'textContent')
        print(label)
        self.assertEqual(self.actual4, label)
        time.sleep(10)

    def test_label2(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label2, 'textContent')
        print(label)
        self.assertEqual(self.actual5, label)
        time.sleep(10)

    def test_label3(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label3, 'textContent')
        print(label)
        self.assertEqual(self.actual6, label)
        time.sleep(10)

    def test_label4(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label4, 'textContent')
        print(label)
        self.assertEqual(self.actual7, label)
        time.sleep(10)

    def test_label5(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label5, 'textContent')
        print(label)
        self.assertEqual(self.actual8, label)
        time.sleep(10)

    def test_label6(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label6, 'textContent')
        print(label)
        self.assertEqual(self.actual9, label)
        time.sleep(10)

    def test_label7(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label7, 'textContent')
        print(label)
        self.assertEqual(self.actual10, label)
        time.sleep(10)

    def test_label8(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label8, 'textContent')
        print(label)
        self.assertEqual(self.actual11, label)
        time.sleep(10)

    def test_label9(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label9, 'textContent')
        print(label)
        self.assertEqual(self.actual12, label)
        time.sleep(10)

    def test_label11(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label11, 'textContent')
        print(label)
        self.assertEqual(self.actual13, label)
        time.sleep(10)

    def test_label12(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label12, 'textContent')
        print(label)
        self.assertEqual(self.actual14, label)
        time.sleep(10)

    def test_label13(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label13, 'textContent')
        print(label)
        self.assertEqual(self.actual15, label)
        time.sleep(10)

    def test_label14(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label14, 'textContent')
        print(label)
        self.assertEqual(self.actual16, label)
        time.sleep(10)

    def test_label15(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label15, 'textContent')
        print(label)
        self.assertEqual(self.actual17, label)
        time.sleep(10)

    def test_label16(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label16, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)
        time.sleep(10)

    def test_label17(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label17, 'textContent')
        print(label)
        self.assertEqual(self.actual19, label)
        time.sleep(10)

    def test_label18(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label18, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)
        time.sleep(10)

    def test_label19(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label19, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)
        time.sleep(10)

    def test_label20(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label20, 'textContent')
        print(label)
        self.assertEqual(self.actual22, label)
        time.sleep(10)

    def test_label21(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label21, 'textContent')
        print(label)
        self.assertEqual(self.actual23, label)
        time.sleep(10)

    def test_label22(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label22, 'textContent')
        print(label)
        self.assertEqual(self.actual24, label)
        time.sleep(10)

    def test_label23(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label23, 'textContent')
        print(label)
        self.assertEqual(self.actual25, label)
        time.sleep(10)

    def test_label24(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label24, 'textContent')
        print(label)
        self.assertEqual(self.actual26, label)
        time.sleep(10)

    def test_label25(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label25, 'textContent')
        print(label)
        self.assertEqual(self.actual27, label)
        time.sleep(10)

    def test_label26(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label26, 'textContent')
        print(label)
        self.assertEqual(self.actual28, label)
        time.sleep(10)

    def test_label27(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label27, 'textContent')
        print(label)
        self.assertEqual(self.actual29, label)
        time.sleep(10)

    def test_label28(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label28, 'textContent')
        print(label)
        self.assertEqual(self.actual30, label)
        time.sleep(10)

    def test_label29(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label29, 'textContent')
        print(label)
        self.assertEqual(self.actual31, label)
        time.sleep(10)

    def test_label30(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label30, 'textContent')
        print(label)
        self.assertEqual(self.actual32, label)
        time.sleep(10)

    def test_label31(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label31, 'textContent')
        print(label)
        self.assertEqual(self.actual33, label)
        time.sleep(10)

    def test_label32(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label32, 'textContent')
        print(label)
        self.assertEqual(self.actual34, label)
        time.sleep(10)

    def test_label33(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label33, 'textContent')
        print(label)
        self.assertEqual(self.actual35, label)
        time.sleep(10)

    def test_label34(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label34, 'textContent')
        print(label)
        self.assertEqual(self.actual36, label)
        time.sleep(10)

    def test_label35(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label35, 'textContent')
        print(label)
        self.assertEqual(self.actual37, label)
        time.sleep(10)

    def test_label36(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label36, 'textContent')
        print(label)
        self.assertEqual(self.actual38, label)
        time.sleep(10)

    def test_label37(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label37, 'textContent')
        print(label)
        self.assertEqual(self.actual39, label)
        time.sleep(10)

    def test_label38(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label38, 'textContent')
        print(label)
        self.assertEqual(self.actual40, label)
        time.sleep(10)

    def test_label39(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label39, 'textContent')
        print(label)
        self.assertEqual(self.actual41, label)
        time.sleep(10)

    def test_label40(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label40, 'textContent')
        print(label)
        self.assertEqual(self.actual42, label)
        time.sleep(10)

    def test_label41(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label41, 'textContent')
        print(label)
        self.assertEqual(self.actual43, label)
        time.sleep(10)

    def test_label42(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label42, 'textContent')
        print(label)
        self.assertEqual(self.actual44, label)
        time.sleep(10)

    def test_label43(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label43, 'textContent')
        print(label)
        self.assertEqual(self.actual45, label)
        time.sleep(10)

    def test_label44(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label44, 'textContent')
        print(label)
        self.assertEqual(self.actual46, label)
        time.sleep(10)

    def test_label45(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label45, 'textContent')
        print(label)
        self.assertEqual(self.actual47, label)
        time.sleep(10)

    def test_label46(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label46, 'textContent')
        print(label)
        self.assertEqual(self.actual48, label)
        time.sleep(10)

    def test_label47(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label47, 'textContent')
        print(label)
        self.assertEqual(self.actual49, label)
        time.sleep(10)

    def test_label48(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label48, 'textContent')
        print(label)
        self.assertEqual(self.actual50, label)
        time.sleep(10)

    def test_label49(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label49, 'textContent')
        print(label)
        self.assertEqual(self.actual51, label)
        time.sleep(10)

    def test_label50(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label50, 'textContent')
        print(label)
        self.assertEqual(self.actual52, label)
        time.sleep(10)

    def test_label51(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label51, 'textContent')
        print(label)
        self.assertEqual(self.actual53, label)
        time.sleep(10)

    def test_label52(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label52, 'textContent')
        print(label)
        self.assertEqual(self.actual54, label)
        time.sleep(10)

    def test_label53(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label53, 'textContent')
        print(label)
        self.assertEqual(self.actual55, label)
        time.sleep(10)

    def test_label54(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label54, 'textContent')
        print(label)
        self.assertEqual(self.actual56, label)
        time.sleep(10)

    def test_label55(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label55, 'textContent')
        print(label)
        self.assertEqual(self.actual57, label)
        time.sleep(10)

    def test_label56(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label56, 'textContent')
        print(label)
        self.assertEqual(self.actual58, label)
        time.sleep(10)

    def test_label57(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label57, 'textContent')
        print(label)
        self.assertEqual(self.actual59, label)
        time.sleep(10)

    def test_label58(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label58, 'textContent')
        print(label)
        self.assertEqual(self.actual60, label)
        time.sleep(10)

    def test_label59(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label59, 'textContent')
        print(label)
        self.assertEqual(self.actual61, label)
        time.sleep(10)

    def test_label60(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label60, 'textContent')
        print(label)
        self.assertEqual(self.actual62, label)
        time.sleep(10)

    def test_label61(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label61, 'textContent')
        print(label)
        self.assertEqual(self.actual63, label)
        time.sleep(10)

    def test_label62(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label62, 'textContent')
        print(label)
        self.assertEqual(self.actual64, label)
        time.sleep(10)

    def test_label63(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label63, 'textContent')
        print(label)
        self.assertEqual(self.actual65, label)
        time.sleep(10)

    def test_label64(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label64, 'textContent')
        print(label)
        self.assertEqual(self.actual66, label)
        time.sleep(10)

    def test_label65(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label65, 'textContent')
        print(label)
        self.assertEqual(self.actual67, label)
        time.sleep(10)

    def test_label66(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label66, 'textContent')
        print(label)
        self.assertEqual(self.actual68, label)
        time.sleep(10)

    def test_label67(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label67, 'textContent')
        print(label)
        self.assertEqual(self.actual69, label)
        time.sleep(10)

    def test_label68(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label68, 'textContent')
        print(label)
        self.assertEqual(self.actual70, label)
        time.sleep(10)

    def test_label69(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label69, 'textContent')
        print(label)
        self.assertEqual(self.actual71, label)
        time.sleep(10)

    def test_label70(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label70, 'textContent')
        print(label)
        self.assertEqual(self.actual72, label)
        time.sleep(10)

    def test_label71(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label71, 'textContent')
        print(label)
        self.assertEqual(self.actual73, label)
        time.sleep(10)

    def test_label72(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label72, 'textContent')
        print(label)
        self.assertEqual(self.actual74, label)
        time.sleep(10)

    def test_label73(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label73, 'textContent')
        print(label)
        self.assertEqual(self.actual75, label)
        time.sleep(10)

    def test_label74(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label74, 'textContent')
        print(label)
        self.assertEqual(self.actual76, label)
        time.sleep(10)

    def test_label75(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label75, 'textContent')
        print(label)
        self.assertEqual(self.actual77, label)
        time.sleep(10)

    def test_label76(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label76, 'textContent')
        print(label)
        self.assertEqual(self.actual78, label)
        time.sleep(10)

    def test_label77(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.label77, 'textContent')
        print(label)
        self.assertEqual(self.actual79, label)
        time.sleep(10)
