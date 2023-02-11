from censys.search import CensysCertificates
c = CensysCertificates()

fields = [
    "parsed.fingerprint_sha256",
    "parsed.validity.start",
    "parsed.validity.end",
]

def search():
    try:
        results = c.search(
                    "parsed.names:censys.io and tags: trusted",
                    fields=fields)
    except:
        print("An exception occured")
            
    certificate = []
    # Convert the results to a list of dictionaries and add to dataframe
    for result in results:
        sha256_fingerprint = result['parsed.fingerprint_sha256']
        validity_start = result['parsed.validity.start']
        validity_end = result['parsed.validity.end']

        certificate.append([sha256_fingerprint, validity_start, validity_end])

    return certificate