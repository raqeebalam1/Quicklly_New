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
    actual20 = "12 piece Falafel"
    actual21 = "6 pcs falafel"
    actual22 = "Baba Ghannouj"
    actual23 = "Dolma"
    actual24 = "Ful Madames"
    actual25 = "Hummus and Meat"
    actual26 = "Shawarma Fries"
    actual27 = "Veggie Combo"
    actual28 = "Lentil"
    actual29 = "Soup Of The Day"
    actual30 = "Beef and Chicken Shawarma"
    actual31 = "Chicken Kabob"
    actual32 = "Double-meat Combo"
    actual33 = "Gyros Plate"
    actual34 = "Kalaya"
    actual35 = "Kefta Kabob"
    actual36 = "Lamb Chop"
    actual37 = "Lamb Shank"
    actual38 = "Shawarma"
    actual39 = "Shish Kabob"
    actual40 = "Triple-meat Combo"
    actual41 = "Beef Shawarma"
    actual42 = "Chicken Kabob"
    actual43 = "Chicken Shawarma"
    actual44 = "Falafel wrap"
    actual45 = "Kefta Kabob"
    actual46 = "Shish Kabob"
    actual47 = "Beef Shawarma Salad"
    actual48 = "Chicken Kabob Salad"
    actual49 = "Chicken Shawarma Salad"
    actual50 = "Cucumber Salad"
    actual51 = "Fattoush"
    actual52 = "House Salad"
    actual53 = "Grilled Shrimp Kabob"
    actual54 = "Salmon"
    actual55 = "Chicken Shawarma"
    actual56 = "Falafel wrap"
    actual57 = "Hummus"
    actual58 = "Shawarma"
    actual59 = "Triple-meat Combo"
    actual60 = "Eggs"
    actual61 = "Eggs with Meat"
    actual62 = "Eggs with Veggie"
    actual63 = "Pita"
    actual64 = "Tourshi"
    actual65 = "Baklava"
    actual66 = "Bottled Water"
    actual67 = "Raini Juice"
    actual68 = "Soft Drinks"
    actual69 = "Yogurt Drink"


    @classmethod
    def setUpClass(cls):
        super(TesINDIANGROCERY, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANGROCERY, cls).tearDownClass()
        cls.driver.quit()

    def Payment(self):
        time.sleep(3)
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

    def test_clickHomemadefood(self):
        time.sleep(5)
        self.grocerybox_page.click_Orderfood()
        self.grocerybox_page.click_Kabochi()

    def test_Homemade(self):
        time.sleep(5)
        self.grocerybox_page.Add_Falafel12()
        time.sleep(3)
        self.grocerybox_page.click_Addtocartbutton()
        self.grocerybox_page.Add_Falafel6()
        time.sleep(3)
        self.grocerybox_page.click_Addtocartbutton()
        self.grocerybox_page.Add_Babaganoch()
        time.sleep(3)
        self.grocerybox_page.click_Addtocartbutton()
        self.grocerybox_page.Add_Dolma()
        time.sleep(3)
        self.grocerybox_page.click_Addtocartbutton()
        time.sleep(10)

    def test_label12falafel(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.label12falafel, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_label6falafel(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.label6falafel, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_labelganooch(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelganooch, 'textContent')
        print(label)
        self.assertEqual(self.actual22, label)

    def test_labeldolmi(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labeldolmi, 'textContent')
        print(label)
        self.assertEqual(self.actual23, label)

    def test_labelmadames(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelmadames, 'textContent')
        print(label)
        self.assertEqual(self.actual24, label)

    def test_labelhumus(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelhumus, 'textContent')
        print(label)
        self.assertEqual(self.actual25, label)

    def test_labelshawarma(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelshawarma, 'textContent')
        print(label)
        self.assertEqual(self.actual26, label)

    def test_labelveggie(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelveggie, 'textContent')
        print(label)
        self.assertEqual(self.actual27, label)

    def test_labellentil(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labellentil, 'textContent')
        print(label)
        self.assertEqual(self.actual28, label)

    def test_labelsoup(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelsoup, 'textContent')
        print(label)
        self.assertEqual(self.actual29, label)

    def test_labelchickenshawarma(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelchickenshawarma, 'textContent')
        print(label)
        self.assertEqual(self.actual30, label)

    def test_labelkabob(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelkabob, 'textContent')
        print(label)
        self.assertEqual(self.actual31, label)

    def test_labeldoublemeat(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labeldoublemeat, 'textContent')
        print(label)
        self.assertEqual(self.actual32, label)

    def test_labelgyros(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelgyros, 'textContent')
        print(label)
        self.assertEqual(self.actual33, label)

    def test_labelkalaya(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelkalaya, 'textContent')
        print(label)
        self.assertEqual(self.actual34, label)

    def test_labelkefta(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelkefta, 'textContent')
        print(label)
        self.assertEqual(self.actual35, label)

    def test_labelchop(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelchop, 'textContent')
        print(label)
        self.assertEqual(self.actual36, label)

    def test_labelshank(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelshank, 'textContent')
        print(label)
        self.assertEqual(self.actual37, label)

    def test_labelshawarma2(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelshawarma2, 'textContent')
        print(label)
        self.assertEqual(self.actual38, label)

    def test_labelshish(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelshish, 'textContent')
        print(label)
        self.assertEqual(self.actual39, label)

    def test_labeltriplemeat(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labeltriplemeat, 'textContent')
        print(label)
        self.assertEqual(self.actual40, label)

    def test_labelbeefshawarma(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelbeefshawarma, 'textContent')
        print(label)
        self.assertEqual(self.actual41, label)

    def test_labelchickenkabob(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelchickenkabob, 'textContent')
        print(label)
        self.assertEqual(self.actual42, label)

    def test_labelchickenshawarma2(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelchickenshawarma2, 'textContent')
        print(label)
        self.assertEqual(self.actual43, label)

    def test_labelfalafelwarp(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelfalafelwarp, 'textContent')
        print(label)
        self.assertEqual(self.actual44, label)

    def test_labelkeftakabob(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelkeftakabob, 'textContent')
        print(label)
        self.assertEqual(self.actual45, label)

    def test_labelshishkabob(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelshishkabob, 'textContent')
        print(label)
        self.assertEqual(self.actual46, label)

    def test_labelbeefsalad(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelbeefsalad, 'textContent')
        print(label)
        self.assertEqual(self.actual47, label)

    def test_labelchickensalad(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelchickensalad, 'textContent')
        print(label)
        self.assertEqual(self.actual48, label)

    def test_labelchickenshawarmasalad(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelchickenshawarmasalad, 'textContent')
        print(label)
        self.assertEqual(self.actual49, label)

    def test_labelCucumberSalad(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelCucumberSalad, 'textContent')
        print(label)
        self.assertEqual(self.actual50, label)

    def test_labelFattoush(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelFattoush, 'textContent')
        print(label)
        self.assertEqual(self.actual51, label)

    def test_labelHouseSalad(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelHouseSalad, 'textContent')
        print(label)
        self.assertEqual(self.actual52, label)

    def test_labelGrilledShrimpKabob(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelGrilledShrimpKabob, 'textContent')
        print(label)
        self.assertEqual(self.actual53, label)

    def test_labelSalmon(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelSalmon, 'textContent')
        print(label)
        self.assertEqual(self.actual54, label)

    def test_labelChickenShawarma(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelChickenShawarma, 'textContent')
        print(label)
        self.assertEqual(self.actual55, label)

    def test_labelFalafelwrap(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelFalafelwrap, 'textContent')
        print(label)
        self.assertEqual(self.actual56, label)

    def test_labelHummus(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelHummus, 'textContent')
        print(label)
        self.assertEqual(self.actual57, label)

    def test_labelShawarma3(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelShawarma3, 'textContent')
        print(label)
        self.assertEqual(self.actual58, label)

    def test_labelTriple_meatCombo(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelTriple_meatCombo, 'textContent')
        print(label)
        self.assertEqual(self.actual59, label)

    def test_labelEggs(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelEggs, 'textContent')
        print(label)
        self.assertEqual(self.actual60, label)

    def test_labelEggswithMeat(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelEggswithMeat, 'textContent')
        print(label)
        self.assertEqual(self.actual61, label)

    def test_labelEggswithVeggie(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelEggswithVeggie, 'textContent')
        print(label)
        self.assertEqual(self.actual62, label)

    def test_labelPita(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelPita, 'textContent')
        print(label)
        self.assertEqual(self.actual63, label)

    def test_labelTourshi(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelTourshi, 'textContent')
        print(label)
        self.assertEqual(self.actual64, label)

    def test_labelBaklava(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelBaklava, 'textContent')
        print(label)
        self.assertEqual(self.actual65, label)

    def test_labelBottledWater(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelBottledWater, 'textContent')
        print(label)
        self.assertEqual(self.actual66, label)

    def test_labelRainiJuice(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelRainiJuice, 'textContent')
        print(label)
        self.assertEqual(self.actual67, label)

    def test_labelSoftDrinks(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelSoftDrinks, 'textContent')
        print(label)
        self.assertEqual(self.actual68, label)

    def test_labelYogurtDrink(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelYogurtDrink, 'textContent')
        print(label)
        self.assertEqual(self.actual69, label)
