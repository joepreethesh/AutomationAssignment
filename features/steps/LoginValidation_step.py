import time

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

@then(u'home screen is displayed')
def step_impl(context):
    homeScreenStatus = context.login.loginHomeScreenStatus()
    assert homeScreenStatus, "Unable to login"

@when(u'clciked on Hamburger menu icon')
def step_impl(context):
    context.login.clickOnHamburgerIcon()

@then(u'Logout option should be displayed')
def step_impl(context):
    logoutButtonStatus = context.login.checkLogOutOptionIsDisplayed()
    assert logoutButtonStatus, "LogOut button is not displayed"

@when(u'clicked on LogOut button')
def step_impl(context):
    context.login.clickLogoutButton()


@then(u'Login screen is displayed')
def step_impl(context):
    screenStatus = context.login.loginScreenStatusAfterLogout()
    assert screenStatus, "Login screen is not displayed after logout"

@then(u'User clicks on Login Button')
def step_impl(context):
    context.login.clickOnLoginButton()

@then(u'User enters Invalid credentials "{Invaliduser}"')
def step_impl(context, Invaliduser):
    context.login.enterTextInUserNameAndPasswordField(Invaliduser)

@then(u'Error message is displayed')
def step_impl(context):
    time.sleep(5)
    errorPromptStatus = context.login.checkErrorMessageForInvalidLogin()
    assert errorPromptStatus, "Error message is not displayed for Invalid Login"


