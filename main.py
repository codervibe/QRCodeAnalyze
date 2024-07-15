import pyzxing
from PIL import Image


def decode_qrcode(image_path):
    # 尝试打开二维码图片
    try:
        img = Image.open(image_path)
        # img.show()  # 显示二维码图片，便于确认
    except FileNotFoundError:
        print(f"文件未找到: {image_path}")
        return
    except IOError:
        print(f"无法打开文件: {image_path}")
        return

    # 初始化ZXing二维码解码器
    reader = pyzxing.BarCodeReader()

    # 使用ZXing库对图片进行解码
    result = reader.decode(image_path)

    # 如果解码成功，打印出二维码中的内容
    if result and result[0].get('parsed'):

        raw_data = result[0]['raw']  # 获取原始字节数据
        try:
            # 尝试使用UTF-8解码
            decoded_data = raw_data.decode('utf-8')
        except UnicodeDecodeError:
            try:
                # 尝试使用GBK解码
                decoded_data = raw_data.decode('gbk')
            except UnicodeDecodeError:
                # 尝试使用GB2312解码
                decoded_data = raw_data.decode('gb2312')
        print(f"二维码内容: {decoded_data}")
    else:
        print("未能解码二维码")


if __name__ == "__main__":
    # 获取用户输入的二维码图片路径
    image_path = input("请输入二维码图片的路径: ")

    # 调用解码函数
    decode_qrcode(image_path)
