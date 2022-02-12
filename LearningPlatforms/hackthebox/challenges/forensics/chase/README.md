# Chase

## Description
```
One of our web servers triggered an AV alert, but none of the sysadmins say they were logged onto it. We've taken a network capture before shutting the server down to take a clone of the disk. Can you take a look at the PCAP and see if anything is up?
```

## Procedure
I am given zip file <b>Chase.zip</b>. The password to the zip file is <b>hackthebox</b>. After decompressing I am presented with a PCAP file, <b>chase.pcapng</b>. I fired up <a href="https://www.wireshark.org/">Wireshark</a> and looked at Protocol Hierarchy. The main point of interest is HTTP which makes up ~10% of the PCAP file. This is the only protocol that is unencrypted.<br>


## HTTP
