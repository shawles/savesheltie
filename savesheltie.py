#!/usr/bin/python3
import urllib.request
import json
import random
import webbrowser

import skimage
from skimage.io import imsave, imread
from skimage.transform import resize


def get_response(url):
	page = urllib.request.urlopen(url)
	text = page.read().decode("utf-8")
	return json.loads(text)

def get_str_likes(x):
	if (x >= 100):
		return "99" + str(x)
	elif (x < 10):
		return "0" + str(x)
	else:
		return str(x)

IMG_SIZE = 512
NUM_POSTS = 10


DOMAIN = "pusheltie"
URL = "https://api.vk.com/method/wall.get?domain=" + DOMAIN + "&access_token=831749168317491683174916108348413b8831783174916dafd0a5f8bc8c5746d323a43" + "&offset=";
 
GROUP_URL = "https://api.vk.com/method/groups.getById?group_id=%s" % DOMAIN
PUBLIC_ID = get_response(GROUP_URL)["response"][0]["gid"]

print(PUBLIC_ID)
print(URL)

POST_URL = "https://vk.com/wall-%s_%%s" % PUBLIC_ID


#likes = get_response(URL % 0)["response"]["items"][0]["likes"]["count"]

#img_num = len(get_response(URL % 0)["response"]["items"][0]["attachments"])

PATH = "/home/shali/pushelties/"

alr = ""
#alr = open(PATH + "gt.txt", 'r').readlines()
#alr.close()

data = open(PATH + "gt.txt", 'a')


for p in range(2, NUM_POSTS):
	get_resp = get_response(URL + str(p) + "&count=1")
	print(get_resp)
	print('\n\n')
	#прикреплено:
	#print(get_resp["response"][1]["attachments"])
	atts = get_resp["response"][1]["attachments"]
	print('ЭЭЭЭ', atts, 'ЭЭЭЭ')
	att_num = len(atts)
	for i in range(att_num):
		if ("photo" in atts[i]):
			#print(get_resp["response"]["items"][0]["attachments"][i]["photo"])
			img_url = atts[i]["photo"]["src_big"]
			img_name = PATH + img_url[len(img_url) - 15:]
			#imgname = PATH + get_str_likes(likes) + img_addr
			#print(p, img_url[len(img_url) - 3:])
			#if ((img_url[len(img_url) - 3:] != 'gif') and (imgname not in alr)):
			#print(imgname)
			data.write(img_name)
			data.write("\n")
			urllib.request.urlretrieve(img_url, img_name)
			#img = imread(imgname)
			#img = resize(img, (IMG_SIZE, IMG_SIZE, 3))
			#imsave(imgname, img)
			
			#print("\n\n\n")

#print("LIKES", get_response(URL % 0)["response"][0]["likes"])
#imsave("shelt.jpg", img)

data.close()

#imgname = str(likes) + "shelt.jpg"

#urllib.request.urlretrieve(img_url, imgname)


