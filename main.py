#using fastapi - solution 3

#creating a public api to call censys api
from fastapi import FastAPI
import pandas as pd
from fastapi.responses import StreamingResponse
import io
import fetch

app = FastAPI()

@app.route("/")
def hello():
    return '''
        <html><body>
        <a href="/certificates">Click me to download csv.</a>
        </body></html>
        '''

@app.get("/certificates")
async def get_certificates(): #using async def because we need to wait for response from censys

    #callin fetch.py to get search result
    certificate = fetch.search()
    
    #adding df column names
    df = pd.DataFrame(certificate, columns=["sha256_fingerprint", "validity_start", "validity_end"])
    
    #convert dataframe to csv
    stream = io.StringIO()
    df.to_csv(stream, index = False)

    response = StreamingResponse(iter([stream.getvalue()]),
                            media_type="text/csv")

    
    response.headers["Content-Disposition"] = "attachment; filename=censys_io_certificates_solution3.csv"

    return response