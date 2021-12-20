# asm1

## Description
```
What does asm1(0x6fa) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format.
```

## Hint
```
assembly conditions
```

## Procedure
We are presented with an assembly file <a href="test.S">test.S</a>.
```asm
asm1:
        <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   cmp    DWORD PTR [ebp+0x8],0x3a2
        <+10>:  jg     0x512 <asm1+37>
        <+12>:  cmp    DWORD PTR [ebp+0x8],0x358
        <+19>:  jne    0x50a <asm1+29>
        <+21>:  mov    eax,DWORD PTR [ebp+0x8]
        <+24>:  add    eax,0x12
        <+27>:  jmp    0x529 <asm1+60>
        <+29>:  mov    eax,DWORD PTR [ebp+0x8]
        <+32>:  sub    eax,0x12
        <+35>:  jmp    0x529 <asm1+60>
        <+37>:  cmp    DWORD PTR [ebp+0x8],0x6fa
        <+44>:  jne    0x523 <asm1+54>
        <+46>:  mov    eax,DWORD PTR [ebp+0x8]
        <+49>:  sub    eax,0x12
        <+52>:  jmp    0x529 <asm1+60>
        <+54>:  mov    eax,DWORD PTR [ebp+0x8]
        <+57>:  add    eax,0x12
        <+60>:  pop    ebp
        <+61>:  ret    
```
Which is the assembly to some program. I'm assuming that the contents of [ebp+0x8] is the user input which is 0x6fa. Starting at <+3> a comparison is made between 0x3a2 and 0x6fa and if 0x3a2 > 0x6fa than a jump is made to <+37>. 0x3a2 ngt (not greater than) 0x6fa so the application continues to <+12> where another comparison is made. Compare 0x358 to 0x6fa. If 0x358 is not equal to 0x6fa than a jump is made to <+29>. The jne evaluates to True since 0x358 ne (not equal) 0x6fa.<br>
At <+29>, 0x6fa is moved into eax and then 0x12 is subtracted from eax. Lastly a jump is made to <+60> where ebp is popped off the stack. Thus 0x6fa - 0x12 = 0x6e8 is the result. 

## Flag
```
0x6e8
```