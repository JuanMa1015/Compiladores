.model small
.stack 100h
.data
    msg1 db 'Ingrese una cadena (max 20 caracteres): $'
    cadena db 21 dup('$') ; espacio para la cadena + '$'
    msg2 db 13,10,'Cadena invertida: $'
.code
main:
    mov ax, @data
    mov ds, ax

    ; Mostrar mensaje
    lea dx, msg1
    mov ah, 09h
    int 21h

    ; Leer cadena (máximo 20 caracteres)
    lea dx, cadena
    mov ah, 0Ah
    mov dx, offset cadena
    mov byte ptr [cadena], 20  ; longitud máxima
    int 21h

    ; Mostrar mensaje
    lea dx, msg2
    mov ah, 09h
    int 21h

    ; Invertir y mostrar
    lea si, cadena+2         ; apuntamos al inicio real
    mov cl, [cadena+1]       ; longitud real ingresada
    mov ch, 0
    add si, cx               ; apuntar al último carácter

invertir:
    dec si
    mov dl, [si]
    mov ah, 02h
    int 21h
    loop invertir

    ; Salir
    mov ah, 4ch
    int 21h
end main