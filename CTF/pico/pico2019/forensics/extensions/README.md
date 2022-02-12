# extensions

## Description
```
This is a really work TXT? Can you find the flag?
```

## Hints
```
How do OS's know what kind of file it is?
```

## Procedure
Looking at the extension of the file tells us that the file is a .txt file, however if we were to look at the contents of flag.txt all that comes back is gibberish. Using UNIX <b>file</b> gives more information:
```bash
file flag.txt
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```
So this is a PNG. To confirm this, we can do a hex dump of this file and look at the magic bytes or the file header information:
```bash
xxd flag.txt | less
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```
The bytes <b>89 50 4E 47 0D 0A 1A 0A</b> confirms that this is a png. Change the file extension and open this file up in an image viewer:
```bash
mv flag.txt flag.png
xdg-open flag.png
```
Opens an image and displays the flag:

## Flag
```
picoCTf{now_you_know_about_extensions}
```