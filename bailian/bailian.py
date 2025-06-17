from tools.llms import call_qianwen
from ui_tars.prompt import MOBILE_USE_DOUBAO
if __name__ == "__main__":
    prompt = MOBILE_USE_DOUBAO.format(language="chinese-simplified", instruction="打开设置页面")
    message = [{"role": "system", "content": prompt}, {"role": "user", "content": [
        {"type": "image_url",
         "image_url": {"url": "https://static.yximgs.com/udata/pkg/ks-zzq-demo/1750141050073_9542.jpg"}},
        {"type": "text", "text": "这是手机的截屏，下一步该做什么"}
    ]}]
    print(call_qianwen(message).model_dump_json())
