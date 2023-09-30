from behave import *

from features.HelperClass.LoginPage import loginPage

@given(u'web page is launched')
def step_impl(context):
    context.login = loginPage(context.driver)
    context.status = context.login.checkWebPageIsDisplayed()
    assert context.status, "Web page is not displayed"

@then(u'User enters valid credentials "{user}"')
def step_impl(context, user):
    context.login.enterTextInUserNameAndPasswordField(user)

@then(u'login screen should be displayed')
def step_impl(context):
    pass

@when(u'clciked on Hamburger menu icon')
def step_impl(context):
    pass

@then(u'Logout option should be displayed')
def step_impl(context):
    pass

@when(u'clicked on LogOut button')
def step_impl(context):
    pass


@then(u'Login screen is displayed')
def step_impl(context):
    pass

