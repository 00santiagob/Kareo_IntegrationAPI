# Kareo_IntegrationAPI

Integration Kareo with Python using the Kareo Web Services API 2.1

#### Requerimientos

* Python 3.x
* ```
  pip install -r requirements.txt
  ```

#### Uso

Sustituir los valores por los correctos.

`python3 kareo.py Key=example User=example@example.com Pass=example`


#### troubleshooting

If you are using MACos and this error occurs:

urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)>

Go to Macintosh HD > Applications > Python folder > double click on "Install Certificates.command" file.