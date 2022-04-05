# Transformation

## Description
```
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

## Hint
```
You may find some decoders online
```

## Procedure
We are given a file <b>end</b>. Checking out the file type:
```bash
file enc
enc: UTF-8 Unicode text, with no line terminators
```
The contents of the file are:
```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽
```
This looks like Mandarin. When looking up a translator though I cannot translate from Mandarin to English.<br>
I have a feeling that it has something to do with the encoding scheme being Unicode. Because ASCII only has 2^7 bits where Unicode can have a lot more. 