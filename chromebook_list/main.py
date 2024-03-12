import sys
# import json

from googleapiclient.discovery import build
from google.oauth2 import service_account

CHROME_SCOPE = 'https://www.googleapis.com/auth/admin.directory.device.chromeos'
CUSTOMER_SCOPE = 'https://www.googleapis.com/auth/admin.directory.customer'
ORGUNIT_SCOPE = "https://www.googleapis.com/auth/admin.directory.orgunit"
        

SCOPES = [CHROME_SCOPE, CUSTOMER_SCOPE, ORGUNIT_SCOPE]


def main(args: list[str]):
    if len(args) < 2:
        raise ValueError('missing <credential-file> <delegated> inputs')

    credentials = service_account.Credentials.from_service_account_file(
        args[0],
        scopes=SCOPES,
        subject=args[1],
    )

    service = build('admin', 'directory_v1', credentials=credentials)

    devices = service.chromeosdevices().list(customerId='my_customer').execute()

    for device in devices['chromeosdevices']:
        print("Device:", device['deviceId'], device['serialNumber'], device['model'])


if __name__ == '__main__':
    main(sys.argv[1:])
