from behave import given, when, then
from features.pages.practice_page import PracticePage


@given("I open the practice page")
def step_open_practice(context):
    context.page = PracticePage(context.driver)
    context.page.open(context.base_url)
    title = context.driver.title
    assert "Practice" in title or "AutomationPractice" in context.base_url


@then("I select the checkbox")
def step_select_checkbox(context):
    context.page.check_checkbox()
    assert context.page.is_checkbox_selected(), "Checkbox should be selected"


@then("I select the radio option")
def step_select_radio(context):
    context.page.select_radio()
    assert context.page.is_radio_selected(), "Radio should be selected"


@when('I select dropdown value "{value}"')
def step_select_dropdown(context, value):
    context.page.select_dropdown(value)
    actual = context.page.get_selected_dropdown_text()
    assert actual == value, f"Expected dropdown {value}, got {actual}"


@when('I type suggestion "{text}"')
def step_type_suggestion(context, text):
    context.page.type_suggestion(text)
    val = context.page.get_suggestion_value()
    assert val.lower().startswith(text.lower()), f"Suggestion value {val} does not start with {text}"


@when('I select second suggestion from the list')
def step_select_second_suggestion(context):
    context.page.select_suggestion_by_index(2)


@then('the selected dropdown should be "{expected}"')
def step_verify_dropdown(context, expected):
    actual = context.page.get_selected_dropdown_text()
    assert actual == expected, f"Expected dropdown '{expected}', got '{actual}'"
