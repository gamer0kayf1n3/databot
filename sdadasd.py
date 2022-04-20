Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import beautifulsoup
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import beautifulsoup
ModuleNotFoundError: No module named 'beautifulsoup'
>>> import beautifulsoup4
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import beautifulsoup4
ModuleNotFoundError: No module named 'beautifulsoup4'
>>> from bs4 import BeautifulSoup
>>> import requests
>>> print(requests.get("https://nhentai.net/g/177013").content)

>>> soup = BeautifulSoup(requests.get("https://nhentai.net/g/177013").content, 'html.parser')
>>> soup.meta
<meta charset="utf-8"/>
>>> soup.title
<title>METAMORPHOSIS » nhentai: hentai doujinshi and manga</title>
>>> soup.p
<p><a class="login-comment" href="/login/">Login</a> or <a class="login-comment" href="/register/">register</a> to post a comment.
						</p>
>>> soup.meta.property['og:title']
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    soup.meta.property['og:title']
TypeError: 'NoneType' object is not subscriptable
>>> soup.find_all("meta")
[<meta charset="utf-8"/>, <meta content="#1f1f1f" name="theme-color"/>, <meta content="METAMORPHOSIS" itemprop="name"/>, <meta content="https://t.nhentai.net/galleries/987560/cover.jpg" itemprop="image"/>, <meta content="article" property="og:type"/>, <meta content="METAMORPHOSIS" property="og:title"/>, <meta content="https://t.nhentai.net/galleries/987560/cover.jpg" property="og:image"/>, <meta content="summary" name="twitter:card"/>, <meta content="METAMORPHOSIS" name="twitter:title"/>, <meta content="group, stockings, anal, schoolgirl uniform, nakadashi, blowjob, ahegao, incest, double penetration, dark skin, x-ray, impregnation, mind break, story arc, mmf threesome, pregnant, drugs, prostitution, piercing, blackmail, gyaru, deepthroat, snuff, already uploaded, vomit, moral degeneration, full body tattoo" name="twitter:description"/>, <meta content="width=device-width, initial-scale=1, user-scalable=yes, viewport-fit=cover" name="viewport"/>, <meta content="Read and download METAMORPHOSIS, a hentai manga by shindol for free on nhentai." name="description"/>]
>>> for x in soup.find_all("meta"):
	print(x)

	
<meta charset="utf-8"/>
<meta content="#1f1f1f" name="theme-color"/>
<meta content="METAMORPHOSIS" itemprop="name"/>
<meta content="https://t.nhentai.net/galleries/987560/cover.jpg" itemprop="image"/>
<meta content="article" property="og:type"/>
<meta content="METAMORPHOSIS" property="og:title"/>
<meta content="https://t.nhentai.net/galleries/987560/cover.jpg" property="og:image"/>
<meta content="summary" name="twitter:card"/>
<meta content="METAMORPHOSIS" name="twitter:title"/>
<meta content="group, stockings, anal, schoolgirl uniform, nakadashi, blowjob, ahegao, incest, double penetration, dark skin, x-ray, impregnation, mind break, story arc, mmf threesome, pregnant, drugs, prostitution, piercing, blackmail, gyaru, deepthroat, snuff, already uploaded, vomit, moral degeneration, full body tattoo" name="twitter:description"/>
<meta content="width=device-width, initial-scale=1, user-scalable=yes, viewport-fit=cover" name="viewport"/>
<meta content="Read and download METAMORPHOSIS, a hentai manga by shindol for free on nhentai." name="description"/>
>>> for x in soup.find_all("meta"):
	if soup.has_attr("og:title"):
		print(x)

		
>>> for x in soup.find_all("meta"):
	if soup.has_attr("og:"):
		print(x)

		
>>> for x in soup.find_all("meta"):
	if soup.has_attr("property"):
		print(x)

		
>>> meta_tags in soup.find_all("meta",{"og:title": True}):
	
SyntaxError: invalid syntax
>>> 
>>> meta_tags in soup.find_all("meta",{"og:title": True})
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    meta_tags in soup.find_all("meta",{"og:title": True})
NameError: name 'meta_tags' is not defined
>>> soup.find_all("meta",{"og:title": True})
[]
>>> soup.find_all("meta",{"og": True})
[]
>>> soup.find_all("meta")
[<meta charset="utf-8"/>, <meta content="#1f1f1f" name="theme-color"/>, <meta content="METAMORPHOSIS" itemprop="name"/>, <meta content="https://t.nhentai.net/galleries/987560/cover.jpg" itemprop="image"/>, <meta content="article" property="og:type"/>, <meta content="METAMORPHOSIS" property="og:title"/>, <meta content="https://t.nhentai.net/galleries/987560/cover.jpg" property="og:image"/>, <meta content="summary" name="twitter:card"/>, <meta content="METAMORPHOSIS" name="twitter:title"/>, <meta content="group, stockings, anal, schoolgirl uniform, nakadashi, blowjob, ahegao, incest, double penetration, dark skin, x-ray, impregnation, mind break, story arc, mmf threesome, pregnant, drugs, prostitution, piercing, blackmail, gyaru, deepthroat, snuff, already uploaded, vomit, moral degeneration, full body tattoo" name="twitter:description"/>, <meta content="width=device-width, initial-scale=1, user-scalable=yes, viewport-fit=cover" name="viewport"/>, <meta content="Read and download METAMORPHOSIS, a hentai manga by shindol for free on nhentai." name="description"/>]
>>> 