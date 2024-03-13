# -*- coding: utf-8 -*-
"""Scrapping Data Review.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XYFtRRDgdL2N02B5g6OwfoA_vWbxd7Uc

# Scrapping Data Review Wisata Indonesia dengan SerpAPI

---

*   **Install Modul Python Google Search Results**
"""

pip install google-search-results

"""

*   **Import Library Google**

"""

from serpapi import GoogleSearch
from urllib.parse import *

"""

*   **Scrapping Hasil Data**

   mengambil 15 objek wisata yang memiliki ≥ 1000 views

"""

params = {
    "engine": "google_maps",
    "q": "wisata indonesia",
    "ll": "@-7.4548074,110.1102104,10z",
    "type": "search",
    "api_key": "1e15cb862401aac1d0ceb77f9bc8a132174b60004dacfe264e7524db24e39878",
    "hl": "id",
    "gl": "id"
}

search = GoogleSearch(params)

idx = 0
last = 15
local_results = []

while idx <= last:

  results = search.get_dict()

  for Result in results['local_results']:
    idx += 1

    if idx <= last:

      if Result["reviews"] < 1000:
        idx += 1
        continue

      local_results.append({'Nama': Result["title"],
                            'data_id': Result["data_id"],
                            'total_reviews': Result["reviews"]});

  if "next" in results.get("serpapi_pagination", {}):
    search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))
  else:
    break

for lr in local_results:
  print(lr)

"""

*   Scrapping Reviews

    Mengambil 100 data dari masing-masing objek wisata sesuai dengan jumlah index yang diinginkan

"""

data = {'nama_wisata': [],
        'nama_pereview': [],
        'rating': [],
        'review': []}

for lr in local_results:
  params = {
      "engine": "google_maps_reviews",
      "data_id": "",
      "api_key": "1e15cb862401aac1d0ceb77f9bc8a132174b60004dacfe264e7524db24e39878",
      "hl": "id",

  }

  params["data_id"] = lr["data_id"]

  search = GoogleSearch(params)

  idx = 0
  last = 30

  while idx <= last:

    results = search.get_dict()

    for Result in results["reviews"]:
      idx += 1

      if idx <= last:
        data['nama_wisata'].append(lr["Nama"]);
        data['nama_pereview'].append(Result["user"]["name"]);
        data['rating'].append(Result["rating"]);
        data['review'].append(Result["snippet"]);

    if "next" in results.get("serpapi_pagination", {}):
      search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))

    else:
      break

review_original = data['review']

"""

*   Export Data Scrapping to CSV

"""

import pandas as pd
from google.colab import drive

drive.mount('/content/drive')
dfScrap = pd.DataFrame(data)
dfScrap.to_csv('/content/drive/My Drive/reviewWisataIndonesia.csv', index=False)
dfScrap

