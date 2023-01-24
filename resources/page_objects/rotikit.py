from resources.config_methods import DataClass
from resources.locators import RotiKit
from resources.page_objects.base_page import BasePage


class RotiBox(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(RotiKit.enter_zip).clear()
        self.find_element(RotiKit.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(RotiKit.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl.clslowspace > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow1(self):
        element = self.driver.find_element_by_xpath(
            ' // *[ @ id = "searchhide"] / div[1] / div / div / i[2] / img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[9]/div/div/div/div/a[13]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_rotiKit(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]//img[@alt="Rotikaa Foods"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[3]/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(RotiKit.BiWeekly)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_WholeWheat(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[1]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_roti(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[2]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_multiGrain(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[3]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_rotla(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[4]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Paratha(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[5]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_SpecialRoti(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[6]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Bakhri(self):
        element = self.driver.find_element_by_css_selector('#searchhide > section.clsFoodStores.organicproductsection.rotikalandingpage.clsPgWidth > div.tabcontents > div > div:nth-child(7) > a > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_OrderRotiKit(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[9]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddWheatBakhri(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[1]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddMasalaParatha(self):
        element = self.driver.find_element_by_xpath(
            '  // *[ @ id = "load_data"] / div[6] / div[4] / a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_PlusMasalaParatha(self):
        element = self.driver.find_element_by_xpath(
            '   // *[ @ id = "load_data"] / div[6] / div[4] / p / a / span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MinusMasalaParatha(self):
        element = self.driver.find_element_by_xpath(
            ' //*[@id="load_data"]/div[6]/div[4]/p/a/span[1]')
        self.driver.execute_script("arguments[0].click();", element)


    def click_DetailsCornRoti(self):
        element = self.driver.find_element_by_xpath(
             '//*[@id="load_data"]/div[12]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_CancelDetailsCornRoti(self):
        element = self.driver.find_element_by_xpath(
             '//*[@id="dvDialog-Custom"]/div/a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_AddRoti(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[1]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_plusRoti(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[1]/div[4]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="v-bar-fixed"]/div[2]/button[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(RotiKit.Email).clear()
        self.find_element(RotiKit.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(RotiKit.Pass).clear()
        self.find_element(RotiKit.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(RotiKit.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ProceedtoCheckout(self):
        self.click(RotiKit.ProceedtoCheckout)

    def click_Pay(self):
        self.click(RotiKit.Pay)

    def click_quicklly(self):
        self.click(RotiKit.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    # /HolidayGift methods/

    def click_HolidayGift(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/div/div/a[4]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Giftnow(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div/div[2]/div/a/input')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Holiday1(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div/div[1]/div[1]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Holiday2(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div/div[1]/div[2]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Holiday3(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div/div[1]/div[3]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Holiday4(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div/div[1]/div[4]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Submit(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "popupdelivery_date"] / div / div / center / button')
        self.driver.execute_script("arguments[0].click();", element)

    # /Readytoeatmeal methods/

    def click_ReadyToEat(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/div/div/a[11]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Selectproducts1(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[1]/div/div[5]/form/button[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ButterChicken(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ChickenMadras(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ChickenVindaloo(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[3]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ChickenBiryani(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[10]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusButterChicken(self):
         element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div[4]/p/a/span[3]')
         self.driver.execute_script("arguments[0].click();", element)

    def click_DetailsChickenMadras(self):
         element = self.driver.find_element_by_xpath('// *[ @ id = "load_data"] / div[2] / div[2] / a')
         self.driver.execute_script("arguments[0].click();", element)

    def click_CloseDetailsChickenMadras(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "dvDialog-Custom"] / div / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Addtocart(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "v-bar-fixed"] / div[2] / button[2]')
        self.driver.execute_script("arguments[0].click();", element)

        #Simmer Sauces#

    def click_Weekly2(self):
        element = self.driver.find_element_by_xpath(
            ' // *[ @ id = "searchhide"] / section[1] / div / div / div[2] / div / div[2] / ul / li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_BiWeekly2(self):
        element = self.driver.find_element_by_xpath(
            ' //*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[2]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly2(self):
        element = self.driver.find_element_by_xpath(
            ' //*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[2]/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[2]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Selectproducts2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[5]/form/button[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Tikkamasala(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Buttermasala(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Vindalo(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[3]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusTikkamasala(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div[4]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

      #DRY PACKED MEALKIT#

    def click_Weekly3(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[3]/div/div[2]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_BiWeekly3(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[3]/div/div[2]/ul/li[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly3(self):
        element = self.driver.find_element_by_xpath(
            ' //*[@id="searchhide"]/section[1]/div/div/div[3]/div/div[2]/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once3(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[3]/div/div[2]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Selectproducts3(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[3]/div/div[5]/form/button[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Daalmakhni(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Daaltadka(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Sambharkit(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[3]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Misalkit(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[4]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusMisalkit(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "load_data"] / div[4] / div[4] / p / a / span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    #SHOPWITHFOOD1#

    def click_food(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/div/div/a[5]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_food1(self):
        element = self.driver.find_element_by_css_selector('#searchhide > div.grocerySpecialSlider.clsFoodSpl.clslowspace > div > div > div > div > a:nth-child(5) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Vajra(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "load_data"] / div[6] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Alutikka(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Chickencholea(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[3]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Gobhi65(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[8]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Vegsamosa(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[11]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

