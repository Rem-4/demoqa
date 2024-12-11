from pages.text_box import TextBox
import time
def test_check_text(browser):
    text_box = TextBox(browser)
    example_1 = 'Ivan'
    example_2 = 'Ivanov'
    text_box.visit()
    text_box.full_name.clear()
    text_box.current_address.clear()
    text_box.full_name.send_keys(example_1)
    text_box.current_address.send_keys(example_2)
    time.sleep(3)
    text_box.btn_submit.click_force()
    text_box.text_output_current_address.scroll_to_elements()
    time.sleep(3)
    assert text_box.text_output_name.get_text() == 'Name:' + example_1
    assert text_box.text_output_current_address.get_text() == 'Current Address :' + example_2