# What Lies Within

## Description
Author: Julio/Danny

There's something in the building. Can you retrieve the flag?

## Approach
1. Donwload the file

```bash
wget https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png
```

2. Let us identify the file

```bash
file buildings.png
```
Output:
```
buildings.png: PNG image data, 657 x 438, 8-bit/color RGBA, non-interlaced
```
3. Seems like a standard PNG image, let us open it!
```bash
eog buildings.png
```

Nothing there, as far as I can see. But before I start doing photo manipulation to see if there is anything there let us explore some other options first.

4. Bulk extract everything

```
bulk_extractor -o file_dump buildings.png
```

Nothing of interest there. 

5. Let us get the meta data as well:

```bash
exiftool buildings.png
```

Output: 
```
ExifTool Version Number         : 12.44
File Name                       : buildings.png
Directory                       : .
File Size                       : 625 kB
File Modification Date/Time     : 2020:10:26 19:30:20+01:00
File Access Date/Time           : 2022:07:31 03:01:08+02:00
File Inode Change Date/Time     : 2022:07:31 03:00:27+02:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 657
Image Height                    : 438
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 657x438
Megapixels                      : 0.288

```

Nothing which sticks out...

6. Let us see if we can find anything online in regards to extracting data from png images..

* I came across a tool called zsteg 
```bash
sudo gem install zsteg
```

7. Let us use zsteg to see if we can find anything
```bash
zsteg buildings.png
```
Output
```
b1,r,lsb,xy         .. text: "^5>R5YZrG"
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"
b1,abgr,msb,xy      .. file: PGP Secret Sub-key -
b2,b,lsb,xy         .. text: "XuH}p#8Iy="
b3,abgr,msb,xy      .. text: "t@Wp-_tH_v\r"
b4,r,lsb,xy         .. text: "fdD\"\"\"\" "
b4,r,msb,xy         .. text: "%Q#gpSv0c05"
b4,g,lsb,xy         .. text: "fDfffDD\"\""
b4,g,msb,xy         .. text: "f\"fff\"\"DD"
b4,b,lsb,xy         .. text: "\"$BDDDDf"
b4,b,msb,xy         .. text: "wwBDDDfUU53w"
b4,rgb,msb,xy       .. text: "dUcv%F#A`"
b4,bgr,msb,xy       .. text: " V\"c7Ga4"
b4,abgr,msb,xy      .. text: "gOC_$_@o"

```

And there is the flag!

Flag:
```
picoCTF{h1d1ng_1n_th3_b1t5}
```

## Conclusion
Interesting challenge, have never used zsteg, or even heard about it before but it works great! https://github.com/zed-0xff/zsteg

A tool that should be in all CTFers toolkit!
