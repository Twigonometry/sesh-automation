import requests

#GET the SESH page contents

print("\n======== GET Request ========\n")

sesh_get = requests.get("https://www.shefesh.com")
print(sesh_get.text)

#make a basic POST request

print("\n======== POST Request ========\n")

bin_post = requests.post('https://httpbin.org/post', data={'our_param':'our_value'})
print(bin_post.text)