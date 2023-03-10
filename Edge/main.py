import time
from selenium.webdriver.support.wait import WebDriverWait
from Data import url, streetName, buildingNumber, phoneNumber, name
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.EdgeOptions()
from selenium.webdriver.common.by import By

# укажите свой absolute path на  msedgedriver
driver = webdriver.Edge(
    executable_path="/Users/evelina/PycharmProjects/testTaskPython/Edge/msedgedriver"
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
    inputStreet.send_keys(Keys.ENTER)
    inputBuilding = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//input[@class="app141 app148 app147 app143 app160"]')
        )
    )

    inputBuilding.click()
    inputBuilding.send_keys(buildingNumber)
    inputBuilding.send_keys(Keys.ENTER)
    radioBtn = driver.find_element(
        By.XPATH,
        '//span[@class="app162 app174"]',
    )
    radioBtn.click()
    apartmentBtn = driver.find_element(By.XPATH, '//li[@class="app186"]')
    apartmentBtn.click()
    findBtn = driver.find_element(
        By.XPATH,
        '//div[@class="app205 app237 app233 app228 app217 app234"]',
    )
    findBtn.click()
    closeBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[@datatest="close_popup1_from_quiz_input_tel"]')
        )
    )

    closeBtn.click()

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
        inputName = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@datatest="providers_provider_order_input_name"]')
            )
        )

        inputName.send_keys(name)
        inputPhone = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@datatest="providers_provider_order_input_tel"]')
            )
        )

        inputPhone.send_keys(phoneNumber)
        sendApp = driver.find_element(
            By.XPATH,
            '//div[@data-test="order_form_input_connect_button"]',
        )
        sendApp.click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form')
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
