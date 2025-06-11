import concurrent.futures
import subprocess
from time import sleep

from tools.android_controller import AndroidController

def get_connected_devices():
    # 执行 adb devices 命令
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)

    # 解析输出
    lines = result.stdout.strip().split('\n')

    # 跳过第一行（标题行）
    lines = lines[1:]

    # 提取设备 ID
    device_list = []
    for line in lines:
        if line:
            device_id = line.split()[0]
            device_list.append(device_id)

    return device_list


def main(device):
    controller = AndroidController(device)
    # 打开设置页面
    controller.open_settings()
    # 暂停0.5秒
    sleep(0.5)
    # 滑动屏幕到底部
    controller.scroll()
    # 暂停0.5秒
    sleep(0.5)
    controller.clickText('系统与更新')
    sleep(0.5)
    controller.clickText('开发者选项')
    sleep(1)
    controller.set_developer_option_switch_state('不使用锁屏', True)
    sleep(0.5)
    controller.set_developer_option_switch_state('充电时屏幕不休眠', True)
    sleep(0.5)
    controller.set_developer_option_switch_state('系统自动更新', False)
    sleep(0.5)
    controller.swipExt('up',1)
    controller.swipExt('up', 1)
    sleep(0.5)
    controller.set_developer_option_switch_state('停用 adb 授权超时功能', True)
    sleep(0.5)
    controller.set_developer_option_switch_state('通过 USB 验证应用', True)
    sleep(0.5)
    controller.home()
    sleep(0.5)
    controller.uninstall_all_apps()


if __name__ == '__main__':
    devices = get_connected_devices()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for device_id in devices:
            executor.submit(main, device_id)
