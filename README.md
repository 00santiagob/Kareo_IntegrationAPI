# Kareo_IntegrationAPI

Integration Kareo with Python using the Kareo Web Services API 2.1

## Requerimientos

* Python 3.x
* ```
  pip install -r requirements.txt
  ```

## Uso

Sustituir los valores por los correctos.

`python3 kareo.py Key=example User=example@example.com Pass=example`


### Troubleshooting

#### [URLopen Error | CERTIFICATE_VERIFY_FAILED #831](https://github.com/sendgrid/sendgrid-python/issues/831)

urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:xxxx)>

  * Linux Solution:
    ```BASH
    $ sudo update-ca-certificates --fresh
    $ export SSL_CERT_DIR=/etc/ssl/certs
    ```
  * MacOs Solution: 
Go to Macintosh HD > Applications > Python folder > double click on "Install Certificates.command" file.
