# Glory of the Garden

## Description

This garden contains more than it seems.

<br />

## Approach
1. Download the file

```bash
wget https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg
```

2. Let us see what we can gather from the file
```bash
file garden.jpg 
```
Gives us the following output:
```
garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3
```
Okay, so we know it is an image. Let us try and open it and see.

```bash
eog gargen.jpg
```
So we see a garden. No text as far as I can see in the image. Let us get some more detailed information of the image.

```bash
exiftool garden.jpg
```
This gives us all the meta information of the file. The exiftool can be used to read and write meta information in files.

```
ExifTool Version Number         : 12.42
File Name                       : garden.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2020:10:26 19:39:31+01:00
File Access Date/Time           : 2022:07:23 15:23:44+02:00
File Inode Change Date/Time     : 2022:07:23 15:23:38+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Image Width                     : 2999
Image Height                    : 2249
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2999x2249
Megapixels                      : 6.7

```

3. So at this point, we might as well just dump all the information within the file to see if there are other files hiding inside it. 

```bash
bulk_extractor -o file_dump garden.jpg
```

This will scan the disk image or file for pre-defined regular expressions and other content. And dump it into a directory called file_dump. In this directory let us just search trough it and see if we find anything interesting.

There is a lot of text files, so let us use some grep magic to see if we find anything.

```bash
grep -iR flag
grep -iR pico
grep -iR ctf
```
Could not find anything of interest. So let us grep all the text and objects

```bash
grep -iR ""
```

Let us scan through all the text we get, and guess what? We did not find anything...

4. Okay, so I opened the hint for the challenge and the following was given:
*"What is a hex editor?"*

Let us check the header of the file. I am now thinking about if it can be magic bytes (aka file signatures).
```bash
xxd garden.jpg | head
```

Output:
```
00000000: ffd8 ffe0 0010 4a46 4946 0001 0101 0048  ......JFIF.....H
00000010: 0048 0000 ffe2 0c58 4943 435f 5052 4f46  .H.....XICC_PROF
00000020: 494c 4500 0101 0000 0c48 4c69 6e6f 0210  ILE......HLino..
00000030: 0000 6d6e 7472 5247 4220 5859 5a20 07ce  ..mntrRGB XYZ ..
00000040: 0002 0009 0006 0031 0000 6163 7370 4d53  .......1..acspMS
00000050: 4654 0000 0000 4945 4320 7352 4742 0000  FT....IEC sRGB..
00000060: 0000 0000 0000 0000 0000 0000 f6d6 0001  ................
00000070: 0000 0000 d32d 4850 2020 0000 0000 0000  .....-HP  ......
00000080: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000090: 0000 0000 0000 0000 0000 0000 0000 0000  ................
```

Need to look up the magic bytes as a reference: https://en.wikipedia.org/wiki/List_of_file_signatures

