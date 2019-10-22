from removebg import RemoveBg
"""
这个脚本将按照图片原路径返回去除了底色的png无背景图片
"""
api_key = "eihevCjPQhkX3Kwbn38WbLXG"
rmbg = RemoveBg(api_key, 'error.log')
img_path = "C:/Users/qiuli/Desktop"
img_name = input("Your Image Name Here (xxx.png/jpg): \n")

rmbg.remove_background_from_img_file("%s\%s"%(img_path, img_name))