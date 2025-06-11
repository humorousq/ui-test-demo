import os.path

import uiautomator2 as u2


class AndroidController:
    def __init__(self, serial):
        self.serial = serial
        self.device = u2.connect(serial)
        self.width, self.height = self.device.window_size()

    def get_app_list(self):
        self.device.app_list()

    def uninstall_all_apps(self):
        # 卸载所有应用
        # 获取所有已安装的应用列表
        for app in self.device.app_list():
            print(f'设备{self.serial} 开始卸载应用: {app}')
            res = self.device.app_uninstall(app)
            print(f'设备{self.serial} 卸载应用: {app} 结果: {res}')

    def uninstall_app(self, package_name):
        return self.device.app_uninstall(package_name)

    def open_settings(self):
        self.device.shell('am start -a android.settings.SETTINGS')

    def scroll(self, steps=10):
        self.device(scrollable=True).scroll(steps=steps)

    def clickText(self, text):
        element = self.device(text=text)
        if element.exists:
            print(f'找到文本为{text}的元素')
            res = element.click()
            print(f'点击文本为{text}的元素结果: {res}')
        else:
            print(f'未找到文本为{text}的元素')

    def set_developer_option_switch_state(self, name, target_state):
        xpath = f'//android.widget.TextView[@text="{name}"]/../../android.widget.LinearLayout/android.widget.Switch'
        switch = self.device.xpath(xpath)
        if not switch.exists:
            print(f"未找到Switch控件: {name}")
            return False
        # 获取开关状态
        is_checked = switch.info.get('checked', False)
        print(f"{name} Switch状态: {'开启' if is_checked else '关闭'} 目标状态: {'开启' if target_state else '关闭'}")
        if is_checked != target_state:  # target_state是你需要的状态
            switch.click()
        else:
            print(f"Switch状态已经是{target_state}")
        return True

    def export_xml(self, root_path, file_name):
        xml_content = self.device.dump_hierarchy()
        file_path = os.path.join(root_path, file_name + '.xml')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(xml_content)
        return file_path

    def swipExt(self, direction, scale=0.2):
        self.device.swipe_ext(direction, scale)

    def home(self):
        self.device.press('home')

    def click_by_path(self, path):
        element = self.device.xpath(path)
        if element.exists:
            print(f'找到路径为{path}的元素')
            res = element.click()
            print(f'点击路径为{path}的元素结果: {res}')
        else:
            print(f'未找到路径为{path}的元素')
