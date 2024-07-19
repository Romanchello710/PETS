from selenium.webdriver.common.by import By


# Создал класс локаторов для авторизации на сайте

class LocatorsAuthorization:
    LOGIN_LINK = (By.ID, 'login')                                                               # Локатор логин
    PASSWORD_LINK = (By.XPATH, '//input[@type="password"]')                                     # Локатор пароль
    BATTON_LINK = (By.XPATH, '//div[@id="pv_id_2_content"]/div/form/div[3]/button/span')        # Локатор кнопки - "отправить"


# Создал класс локаторов создания питомца

class LocatorsPets:
    BATTON_PETS=(By.XPATH, "//div[@id='app']/main/div/div/div/div/div/button/span")             # Локатор кнопки - "+"
    PETS_NAME=(By.XPATH, "//input[@id='name']")                                                 # Локатор поля NAME
    AGE_PETS=(By.XPATH, "//span[@id='age']/input")                                              # Локатор поля AGE (возраст)
    TYPE_MENU=(By.XPATH, "//div[2]/div/div/span")                                               # Локатор поля TYPE (вид питомца)
    TYPE_CHOICE=(By.XPATH, "//div[3]/div/ul/li")                                                           # Локатор выбора вида питомца
    GENDER_MENU=(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div/div/span")                        # Локатор поля GENDER (возраст питомца)
    GENDER_CHOICE=(By.XPATH, "//div[3]/div/ul/li[2]")                                           # Локатор выбора пола питомца
    SUBMIT_PETS=(By.XPATH, "/html/body/div[1]/main/div/div/form/div/div[2]/div[3]/button[1]")   # Локатор кнопки - "SUBMIT"

    