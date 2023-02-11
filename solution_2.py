#creating api to download csv
from flask import Flask, send_file
from flask_restful import Api, Resource
from censys.search import CensysCertificates
import pandas as pd
import fetch

app = Flask(__name__)
api = Api(app)


class certificate(Resource):
    def get(self):

        #callin fetch.py to get search result
        certificate = fetch.search()

        #adding df column names
        df = pd.DataFrame(certificate, columns=["sha256_fingerprint", "validity_start", "validity_end"])

        #convert dataframe to csv
        df.to_csv("censys_io_certificates_solution2.csv", index=False)

        return send_file(
            'censys_io_certificates_solution2.csv',
            mimetype='text/csv',
            attachment_filename='censys_io_certificates_solution2.csv',
            as_attachment=True
        )

api.add_resource(certificate, '/get')
if __name__ == "__main__":
    app.run(debug=True) #used to start server and see logs; set true only in development environment not production