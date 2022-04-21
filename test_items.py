import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_addToBasketButton(browser):
    browser.get(link)
    time.sleep(10)
    basket = browser.find_elements_by_css_selector("button.btn")
    assert basket, "Button not found"