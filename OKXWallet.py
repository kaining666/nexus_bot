import time
import random
from loguru import logger

def login_with_private_key(private_key,page_info):

    tab1 = page_info
    tab1.get('chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html')
    input_button = tab1.ele('@@tag():button@@text():导入已有钱包')
    if input_button:
        input_button.click()
        time.sleep(random.random())

    private_key_button = tab1.ele('@text():助记词或私钥')
    if private_key_button:
        private_key_button.click()
        time.sleep(random.random())

    #点击私钥按钮，页面元素复杂使用xpath
    private1 = tab1.ele('xpath:/html/body/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[2]')
    if private1:
        private1.click()
        time.sleep(random.random())

    private_key_input = tab1.ele('@tag():textarea')
    if private_key_input:
        private_key_input.input(private_key)
        time.sleep(3)

    yes_button = tab1.ele('@@data-testid=okd-button@@text():确认')
    if yes_button:
        yes_button.click()
        time.sleep(2)
        logger.info(f'私钥输入成功')

    yes_button2= tab1.ele('@@data-testid=okd-button@@text():确认')
    if yes_button2:
        yes_button2.click()
        time.sleep(random.random())

    yanzheng_button = tab1.ele('@text():密码验证')
    if yanzheng_button:
        yanzheng_button.click()
        time.sleep(random.random())

    next_step = tab1.ele('@@tag():button@@text():下一步')
    if next_step:
        next_step.click()
        time.sleep(random.random())

    #输入钱包的密码
    input_pwd = tab1.ele('xpath:/html/body/div/div/div[1]/div/div[2]/form/div[1]/div[2]/div/div/div/div/input')
    if input_pwd:
        input_pwd.input('asdfzxcv')
        time.sleep(random.random())
    #确认钱包密码
    input_pwd1 = tab1.ele('xpath:/html/body/div/div/div[1]/div/div[2]/form/div[3]/div[2]/div/div/div/div/input')
    if input_pwd1:
        input_pwd1.input('asdfzxcv')
        time.sleep(random.random())
    #提交
    yes_button3 = tab1.ele('@@data-testid=okd-button@@text():确认')
    if yes_button3:
        yes_button3.click()
        time.sleep(random.random())
        logger.info(f'设置钱包密码成功')

    #选择导入evm网络
    evm_button = tab1.ele('@@tag():span@@text()：EVM 网络')
    if evm_button:
        evm_button.click()
        time.sleep(random.random())

    yes_button3= tab1.ele('@@data-testid=okd-button@@text():确认')
    if yes_button3:
        yes_button3.click()
        time.sleep(random.random())

    # button_final = tab1.ele('@@data-testid=okd-button@@text():开启你的 Web3 之旅')
    # if button_final:
    #     button_final.click()
    logger.success(f'使用私钥登陆okx钱包成功')
    return True
