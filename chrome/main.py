import time
from selenium.webdriver.support.wait import WebDriverWait
from Data import url, streetName, buildingNumber, phoneNumber, name
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
from selenium.webdriver.common.by import By

# укажите свой absolute path на  chromedriver
driver = webdriver.Chrome(
    executable_path="/Users/evelina/PycharmProjects/testTaskPython/chrome/chromedriver"
)
try:
    driver.get(url=url)
    driver.fullscreen_window()
    okBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.app623"))
    )
    okBtn.click()
    inputStreet = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//input[@class="app141 app148 app147 app143 app160 app142"]')
        )
    )

    inputStreet.click()
    inputStreet.send_keys(streetName)
    time.sleep(1)
    print("- успешный ввод улицы")
    inputStreet.send_keys(Keys.ENTER)
    inputBuilding = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//input[@class="app141 app148 app147 app143 app160"]')
        )
    )

    inputBuilding.click()
    inputBuilding.send_keys(buildingNumber)
    inputBuilding.send_keys(Keys.ENTER)
    print("- Успешный ввод номера дома")

    radioBtn = driver.find_element(
        By.XPATH,
        '//span[@class="app162 app174"]',
    )
    radioBtn.click()
    apartmentBtn = driver.find_element(By.XPATH, '//li[@class="app186"]')
    apartmentBtn.click()
    print("- Успешный выбор вида итернета")
    findBtn = driver.find_element(
        By.XPATH,
        '//div[@class="app205 app237 app233 app228 app217 app234"]',
    )
    findBtn.click()
    print("- Успешное нажатие кнопки поиска")
    closeBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[@datatest="close_popup1_from_quiz_input_tel"]')
        )
    )

    closeBtn.click()
    print("- Успешное закрытие всплывающего окна")

    for i in range(0, 5):
        connectPromo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//div[@datatest="providers_form_inspect_connect_tariff_button"]',
                )
            )
        )

        connectPromo.click()
        print("- Успешное нажатие кнопки Подключить")
        inputName = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@datatest="providers_provider_order_input_name"]')
            )
        )

        inputName.send_keys(name)
        print("- Успешный ввод имени")
        inputPhone = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@datatest="providers_provider_order_input_tel"]')
            )
        )

        inputPhone.send_keys(phoneNumber)
        print("- Успешный ввод номера")
        sendApp = driver.find_element(
            By.XPATH, '//div[@data-test="order_form_input_connect_button"]'
        )
        sendApp.click()
        succesForm = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@data-test="give_feedback"]')
            )
        )

        print("- Успешная отправка заявки №  " + str(i + 1))
        driver.back()


except Exception as ex:

    print(ex)
finally:
    driver.close()
    driver.quit()

    # Соискатель Мамутов Руслан
