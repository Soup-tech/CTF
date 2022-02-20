# Buffer Overflow Made Easy
This follows the course laid out by The Cyber Mentor. Provides a basic buffer overflow methodology. Check it out <a href="https://www.youtube.com/watch?v=qSnPayW6F7U&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&ab_channel=TheCyberMentor">here</a>

## Startup
When booting up the lab, make sure to run both VulnServer and Immunity Debugger as Administrator.<br><br>
For Immunity Debugger go File > Attach > VulnServer<br>
Then hit the play button to set the program from "stopped" to "running".<br>

## Spiking
Spiking is a method of determining what is vulnerable in an application. This is done by feeding large values to a command and/or application and seeing if a crash occurs - similar to fuzzing. If a crash does happen, it may be likely that the command/application is vulnerable a buffer overflow.<br><br>
The tool used is called "generic_send_tcp". This application sends spiking script commands over a tcp network. The spiking script used is below:
```spk
s_readlines();
s_string("STATS ");
s_string_variable("0");
```
Then the command to follow is:
```bash
generic_send_tcp 192.168.1.101 9999 0 0
```
When performing the same task on TRUN cmd, the program will actually crash. Immunity debugger will pause the execution of the program because there is an invalid EIP. The EIP gets overflowed with 41414141 (which is just AAAA in hex).