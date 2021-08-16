import requests

r = requests.post("http://127.0.0.1:8000/filter_api/filter/",data={"input_data":"2.40 2.60 JAN-01-2019 JAN-31-2019"})
print(r.raw)