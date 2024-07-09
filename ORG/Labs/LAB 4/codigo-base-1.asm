.data
# Arranjo inicializado com elementos N não nulos.
_array: .word 3:N		  # N elementos com o valor 3       [substitua N pelo valor definido no relatório]
_size: .word N  		  # tamanho do arranjo              [substitua N pelo valor definido no relatório]

.text
.globl main

main:
    ...                   # $a0 = &array                    [completar com 1 pseudo-instrução]
    ...                   # $a1 = size                      [completar com 1 pseudo-instrução]
    jal clear1
    li  $v0,10
    syscall

clear1:
   ...                    # i=0                             [completar com 1 instrução nativa]
loop1:
   ...                    # $t3 = (i < size)                [completar com 1 instrução nativa]
   ...                    # se (i >= size) desvia para Exit [completar com 1 instrução nativa]
   ...                    # i = i * 4                       [completar com 1 instrução nativa]
   add $t2,$a0,$t1        # $t2 = &array[i]                 
   sw $zero,0($t2)        # array[i] = 0                    
   addi $t0,$t0,...       # i++                             [completar operando faltante]                      
   j loop1
   
 Exit:
   jr $ra

