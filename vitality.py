import requests

cookies = {
    'SESSION': 'f26281c3-dc03-4a3a-89fc-87f0ed6ac913',
    'XSRF-TOKEN': 'a8f2360e-722f-4b89-bac4-a936f08916bd',
    'visid_incap_1445108': 'q3gC2FGrTtWKiXUTJ+OH5qSCx2UAAAAAQUIPAAAAAADsYNYdOznprmLlNd6hEU+h',
    'okta_override': 'null',
    'MOBILE_APP': 'null',
    'MOBILE_PLATFORM': 'null',
    'OKTA_MOBILE_USER_LOGIN': 'null',
    'mobile_webview': 'null',
    'USER_PRODUCT': 'us',
    'MNCPORTAL_LANGUAGE': 'en',
    '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D',
    '_tracking_consent': '%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%2C%22m%22%3A%22%22%7D%7D%2C%22lim%22%3A%5B%22CMP%22%5D%2C%22region%22%3A%22USFL%22%2C%22v%22%3A%222.1%22%2C%22reg%22%3A%22%22%7D',
    '_shopify_y': 'e4e7e403-8724-4af4-80f2-2245eb146bba',
    '_orig_referrer': 'https%3A%2F%2Fwww.powerofvitality.com%2F',
    '_landing_page': '%2F',
    'nlbi_1445108': 'CNfmHWQBjX3j5DjpFLCm0wAAAAC8+DuLnDBZa5KBNU+BMhph',
    'incap_ses_1596_1445108': '33UvLs596mPQvZ1MICImFt/sx2UAAAAAdaiWHEFWDqJ3mxdQu2IJ/w==',
    'okta_redirect_uri': 'https://www.powerofvitality.com/vitality/login/complete_login',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Feb+10+2024+16%3A38%3A41+GMT-0500+(Eastern+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.powerofvitality.com%2Fvitality%2Flogin&groups=C0003%3A0%2CC0002%3A0%2CC0001%3A1%2CC0004%3A0',
    'okta-oauth-redirect-params': '{%22responseType%22:[%22code%22]%2C%22state%22:%22eLMkshSQwKZ9BHEfHKDQzKHe5zqEoUtCgekDziq4PDRidllet8z5ZgqGVNKbLyp1%22%2C%22nonce%22:%22afy5EdKuHrU3OH2hl9QxXJ0BoFT9J3N2r7xBoTuyUVvhLDOd5LwFuNvSI5xUE6yl%22%2C%22scopes%22:[%22openid%22%2C%22profile%22%2C%22email%22]%2C%22clientId%22:%220oajntygg6PQ8hXAZ5d6%22%2C%22urls%22:{%22issuer%22:%22https://login.powerofvitality.com/oauth2/default%22%2C%22authorizeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/authorize%22%2C%22userinfoUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/userinfo%22%2C%22tokenUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/token%22%2C%22revokeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/revoke%22%2C%22logoutUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/logout%22}%2C%22ignoreSignature%22:false}',
    'okta-oauth-nonce': 'afy5EdKuHrU3OH2hl9QxXJ0BoFT9J3N2r7xBoTuyUVvhLDOd5LwFuNvSI5xUE6yl',
    'okta-oauth-state': 'eLMkshSQwKZ9BHEfHKDQzKHe5zqEoUtCgekDziq4PDRidllet8z5ZgqGVNKbLyp1',
    'ROUTEID': '.tkgch2',
    'VITALITYPORTAL_WD_WLJSESSIONID': 'z3CU9ZmXDD6zkfCGEAaJX-LRuEvOrqLPJSa3j_GbyBnRF4aLtGDF!-1456948109',
    'reese84': '3:cbaOdase01anyTOZ25iVmw==:0NVKxlH4c/yqOj9FxUIQk8ouDfpvLHCL40YQgPZ+vOHRcTrHcz/4i7TZ02HTUS/bKONm9mEsm3hyILjM3C0qxTpALzfDTa/vhOF/spSK8TIR2mYK+Xj7h9dTjuxjqz2M2cKtBfH4g9AYmQ8/v5y7guzbRWHvHCK4+4IzCNJZoGT0u0Eazym8nYVaVG6jxJSONfQv+7lBeyt+0XI76QdM5W5fj4MbvNHksNxGC62ar3wT/NFTPKot8A8beRkcbf2SOgHj1ABg0Uuozxk59BlkX9Y9H1ScIfJlbPAKJvLuQ5DtJRVtAYmrEx/RiZMt5D83mYeqTwlDGghAuyw0T17LoEUfs14qp48BWHpwFyVHS2Z6w7DBr++Xwewy3YbzR+dpWTmi4LfJ9WkefaCOcmwNYw3keLHSeBym9RL+lgZhwctRZ962jOzbs/0IYVur0aAzT9X6S3DoPDAzOv4H4dZu0gNtuSRiq0Ui6nodrGXZ/i4=:09MyRdDoJHojoocZfNYN2fVbuXLiX1DDSgcbi/Mf8Us=',
    'nlbi_1445108_2147483392': 'Mw4BIvhH4nDjulTtFLCm0wAAAAAP3wARj8yXP8k6SDiX+s4J',
    'dtCookie': 'v_4_srv_3_sn_34402444BA5FD7A915148E8EBB3AB11D_perc_100000_ol_0_mul_1_app-3Aa300a63665cac321_1_app-3Af705364a6360debd_1_app-3A2c36208e7dc0785b_1_rcs-3Acss_0',
}

headers = {
    'authority': 'www.powerofvitality.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,es;q=0.8',
    # 'content-length': '0',
    # 'cookie': 'SESSION=f26281c3-dc03-4a3a-89fc-87f0ed6ac913; XSRF-TOKEN=a8f2360e-722f-4b89-bac4-a936f08916bd; visid_incap_1445108=q3gC2FGrTtWKiXUTJ+OH5qSCx2UAAAAAQUIPAAAAAADsYNYdOznprmLlNd6hEU+h; okta_override=null; MOBILE_APP=null; MOBILE_PLATFORM=null; OKTA_MOBILE_USER_LOGIN=null; mobile_webview=null; USER_PRODUCT=us; MNCPORTAL_LANGUAGE=en; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%2C%22m%22%3A%22%22%7D%7D%2C%22lim%22%3A%5B%22CMP%22%5D%2C%22region%22%3A%22USFL%22%2C%22v%22%3A%222.1%22%2C%22reg%22%3A%22%22%7D; _shopify_y=e4e7e403-8724-4af4-80f2-2245eb146bba; _orig_referrer=https%3A%2F%2Fwww.powerofvitality.com%2F; _landing_page=%2F; nlbi_1445108=CNfmHWQBjX3j5DjpFLCm0wAAAAC8+DuLnDBZa5KBNU+BMhph; incap_ses_1596_1445108=33UvLs596mPQvZ1MICImFt/sx2UAAAAAdaiWHEFWDqJ3mxdQu2IJ/w==; okta_redirect_uri=https://www.powerofvitality.com/vitality/login/complete_login; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+10+2024+16%3A38%3A41+GMT-0500+(Eastern+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.powerofvitality.com%2Fvitality%2Flogin&groups=C0003%3A0%2CC0002%3A0%2CC0001%3A1%2CC0004%3A0; okta-oauth-redirect-params={%22responseType%22:[%22code%22]%2C%22state%22:%22eLMkshSQwKZ9BHEfHKDQzKHe5zqEoUtCgekDziq4PDRidllet8z5ZgqGVNKbLyp1%22%2C%22nonce%22:%22afy5EdKuHrU3OH2hl9QxXJ0BoFT9J3N2r7xBoTuyUVvhLDOd5LwFuNvSI5xUE6yl%22%2C%22scopes%22:[%22openid%22%2C%22profile%22%2C%22email%22]%2C%22clientId%22:%220oajntygg6PQ8hXAZ5d6%22%2C%22urls%22:{%22issuer%22:%22https://login.powerofvitality.com/oauth2/default%22%2C%22authorizeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/authorize%22%2C%22userinfoUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/userinfo%22%2C%22tokenUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/token%22%2C%22revokeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/revoke%22%2C%22logoutUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/logout%22}%2C%22ignoreSignature%22:false}; okta-oauth-nonce=afy5EdKuHrU3OH2hl9QxXJ0BoFT9J3N2r7xBoTuyUVvhLDOd5LwFuNvSI5xUE6yl; okta-oauth-state=eLMkshSQwKZ9BHEfHKDQzKHe5zqEoUtCgekDziq4PDRidllet8z5ZgqGVNKbLyp1; ROUTEID=.tkgch2; VITALITYPORTAL_WD_WLJSESSIONID=z3CU9ZmXDD6zkfCGEAaJX-LRuEvOrqLPJSa3j_GbyBnRF4aLtGDF!-1456948109; reese84=3:cbaOdase01anyTOZ25iVmw==:0NVKxlH4c/yqOj9FxUIQk8ouDfpvLHCL40YQgPZ+vOHRcTrHcz/4i7TZ02HTUS/bKONm9mEsm3hyILjM3C0qxTpALzfDTa/vhOF/spSK8TIR2mYK+Xj7h9dTjuxjqz2M2cKtBfH4g9AYmQ8/v5y7guzbRWHvHCK4+4IzCNJZoGT0u0Eazym8nYVaVG6jxJSONfQv+7lBeyt+0XI76QdM5W5fj4MbvNHksNxGC62ar3wT/NFTPKot8A8beRkcbf2SOgHj1ABg0Uuozxk59BlkX9Y9H1ScIfJlbPAKJvLuQ5DtJRVtAYmrEx/RiZMt5D83mYeqTwlDGghAuyw0T17LoEUfs14qp48BWHpwFyVHS2Z6w7DBr++Xwewy3YbzR+dpWTmi4LfJ9WkefaCOcmwNYw3keLHSeBym9RL+lgZhwctRZ962jOzbs/0IYVur0aAzT9X6S3DoPDAzOv4H4dZu0gNtuSRiq0Ui6nodrGXZ/i4=:09MyRdDoJHojoocZfNYN2fVbuXLiX1DDSgcbi/Mf8Us=; nlbi_1445108_2147483392=Mw4BIvhH4nDjulTtFLCm0wAAAAAP3wARj8yXP8k6SDiX+s4J; dtCookie=v_4_srv_3_sn_34402444BA5FD7A915148E8EBB3AB11D_perc_100000_ol_0_mul_1_app-3Aa300a63665cac321_1_app-3Af705364a6360debd_1_app-3A2c36208e7dc0785b_1_rcs-3Acss_0',
    'origin': 'https://www.powerofvitality.com',
    'referer': 'https://www.powerofvitality.com/v3/employee-portal/home/activities/Workouts/25694501/Gym%20workout/Self%20captured?form=gymworkout&entryPoint=Workouts',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'translate-to': 'EN_US',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-xsrf-token': 'a8f2360e-722f-4b89-bac4-a936f08916bd',
}

params = {
    'programEnrolmentCohortActivityId': '25694501',
    'activityValue': 'crunch',
    'date': '2024-01-01T05:00:00.062Z',
}

response = requests.post(
    'https://www.powerofvitality.com/v3/bff/activity/api/v1/program-enrolment-cohort-activity/activity/complete',
    params=params,
    cookies=cookies,
    headers=headers,
)

for day in range (1,28):
    day_long = f'0{day}' if day < 10 else str(day)
    params = {
        'programEnrolmentCohortActivityId': '25694501',
        'activityValue': 'crunch',
        'date': f'2024-03-{day_long}T05:00:00.062Z',
    }
    
    response = requests.post(
        'https://www.powerofvitality.com/v3/bff/activity/api/v1/program-enrolment-cohort-activity/activity/complete',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(f'{day_long} - {response.status_code}')
