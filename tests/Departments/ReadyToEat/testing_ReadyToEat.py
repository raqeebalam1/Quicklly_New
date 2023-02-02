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
    actual5 = "Butter Chicken with Basmati Rice  "
    actual6 = "Chicken Madras with Lemon Rice  "
    actual7 = "Chicken Vindaloo with Basmati Rice  "
    actual8 = "Yellow Lentil with Basmati Rice  "
    actual9 = "Chana Masala with Lemon Rice  "
    actual10= "Tofu Tikka Masala with Basmati Rice  "
    actual11 = "Paneer Tikka Masala with Basmati Rice  "
    actual12 = "Paneer Cashew Korma with Basmati Rice  "
    actual13 = "Veg Biryani  "
    actual14 = "Chicken Biryani  "
    actual15 = "Chicken Tikka Masala with Basmati Rice  "
    actual16 = "Dudhi Halwa Kit  "
    actual17 = "Dal Tadka Kit + 2 Rotis  "
    actual18 = "Sambhar Kit + 2 Rotis  "
    actual19 = "Chicken Korma + 2 Rotis  "
    actual20 = "Details"
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


    # def test_Signin(self):
    #     # self.roti_page.select_dropdown()
    #     # self.roti_page.click_signin()
    #     self.roti_page.EnterEmail("testaccount@quicklly.com")
    #     self.roti_page.EnterPass("123456")
    #     self.roti_page.click_login()
    #     time.sleep(2)
        # alert = self.driver.switch_to.alert
        # if alert:
        #     alert.accept()

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
        self.roti_page.click_Selectproducts1()
        time.sleep(5)
        self.roti_page.click_ButterChicken()
        self.roti_page.click_PlusButterChicken()
        self.roti_page.click_PlusButterChicken()
        self.roti_page.click_ChickenMadras()
        self.roti_page.click_ChickenVindaloo()
        self.roti_page.click_DetailsChickenMadras()
        self.roti_page.click_CloseDetailsChickenMadras()
        self.roti_page.click_Addtocart()
        time.sleep(10)


    def test_labelReadyToEat1(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat1, 'textContent')
        print(label)
        self.assertEqual(self.actual5, label)
        time.sleep(10)

    def test_labelReadyToEat2(self):
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat2, 'textContent')
        print(label)
        self.assertEqual(self.actual6, label)
        time.sleep(10)

    def test_labelReadyToEat3(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat3, 'textContent')
        print(label)
        self.assertEqual(self.actual7, label)
        time.sleep(10)

    def test_labelReadyToEat4(self):
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat4, 'textContent')
        print(label)
        self.assertEqual(self.actual8, label)
        time.sleep(10)


    def test_llabelReadyToEat5(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat5, 'textContent')
        print(label)
        self.assertEqual(self.actual9, label)
        time.sleep(10)

    def test_labelReadyToEat6(self):
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat6, 'textContent')
        print(label)
        self.assertEqual(self.actual10, label)
        time.sleep(10)

    def test_labelReadyToEat7(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat7, 'textContent')
        print(label)
        self.assertEqual(self.actual11, label)
        time.sleep(10)

    def test_labelReadyToEat8(self):
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat8, 'textContent')
        print(label)
        self.assertEqual(self.actual12, label)
        time.sleep(10)


    def test_labelReadyToEat9(self):
        time.sleep(10)
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat9, 'textContent')
        print(label)
        self.assertEqual(self.actual13, label)
        time.sleep(10)

    def test_labelReadyToEat10(self):
        label = self.roti_page.get_attribute(RotiKit.labelReadytoeat10, 'textContent')
        print(label)
        self.assertEqual(self.actual14, label)
        time.sleep(10)

    # def test_labelReadyToEat11(self):
    #     time.sleep(10)
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat11, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual15, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat12(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat12, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual16, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat13(self):
    #     time.sleep(10)
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat13, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual17, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat14(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat14, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual18, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat15(self):
    #     time.sleep(10)
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat15, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual19, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat16(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat16, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat17(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat17, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat18(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat18, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat19(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat19, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat20(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat20, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat21(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat21, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat22(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat22, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)

    # def test_labelReadyToEat23(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat23, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat24(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat24, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat25(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat25, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)
    #
    # def test_labelReadyToEat26(self):
    #     label = self.roti_page.get_attribute(RotiKit.labelReadytoeat26, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     time.sleep(10)

