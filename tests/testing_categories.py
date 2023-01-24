import time
from resources import ui_test_class
from resources.page_objects.category import Category
from resources.page_objects.category import GroceryCategories


class TesCATEGORIES(ui_test_class.UVXIIIClass):
    category_page: Category
    category_page: GroceryCategories

    expected = "Unbeatable Deals"
    expected1 = "Foods & Beverages"
    expected2 = "Go Fresh"
    expected3 = "Grocery"
    expected4 = "Household"
    expected5 = "Meat Products"
    expected6 = "Organic"
    expected7 = "Personal Care"
    actual3 = "Search for products..."
    actual4 = "Jiffy Foil Utility Pan 2 COUNT"
    actual5 = "Jiffy Foil Utility Pan 2 COUNT"
    actual6 = "Hem Vanilla Incense 20 COUNT"
    actual7 = "Essential Everyday Foam Cups 51 COUNT"
    actual8 = "Red Candle 1 COUNT"
    actual9 = "Handi Foil Pie Pans 10 Inch 2 COUNT"
    actual10 = "Essential Everyday Coffee Creamer 16 Oz 2 COUNT"
    actual11 = "Baby Carrot 16 OZ"
    actual12 = "Green Swiss Chard Or Leek 1 LBS"
    actual13 = "Loose Turnip 1 LBS"
    actual14 = "Essential Everyday Ketchup 24 OZ"
    actual15 = "Kiwifruit Reg 1 COUNT"
    actual16 = "King Arthur Whole Wheat Flour 5 LBS"
    actual17 = "Red Delicious Apple Large 1 COUNT"
    actual18 = "Gala Apples  Small 1 COUNT"
    actual19 = "Maniola Orange 1 COUNT"


    @classmethod
    def setUpClass(cls):
        super(TesCATEGORIES, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCATEGORIES, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipcode(self):
        self.category_page.EnterZip("60611")
        self.category_page.submit_zip()
        search = self.category_page.get_attribute(Category.SearchForProducts, 'placeholder')
        self.assertEqual(search, self.actual3)


    def test_udeals(self):
        time.sleep(2)
        self.category_page.click_unbeatable()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected)
        time.sleep(15)

    def test_labelCoffee(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelCoffee, 'textContent')
        print(label)
        self.assertEqual(self.actual10, label)

    def test_labelCarrot(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelCarrot, 'textContent')
        print(label)
        self.assertEqual(self.actual11, label)

    def test_labelGreeswis(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelGreeswis, 'textContent')
        print(label)
        self.assertEqual(self.actual12, label)

    def test_labelLoose(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelLoose, 'textContent')
        print(label)
        self.assertEqual(self.actual13, label)

    def test_labelKetchup(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelKetchup, 'textContent')
        print(label)
        self.assertEqual(self.actual14, label)

    def test_fresh(self):
        time.sleep(5)
        self.category_page.click_GoFresh()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected2)
        time.sleep(15)

    def test_labelKiwi(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelKiwi, 'textContent')
        print(label)
        self.assertEqual(self.actual15, label)

    def test_labelApple1(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelApple1, 'textContent')
        print(label)
        self.assertEqual(self.actual16, label)

    def test_labelApple2(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelApple2, 'textContent')
        print(label)
        self.assertEqual(self.actual17, label)

    def test_labelApple3(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelApple3, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_labelOrange(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelOrange, 'textContent')
        print(label)
        self.assertEqual(self.actual19, label)

    def test_grocery(self):
        time.sleep(2)
        self.category_page.click_Grocery()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected3)
        # time.sleep(15)

    def test_meat(self):
        time.sleep(2)
        self.category_page.click_Meat()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected5)
        # time.sleep(15)

    def test_foodBeverages(self):
        time.sleep(2)
        self.category_page.click_Beverages()
        label = self.category_page.get_attribute(Category.StoreLabel, 'textContent')
        print(label)
        self.assertEqual(label, self.expected1)
        # time.sleep(15)

    def test_organic(self):
        time.sleep(2)
        self.category_page.click_Organic()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected6)
        # time.sleep(15)

    def test_personalCare(self):
        time.sleep(10)
        self.category_page.click_personalCare()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected7)
        time.sleep(15)

    def test_household(self):
        time.sleep(2)
        self.category_page.click_Household()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected4)
        time.sleep(15)

    def test_labelVanilla(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelVanila, 'textContent')
        print(label)
        self.assertEqual(self.actual4, label)

    def test_labelJiffyfoil(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelJiffy, 'textContent')
        print(label)
        self.assertEqual(self.actual5, label)

    def test_labelHandifoil(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelHandi, 'textContent')
        print(label)
        self.assertEqual(self.actual6, label)

    def test_labelCups(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelCups, 'textContent')
        print(label)
        self.assertEqual(self.actual7, label)

    def test_labelRedcandle(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelCandle, 'textContent')
        print(label)
        self.assertEqual(self.actual8, label)

    def test_labelHandifoilpie(self):
        time.sleep(10)
        label = self.category_page.get_attribute(Category.labelPie, 'textContent')
        print(label)
        self.assertEqual(self.actual9, label)



