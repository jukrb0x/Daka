# :performing_arts: Daka

**XMUM Automated Covid-19 daily health Check-in**

Version `0.1`

This is an automated Python(3.7+) script of filling out the forms for Xiamen University Malaysia Covid-19 health Check-in

[The link to the form](https://forms.office.com/Pages/ResponsePage.aspx?id=00dqnpUnl0ueUnixBgYp8Stmu_7GloVGt3cAK35kmChUMkU5QzRHV1kxQlpCN0dIQk9NSUdEWUQ3WC4u)

Simple code, based on [Microsoft Playwright](https://github.com/microsoft/playwright-python), **no browser simulation**(playwright) on `Version 1.0` _// TODO_

The script will help you filling out the forms and print the feedback.

## :face_with_thermometer: Important Attention

:warning: **Please noted** that this handsfree script is only for students who are in the good physical condition, If you have any symptoms, **please fill out the form according to the actual situation** and seek medical attention. :hospital: Stay safe, we are all fighting alongside you in this white war.

## 🦕 Demo

![Demo GIF](static/demo.gif)

# :beers: Getting Started

The shell environment of python shall be higher than **3.7** for Playwright.

## :package: Install Playwright-python

Playwright module

```shell
pip install playwright
```

Browser supporting drivers

```shell
# it may take a white to install due to the network condition
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
