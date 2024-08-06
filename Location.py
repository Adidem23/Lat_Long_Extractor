import pandas as pd
import http.client
import json

file_path = 'Location_excel.xlsx'

PinCodeColumns= pd.read_excel(file_path, usecols=['Pincode'])
AREAColumns= pd.read_excel(file_path,usecols=['AREA'])

def ExtractLatiandLongitude():
    for Pincode in PinCodeColumns['Pincode']:
        for Area in AREAColumns['AREA']:  
            conn = http.client.HTTPSConnection("india-pincode-with-latitude-and-longitude.p.rapidapi.com")

            headers = {
            'x-rapidapi-key': "4638530cfemshb5f9bea28be8a72p1d9bb8jsnef9a6f833608",
            'x-rapidapi-host': "india-pincode-with-latitude-and-longitude.p.rapidapi.com"
            }
            
            conn.request("GET", f"/api/v1/pincode/{Pincode}", headers=headers)
            
            res = conn.getresponse()
            data = res.read()
            JSON_String=data.decode("utf-8")
            JSON_Object=json.loads(JSON_String)

            for i in JSON_Object:
                if str.lower(i['area'])==str.lower(Area):
                    print(f"Pincode {Pincode} Belongs to State {i['state']}")
                    print(f"Latitude and Logitude for {Area} are {i['lat']} and {i['lng']}")

if __name__=="__main__":
    ExtractLatiandLongitude()