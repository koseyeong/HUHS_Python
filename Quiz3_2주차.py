site = "http://naver.com"
site = site.replace("http://", "")
site = site.replace(".com", "") #site = site[:site.index(".")]

password = site[:3] + str(len(site)) + str(site.count('e')) + "!"
print(password)