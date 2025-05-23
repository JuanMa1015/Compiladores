.model small
.stack 100h
.data
    msg1 db 'Ingrese un numero decimal (0-99): $'
    msg2 db 13,10,'Binario: $'
    numero db ?
.code
main:
    mov ax, @data
    mov ds, ax

    ; Mostrar mensaje de entrada
    lea dx, msg1
    mov ah, 09h
    int 21h

    ; Leer caracter (solo un dígito)
    mov ah, 01h
    int 21h
    sub al, '0'       ; convertir a valor numérico
    mov bl, al

    ; Leer segundo dígito
    mov ah, 01h
    int 21h
    sub al, '0'
    mov bh, al

    ; Convertir a número decimal (decena * 10 + unidad)
    mov al, bl
    mov ah, 0
    mov cx, 10
    mul cx
    add al, bh        ; AL = número decimal
    mov bl, al        ; Guardamos en BL

    ; Mostrar mensaje binario
    lea dx, msg2
    mov ah, 09h
    int 21h

    ; Convertir a binario y mostrar
    mov cx, 8         ; 8 bits
next_bit:
    shl bl, 1         ; Desplazar bit más significativo a CF
    jc  bit1
    mov dl, '0'
    jmp mostrar
bit1:
    mov dl, '1'
mostrar:
    mov ah, 02h
    int 21h
    loop next_bit

    ; Finalizar programa
    mov ah, 4ch
    int 21h
end main