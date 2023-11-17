*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  mattimeika123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kallekainen456
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ma  mattimeika123
    Output Should Contain  Username has to contain 3 characters or more

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  matti123  mattimeika123
    Output Should Contain  Username must contain characters a-z

Register With Valid Username And Too Short Password
    Input Credentials  matti  ma123
    Output Should Contain  Password has to contain 8 characters or more

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  mattimeika
    Output Should Contain  Password must contain other characters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kallekainen123
    Input New Command
