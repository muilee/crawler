
# coding: utf-8

# In[1]:

import requests
import re
import json
from urllib import parse
import shutil

res = requests.get("https://www.youtube.com/watch?v=Ez4-ZY9yY_U")
m = re.search("ytplayer.config = ({.*?});", res.text)
js = json.loads(m.group(1))
a = parse.parse_qs(js['args']['url_encoded_fmt_stream_map'])
res2 = requests.get(a["url"][0], stream=True)
f = open('a.mp4', 'wb')
shutil.copyfileobj(res2.raw, f)
f.close()


# In[ ]:



