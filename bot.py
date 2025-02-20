from DrissionPage import Chromium,ChromiumOptions
from loguru import logger
from OKXWallet import login_with_private_key
import os

def work(private_key):
    co = ChromiumOptions()
    co.auto_port()
    # 添加插件（path放路径）
    co.add_extension(
        path=r"./extension/okxWallet/3.37.0_1")
    # 配置浏览器信息
    browser = Chromium(addr_or_opts=co)
    tab1 = browser.new_tab()
    #等待插件加载
    tab1.wait(10)
    logger.info('打开okx钱包页面')
    wallet_login = login_with_private_key(private_key=private_key, page_info=tab1)
    if not wallet_login:
        browser.quit()
        logger.error('钱包登录失败')
        return False
    browser.close_tabs(tab1, True)
    tab2 = browser.new_tab()
    tab2.get('https://app.nexus.xyz/')
    tab2.ele('xpath:/html/body/div[3]/div[2]/main/main/div[2]/div/div/div[2]/div[1]/div/div/div/div').click()
    #处理shadowroot窗口
    sr_ele = tab2.ele('xpath:/html/body/div[14]/div').shadow_root
    connect_button = sr_ele.ele('xpath://div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[4]')
    if connect_button:
        connect_button.click()
    okx_button = sr_ele.ele('xpath=//div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[3]/div/button[1]')
    if okx_button:
        okx_button.click()
    connect = tab1.ele('@@tag():button@@text():连接')
    if connect:
        connect.click()
    select_newwork = sr_ele.ele('xpath://div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/button')
    if select_newwork:
        select_newwork.click()
    shouquan = tab1.ele('@text():授权')
    if shouquan:
        shouquan.click()
    queding = tab1.ele('xpath:/html/body/div[1]/div/div/div/div/div/div[4]/div/button[2]')
    if queding:
        queding.click()
    try:
        continue_button = sr_ele.ele('xpath://div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/form/button')
        if continue_button:
            continue_button.click()
    except:
        logger.info('已经注册过')
    script = """
function checkAndClick() {

    const outerDiv = document.querySelector('div.relative.w-24.h-16'); 
 
    if (outerDiv) {

        const hasWhiteBackground = outerDiv.classList.contains('bg-[#ffffff]'); 
 
        if (hasWhiteBackground) {
            console.log("Detected  bg-[#ffffff], clicking the element...");
            outerDiv.click(); 
            console.log("Outer  div clicked!");
        } else {
            console.log("bg-[#ffffff]  not detected, waiting...");
        }
    } else {
        console.error("Outer  div not found!");
    }
}
const intervalId = setInterval(checkAndClick, 5000); 
    """
    tab2.run_js(script)

if __name__ == '__main__':
    keyfile = os.path.abspath('private_key.txt')
    # 获取用户输入
    a = int(input("请输入开始的值: "))
    b = int(input("请输入结束的值: "))

    # 读取txt文件
    try:
        with open(keyfile, "r") as file:
            lines = file.readlines()

            # 检查输入的行数是否在文件的范围内
            if a <= len(lines) and b <= len(lines):
                # 输出对应行数的数据
                for line in lines[a - 1:b]:  # 使用切片获取a到b行（包含a, 不包含b）
                    logger.info(f'开始挂机，私钥为：{line.strip()}')
                    try:
                        work(private_key=line.strip())
                    except:
                        logger.error("挂机失败")
            else:
                logger.error("输入的行数超出了文件的范围")
    except FileNotFoundError:
        logger.error("文件未找到，请检查文件路径")
