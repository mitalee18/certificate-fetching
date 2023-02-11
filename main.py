#using fastapi - solution 3

#creating a public api to call censys api
from fastapi import FastAPI
from censys.search import CensysCertificates
import pandas as pd
from fastapi.responses import StreamingResponse
import io

app = FastAPI()

c = CensysCertificates()
fields = [
    "parsed.fingerprint_sha256",
    "parsed.validity.start",
    "parsed.validity.end",
]

@app.route("/")
def hello():
    return '''
        <html><body>
        <a href="/certificates">Click me to download csv.</a>
        </body></html>
        '''

@app.get("/certificates")
async def get_certificates(): #using async def because we need to wait for response from censys

    results = c.search(
        "parsed.names:censys.io and tags: trusted",
        fields=fields
    )
    certificate = []
    #convert the results to a list of dictionaries
    for result in results:
        sha256_fingerprint = result['parsed.fingerprint_sha256']
        validity_start = result['parsed.validity.start']
        validity_end = result['parsed.validity.end']

        certificate.append([sha256_fingerprint, validity_start, validity_end])
    

    #adding df column names
    df = pd.DataFrame(certificate, columns=["sha256_fingerprint", "validity_start", "validity_end"])
    
    #convert dataframe to csv
    stream = io.StringIO()
    df.to_csv(stream, index = False)

    response = StreamingResponse(iter([stream.getvalue()]),
                            media_type="text/csv"
       )

    
    response.headers["Content-Disposition"] = "attachment; filename=censys_io_certificates_solution3.csv"

    return response