from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    Full_Name = (By.CSS_SELECTOR, 'input[id="userName"]')
    Email = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    Current_Address = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    Permanent_Address = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    Submit = (By.CSS_SELECTOR, 'button[id="submit"]')


    #create form

    Created_Full_Name = (By.CSS_SELECTOR, '#output #name')
    Created_Email = (By.CSS_SELECTOR, '#output #email')
    Created_Current_Address = (By.CSS_SELECTOR, '#output #currentAddress')
    Created_Permanent_Address = (By.CSS_SELECTOR, '#output #permanentAddress')


