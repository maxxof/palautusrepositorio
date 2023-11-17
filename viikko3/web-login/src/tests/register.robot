*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  matti
    Set Password  meika123
    Set Password Confirmation  meika123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  meikalainen123
    Set Password Confirmation  meikalainen123
    Submit Register Credentials
    Register Should Fail With Message  Username has to contain 3 characters or more

Register With Valid Username And Invalid Password
    Set Username  matti
    Set Password  meikalainen
    Set Password Confirmation  meikalainen
    Submit Register Credentials
    Register Should Fail With Message  Password must contain other characters

Register With Nonmatching Password And Password Confirmation
    Set Username  matti
    Set Password  meika123
    Set Password Confirmation  meika456
    Submit Register Credentials
    Register Should Fail With Message  Passwords are not matching

Login After Successful Registration
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ma
    Set Password  ma123
    Set Password Confirmation  ma123
    Submit Register Credentials
    Register Should Fail With Message  Username has to contain 3 characters or more
    Go To Login Page
    Set Username  ma
    Set Password  ma123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password
    
*** Keywords ***
Submit Register Credentials
    Click Button  Register
    
Register Should Succeed
    Welcome Page Should Be Open

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open