import time
from pages.form_page import FormPage
def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('test1')
    form_page.last_name.send_keys('test2')
    form_page.user_email.send_keys('ttt@tt.ru')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('777')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('text')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()