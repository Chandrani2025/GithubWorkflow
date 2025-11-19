from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class PracticePage(BasePage):
    CHECKBOX = (By.ID, "checkBoxOption1")
    DROPDOWN = (By.ID, "dropdown-class-example")
    RADIO_OPTION = (By.XPATH, "//input[@value='radio2']")
    ALERT_BUTTON = (By.ID, "alertbtn")
    CONFIRM_BUTTON = (By.ID, "confirmbtn")
    SUGGESTION_INPUT = (By.ID, "autocomplete")
    SUGGESTION_LIST_ITEMS = (By.XPATH, "//ul[contains(@class,'ui-menu')]/li")

    def open(self, base_url: str):
        super().open(base_url)

    def check_checkbox(self):
        self.click(self.CHECKBOX)

    def is_checkbox_selected(self):
        return self.find(self.CHECKBOX).is_selected()

    def select_dropdown(self, value: str):
        el = self.find(self.DROPDOWN)
        Select(el).select_by_visible_text(value)

    def get_selected_dropdown_text(self):
        el = self.find(self.DROPDOWN)
        return Select(el).first_selected_option.text.strip()

    def select_radio(self):
        self.click(self.RADIO_OPTION)

    def is_radio_selected(self):
        return self.find(self.RADIO_OPTION).is_selected()

    def trigger_alert_and_accept(self):
        self.click(self.ALERT_BUTTON)
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def trigger_confirm_and_dismiss(self):
        self.click(self.CONFIRM_BUTTON)
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.dismiss()
        return text

    def type_suggestion(self, text: str):
        self.type(self.SUGGESTION_INPUT, text)

    def get_suggestion_value(self):
        return self.find(self.SUGGESTION_INPUT).get_attribute("value")

    def select_suggestion_by_index(self, index: int = 1):
        from selenium.webdriver.support import expected_conditions as EC

        items = self.wait.until(EC.presence_of_all_elements_located(self.SUGGESTION_LIST_ITEMS))
        if not items:
            raise RuntimeError("No suggestion items found")
        if index <= 0:
            raise IndexError("Index must be >= 1")
        target = items[index - 1] if index <= len(items) else items[-1]
        target.click()
