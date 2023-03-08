import time
from selenium.webdriver.support.wait import WebDriverWait
from Data import url, streetName, buildingNumber, phoneNumber, name
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.EdgeOptions()
from selenium.webdriver.common.by import By

#укажите свой absolute path на msedgedriver
driver = webdriver.Edge(
    executable_path="/Users/evelina/PycharmProjects/testTaskPython/Edge/msedgedriver"
)
try:
    driver.get(url=url)
    driver.fullscreen_window()
    time.sleep(5)

    okBtn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[10]/div/div/span[2]')
    okBtn.click()
    inputStreet = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div/div[1]/input',
    )
    inputStreet.click()
    inputStreet.send_keys(streetName)
    time.sleep(3)
    inputStreet.send_keys(Keys.ENTER)
    inputBuilding = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/input',
    )
    inputBuilding.send_keys(buildingNumber)
    radioBtn = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[1]',
    )
    radioBtn.click()
    apartmentBtn = driver.find_element(
        By.XPATH, '//*[@id="forSelectField"]/div[1]/div/div/div/ul/li[1]'
    )
    apartmentBtn.click()
    findBtn = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div',
    )
    findBtn.click()
    time.sleep(5)
    close = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div'
    )
    close.click()
    time.sleep(1)
    for i in range(0, 5):
        connectPromo = driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[1]/div[6]/div/div/div[2]/div[2]/a',
        )
        connectPromo.click()
        time.sleep(3)
        inputName = driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[2]/div/div[2]/input',
        )
        inputName.send_keys(name)
        inputPhone = driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[3]/div/div[2]/input',
        )
        inputPhone.send_keys(phoneNumber)
        sendApp = driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form/div/div[5]',
        )
        sendApp.click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div[1]/form')
            )
        )
        driver.back()
        print(" - Успешная отправка заявки №  " + str(i + 1))

except Exception as ex:

    print(ex)
finally:
    driver.close()
    driver.quit()

    # Соискатель Мамутов Руслан