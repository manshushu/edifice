from urllib.request import urlopen
urlopen('https://www.howsmyssl.com/a/check').read()
import ssl
print(urlopen('https://www.howsmyssl.com/a/check', context=ssl._create_unverified_context()).read())