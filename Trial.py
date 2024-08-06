import http.client

conn = http.client.HTTPSConnection("india-pincode-with-latitude-and-longitude.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "4638530cfemshb5f9bea28be8a72p1d9bb8jsnef9a6f833608",
    'x-rapidapi-host': "india-pincode-with-latitude-and-longitude.p.rapidapi.com"
}

conn.request("GET", "/api/v1/pincode/500032", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))