# So Meta

## Description
Find the flag in this picture.

## Approach
1. Download the file

```
wget https://jupiter.challenges.picoctf.org/static/89b371a46702a31aa9931a2a2b12f8bf/pico_img.png
```

2. Identify the flag, check that it is an image

```
file pico_img.png
```

Output:
```
pico_img.png: PNG image data, 600 x 600, 8-bit/color RGB, non-interlaced
```

3. Open the image and have a look at the image it self.

```bash
eog pico_img.png
```

Did not really see anything there, nothing "sticks" out. 

4. Let us try and check  with buld_extractor

```bash
bulk_extract -o meta_out pico_img.png
```

Let us move inside the meta folder and do some greps.

```bash
cd meta_out/

grep -iR pico
grep -iR CTF
```

Had a look as well, could not find any flags.

5. Let us dump the meta data

```bash
exiftool pico_img.png
```

Output:
```
ExifTool Version Number         : 12.44
File Name                       : pico_img.png
Directory                       : .
File Size                       : 109 kB
File Modification Date/Time     : 2020:10:26 19:38:23+01:00
File Access Date/Time           : 2022:07:28 16:10:11+02:00
File Inode Change Date/Time     : 2022:07:27 10:31:50+02:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_eb36bf44}
Image Size                      : 600x600
Megapixels                      : 0.360
```

Et Voila! Artist has the flag: 

```
picoCTF{s0_m3ta_eb36bf44}
```

## Conclusion
Fun little challenge. Dumped the data is always a good practice, but got the information I wanted with the exiftool. 

