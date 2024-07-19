from pages.base_page import BasePage
from pages.locators import LocatorsAuthorization, LocatorsPets


class LoginPage(BasePage):
    def go_to_login(self):                                                   # поле логин
        login_email = self.browser.find_element(*LocatorsAuthorization.LOGIN_LINK)
        login_email.send_keys('roman_barn7@mail.ru')

    def go_to_password(self):                                               # поле пароль
        login_password = self.browser.find_element(*LocatorsAuthorization.PASSWORD_LINK)
        login_password.send_keys('Privet250')

    def go_to_submit(self):                                                 # кнопка submit
        login_submit = self.browser.find_element(*LocatorsAuthorization.BATTON_LINK)
        login_submit.submit()

    # Описываем функцию по созданию карточки питомца:

    def go_to_pets(self):                                                   # находим и кликаем по кнопке - "+"
        batton_pets = self.browser.find_element(*LocatorsPets.BATTON_PETS)
        batton_pets.click()

    def go_to_name(self):                                                   # имя питомца
        pets_name = self.browser.find_element(*LocatorsPets.PETS_NAME)
        pets_name.send_keys('BAKSI')

    def go_to_age(self):                                                    # возраст питомца
        pets_age = self.browser.find_element(*LocatorsPets.AGE_PETS)
        pets_age.send_keys('10')

    def go_to_type(self):                                                   # поле вид питомца (дропдаун)
        type_menu=self.browser.find_element(*LocatorsPets.TYPE_MENU)
        type_menu.click()

    def click_type(self):                                                   # выбор питомца
        type_choice=self.browser.find_element(*LocatorsPets.TYPE_CHOICE)
        type_choice.click()

    def go_to_gender(self):                                                 # поле пол питомца
        gender_menu=self.browser.find_element(*LocatorsPets.GENDER_MENU)
        gender_menu.click()

    def click_gender(self):                                                 # выбор пола питомца
        gender_choice=self.browser.find_element(*LocatorsPets.GENDER_CHOICE)
        gender_choice.click()

    def click_submit(self):                                                 # поиск и клик по кнопке submit
        submit_pets=self.browser.find_element(*LocatorsPets.SUBMIT_PETS)
        submit_pets.submit()