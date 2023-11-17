*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  matti
    Set Password  meika123
    Set Password Confirmation  meika123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  meikalainen123
    Set Password Confirmation  meikalainen123
    Submit Credentials
    Register Should Fail With Message  Username has to contain 3 characters or more

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  matti
    Set Password  meikalainen
    Set Password Confirmation  meikalainen
    Submit Credentials
    Register Should Fail With Message  Password must contain other characters

Register With Nonmatching Password And Password Confirmation
    Set Username  matti
    Set Password  meika123
    Set Password Confirmation  meika456
    Submit Credentials
    Register Should Fail With Message  Passwords are not matching

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}
    
Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register
    
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open