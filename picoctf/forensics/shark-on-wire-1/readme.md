# shark on wire 1

## Description
Author: Danny
Description

We found this packet capture. Recover the flag.

## Approach

1. Download the file
```bash
wget https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap
```

2. Open the Capture in wireshark

```
wireshark capture.pcap
```

3. Let us check if there is anything interesting traffic that sticks out.

* Checking DNS, ARP and Broadcasts
* Checking TCP streams 0-10 Nothing
* Checking UDP streams 0-10 Found it!

Flag was found iterating through the UDP streams on the sixth UDP stream!

Flag: 
```
picoCTF{StaT31355_636f6e6e}
```

## Conclusion
Fun little challenge. Remember to always make sure you run through your streams!


