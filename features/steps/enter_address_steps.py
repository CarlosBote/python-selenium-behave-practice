from behave import given

from pages.habi_home_page import habiHomePage


@given("I browse to home page")
def browse_to_url(context):
    habi_home_page = habiHomePage(context.browser)
    context.browser.get(habi_home_page.url)

