# 尝试通过 url 的方式保存图片信息
import requests
from io import BytesIO
from PIL import Image
import uuid

# 函数名称
def save_img_from_url(url_path,save_path):
    req=requests.get(url_path)
    
    #使用BytesIO接口
    image=Image.open(BytesIO(req.content))
    fileName=str(uuid.uuid4())+'.'+image.format.lower()
    print ('file name -->',fileName)
    
    with open(save_path + '/' +fileName,'wb') as f:
        f.write(req.content)
        
if __name__ == "__main__":
    img_url = 'https://img0.baidu.com/it/u=3101694723,748884042&fm=26&fmt=auto&gp=0.jpg'
    img_save_path = '/Users/kenan/Desktop/test_file/test_video'

    save_img_from_url(img_url,img_save_path)
    
    print ('done!')
    