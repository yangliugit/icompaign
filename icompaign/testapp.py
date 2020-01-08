# -*- coding: utf-8 -*-
from appium import webdriver

desired_caps = {

                'platformName': 'Android',

                'deviceName': '28b6e430',

                'platformVersion': '7.9',

                # apk包名

                'appPackage': 'com.axon.ikeeper',

                # apk的launcherActivity

                'appActivity': 'com.axon.ikeeper.SplashActivity'

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
