# :performing_arts: Daka

**XMUM Automated Covid-19 daily health Check-in**

Version `0.1`

This is an automated Python(3.7+) script of filling out the forms for Xiamen University Malaysia Covid-19 health Check-in

[The link to the form](https://forms.office.com/Pages/ResponsePage.aspx?id=00dqnpUnl0ueUnixBgYp8Stmu_7GloVGt3cAK35kmChUMkU5QzRHV1kxQlpCN0dIQk9NSUdEWUQ3WC4u)

Simple Code, based on [Microsoft Playwright](https://github.com/microsoft/playwright-python), no browser simulation(playwright) on `Version 1.0` // TODO

The script will help you filling out the forms and print the feedback.

## 🦕 Demo

We will have one here!!

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

- [ ] Collect thank you
- [ ] Testing if filled out first
- [ ] Telegram Bot
- [ ] **A script without browser simulation**