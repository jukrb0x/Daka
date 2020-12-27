# :performing_arts: Daka

**XMUM Covid-19 daily health Automated Check-in**

厦门大学马来西亚分校**一键**每日健康**打卡**脚本

Version `0.2`

This is an automated Python(3.7+) script of filling out the forms for Xiamen University Malaysia Covid-19 health Check-in

Simple code, based on [Microsoft Playwright](https://github.com/microsoft/playwright-python), **no browser simulation**(playwright) on `Version 1.0` _// TODO_

The script will help you filling out the forms and print the feedback.

## :face_with_thermometer: Important Attention

:warning: **Please noted** that this handsfree script is only for students who are in the good physical condition, If you have any symptoms, **please fill out the form according to the actual situation** and seek medical attention. :hospital: Wear mask and stay safe, keep away from the crowds, we are all fighting alongside you in this anti-epidemic.

:warning: **请注意**，本自动打卡脚本只限于身体状况实际符合健康标准的同学使用，如果你的身体状况不佳，请手动点击下方的链接如实填报，并寻求相应的医疗帮助 :hospital: 。戴好口罩，保持健康，远离人群，我们与你同在。

[The link to the form 厦门大学马来西亚分校健康打卡](https://forms.office.com/Pages/ResponsePage.aspx?id=00dqnpUnl0ueUnixBgYp8Stmu_7GloVGt3cAK35kmChUMkU5QzRHV1kxQlpCN0dIQk9NSUdEWUQ3WC4u)

## 🦕 Demo

![Demo GIF](static/demo.gif)

# :beers: Getting Started

**Requirement:** The shell environment of python shall be higher than **3.7** for Playwright.

Download the python script `daka.py`.

## :package: Install Playwright-python

Playwright module

```shell
pip install playwright
```

Browser supporting drivers

```shell
# it may take a while to install, depending on network conditions
python -m playwright install
```

## :gear: Configure the email and password

You will configure the account info of email and password accordingly by yourself.

```python
# Account info 账号信息
email = "YOUR_CAMPUS_ID@xmu.edu.my"
pwd = "YOUR_PASSWORD"
```

## :ticket: Email receipt option

You can choose to receive the email receipt or not.
The option only accepted `True` or `False`, right after the lines of account information. `True` by default.

```python
# Send email receipt 发送邮件回执
# Options: True/False
SEND_EMAIL = True
```

## :shell: Run the script

Now run and free up your hands!

```shell
# in the directory of python script
python daka.py
```

:taco: After filling, you will see the thank-you message on the shell~

## :bird: TODO

- [x] Collect thank-you message
- [ ] Testing if filled out first
- [ ] GUI
- [ ] Telegram Bot
- [ ] **A script without browser simulation**
