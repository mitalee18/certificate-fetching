#creating api to download csv
from flask import Flask, send_file
from flask_restful import Api, Resource
from censys.search import CensysCertificates
import pandas as pd


app = Flask(__name__)
api = Api(app)

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
        <a href="/get">Click me to download csv.</a>
        </body></html>
        '''

class certificate(Resource):
    def get(self):

        results = c.search(
            "parsed.names:censys.io and tags: trusted",
            fields=fields)
        
        certificate = []
        # Convert the results to a list of dictionaries and add to dataframe
        for result in results:
            sha256_fingerprint = result['parsed.fingerprint_sha256']
            validity_start = result['parsed.validity.start']
            validity_end = result['parsed.validity.end']

            certificate.append([sha256_fingerprint, validity_start, validity_end])
        
        #adding df column names
        df = pd.DataFrame(certificate, columns=["sha256_fingerprint", "validity_start", "validity_end"])

        #convert dataframe to csv
        df.to_csv("censys_io_certificates.csv", index=False)

        return send_file(
            'censys_io_certificates.csv',
            mimetype='text/csv',
            attachment_filename='censys_io_certificates.csv',
            as_attachment=True
        )

api.add_resource(certificate, '/get')
if __name__ == "__main__":
    app.run(debug=True) #used to start server and see logs; set true only in development environment not production