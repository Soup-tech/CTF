# Shark on the Wire 1

## Description
```
We found this packet capture. Recover the flag.
```

## Hints
```
Try using a tool like Wireshark
What are streams?
```

## Procedure
This is a straight forward forensics challenge (maybe). Downloading the <a href="capture.pcap">packet capture file</a> and cracking open Wireshark. I always look at <b>Statistics > Protocol Hierarchy</b> gives a good idea of the PCAP file as a whole. There are a lot of streams of interest including:<br> 
<ul>
Simple Service Discovery Protocol (SSDP)
Server Message Block Protocol (SMB)
Address Resolution Protocol (ARP)
User Datagrap Protocol (UDP)
</ul>

Because UDP makes up 49.2% of the PCAP file, I begin my digging there.<br>
I procedurally go through and use <b>udp.stream eq #</b> looking at all teh UDP streams. When I arrive at <b>udp.stream eq 6</b> I find the flag:

## Flag
```
picoCTF{StaT31355_636f6e6e}
```