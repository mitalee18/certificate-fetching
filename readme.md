# Censys Certificate Data Extractor
This project implements a Python script that uses the Censys API and Python library to query the certificates index and download a CSV of the SHA256 fingerprints and validity start and end dates for all trusted (unexpired) X.509 certificates associated with the censys.io domain.

## Requirements
1. Python 3.x

2. Censys Python library
```bash
 pip install censys
 ```

 3. Set both `CENSYS_API_ID` and `CENSYS_API_SECRET` environment variables.

```bash
$ censys config

Censys API ID: XXX
Censys API Secret: XXX
Do you want color output? [y/n]: y

Successfully authenticated for your@email.com
```

## Usage
1. Clone this repository:
``` bash
git clone https://github.com/mitalee18/certificate-fetching.git
```

2. Navigate to the project directory:
``` bash
cd certificate-fetching
```

3. Install requirements:
``` bash
pip install -r requirements.txt
``` 

4. Run the script:\
There are 3 solutions for this application, run each one in the directory where the dependencies are installed\
Solution 1
```bash
python solution_1.py
```
This will normally download the csv file in the existing directory

Solution 2
```bash
python solution_1.py
```
This solution creates a flask api running on `http://127.0.0.1:5000/` creates a hyper link, which is clicked to call the get api which will download cvs

Solution 3
```bash
uvicorn main:app --reload
```
This solution creats a fastAPI running on `http://127.0.0.1:8000/certificate` downloads the csv file directly

## Configuration
You can modify the following parameters in the script to customize the query and the output:

`query`: the query to be performed on the Censys certificates index. The default query is `"parsed.names: censys.io and tags: trusted"`, which returns all trusted X.509 certificates associated with the censys.io domain.
`fields`: the fields to be included in the output. The default fields are ["parsed.sha256_fingerprint", "parsed.validity.start", "parsed.validity.end"], which are the SHA256 fingerprints and validity start and end dates of the certificates.