
# Appium automation test for basic IOS app


**Prerequsite**
1. Xcode 9.4.1 or later installed on your macOS
2. Appium application( installed by GUI/ CMI)
   ```shell
   npm install -g appium
    ``` 
3. Python - there are many ways to do this but i use brew for mac
   ```shell
   brew install python
    ``` 
4. Appium-Python-Client
   ```shell
   pip install Appium-Python-Client
    ``` 
5. pytest
   ```shell
   pip install -U pytest
    ``` 
6. carthage
   ```shell
   brew install carthage
    ```     
7. DEMO IOS Application
   Find a demo app with source code to work with or build yours.
   in this case i used the demo app i found at https://www.appcoda.com

**To run Code**

1. Install all the pre-requsite applications
2. Copy files in this project
3. Go to the /tests/
4. Run
    ```python
    pytest test_login.py
    ``` 
**Improvements**
 
This is just the basic from the tutorial at https://www.appcoda.com.
There a number of things i can add to make this into a proper framework.
As i get time and add the improvements i will remove from the list.
1. Add a reporting framework ie Allure
2. Reorder code in a page object model structure
3. Multi ios device screen size support. extend code so it runs
on different simulator ios device size
4. Optional real device support
5. Auto record screenshots of fails
6. support for browserstack


**Credits**

i started this small project based on a tutorial by 
Lawrence Tan @ https://www.appcoda.com

