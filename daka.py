from playwright import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Account info 账号信息
    email = "YOUR_CAMPUS_ID@xmu.edu.my"
    pwd = "YOUR_PASSWORD"

    # Send email receipt 发送邮件回执
    # Options: True/False
    SEND_EMAIL = True

    # Open new page
    page = context.newPage()
    form_link = "https://forms.office.com/Pages/ResponsePage.aspx?id=00dqnpUnl0ueUnixBgYp8Stmu_7GloVGt3cAK35kmChUMkU5QzRHV1kxQlpCN0dIQk9NSUdEWUQ3WC4u"
    # Login to Microsoft Office
    page.goto("https://login.microsoftonline.com/")
    email_focus = "input[type=\"email\"]"
    page.click(email_focus)
    page.fill(email_focus, email)
    with page.expect_navigation():
        page.click("input[type=\"submit\"]")
    pwd_focus = "input[type=\"password\"]"
    page.click(pwd_focus)
    page.fill(pwd_focus, pwd)
    with page.expect_navigation():
        page.click("input[type=\"submit\"]")
    # Go to the form page
    page.goto(form_link)

    # TODO: Test if filled out

    # Filling out
    page.click("text=\"中国\"")
    page.click("text=\"与曾输入地址完全一致\"")
    page.click("text=\"低于37.3摄氏度\"")
    page.click("text=\"以上症状均无\"")
    # Receipt option
    if(SEND_EMAIL):
        # FIXME: text => XPath
        page.click("text=/.*Send me an email receipt of my.*/")
    # Submit
    # FIXME: text=>XPath
    page.click("text=\"Submit\"")

    # Get focus
    page.click(".thank-you-page-message")
    print(email, "打卡完成！")

    # Get the thank-you message
    title = page.querySelector(
        "//*[@role=\"log\"]/div[1]/span")
    message = page.querySelector(
        "//*[@role=\"log\"]/div[2]/span")
    # Print the thank-you message
    print("\n", title.innerHTML())
    print("\n", message.innerHTML())

    # TODO: Send to Telegram Bot

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
