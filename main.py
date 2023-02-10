#using fastapi

#creating a public api to call censys api
from fastapi import FastAPI
from censys.search import CensysCertificates
import uvicorn

app = FastAPI()

c = CensysCertificates()
fields = [
    "parsed.fingerprint_sha256",
    "parsed.validity.start",
    "parsed.validity.end",
]

@app.get("/certificates")
async def get_certificates(): #using async def because we need to wait for response from censys

    results = c.search(
        "parsed.names:censys.io and tags: trusted",
        fields=fields
    )
    
    #convert the results to a list of dictionaries
    certificates = [{
        'SHA256': result['parsed.fingerprint_sha256'],
        'Validity Start': result['parsed.validity.start'],
        'Validity End': result['parsed.validity.end']
    } for result in results]
    
    #return the results as JSON
    return certificates