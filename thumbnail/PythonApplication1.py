import requests
import re
import os
import random
def getImg():
    url='https://bing.ioliu.cn/?p='    #图片对应的网站
    pattern=r'http://h1.ioliu.cn/bing/.+?(jpg|png)'    #匹配图片的正则
    path='./'    #图片存储路径
    r=requests.get(url+str(random.randint(2,100)))
    r.encoding=r.apparent_encoding
    print(r.text)
    mattch=re.finditer(pattern,r.text)
    #print(mattch)
    i=12
    k=0
    for ik in mattch:
        print(1233)
        if(k%3==0):
            img=requests.get(ik.group(0))
            if(not os.path.exists(path)):   #保存图片的路径不存在则创建
                os.mkdir(path)
            if(img.url.endswith('.jpg')):   #不同格式的图片
                with open(path+'/t'+str(i+1)+'.jpg','wb') as f:
                    f.write(img.content)    #将图片保存到本地
                    f.close()       
            else:
                print('爬取失败，图片后缀为：'+img.url[-4:])
            #print('第'+str(i+1)+'次爬取\t成功！')
            i+=1
            if(i>240000): #这里仅爬取12张图片
                break
        k+=1


def main():
    print(123);
    getImg()   
main()
