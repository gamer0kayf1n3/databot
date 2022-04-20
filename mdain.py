import re
import opengraph_py3
import requests as rq
def detect_sauce(inw: str):
  unverified_sussy_codes = re.findall("\\d{5,6}",inw)
  to_be_returned = []
  for code in unverified_sussy_codes:
    if rq.get(f"https://nhentai.net/g/{code}").status_code == 200:
      to_be_returned.append(code)
  return to_be_returned
