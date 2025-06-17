import concurrent.futures
import subprocess


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


def main(serial):
    subprocess.run(['scrcpy', '-s', serial], capture_output=True, text=True)


if __name__ == '__main__':
    devices = get_connected_devices()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for device_id in devices:
            executor.submit(main, device_id)
