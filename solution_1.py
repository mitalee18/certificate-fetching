from censys.search import CensysCertificates
import csv
c = CensysCertificates()

fields = [
    "parsed.fingerprint_sha256",
    "parsed.validity.start",
    "parsed.validity.end",
]

with open('certificates.csv', 'w', newline='') as csvfile:
    fieldnames = ['sha256_fingerprint', 'validity_start', 'validity_end']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for result in c.search(
        "parsed.names:censys.io and tags: trusted",
        fields=fields,
        max_records=100, #can change this value, but maximum records being returned are 458
    ):
        writer.writerow({'sha256_fingerprint': result['parsed.fingerprint_sha256'],
                         'validity_start': result['parsed.validity.start'],
                         'validity_end': result['parsed.validity.end']})
