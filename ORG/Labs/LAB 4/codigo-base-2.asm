.data
# Arranjo inicializado com elementos N não nulos. 
_array: .word 3:N	   # N elementos com o valor 3               [substitua N pelo valor definido no relatório]
_size: .word N  	   # tamanho do arranjo                      [substitua N pelo valor definido no relatório]

.text
.globl main

main:
    ...                # carrega o endereco de array em $a0      [completar com 1 pseudo-instrução]
    ...                # carrega size em $a1                     [completar com 1 pseudo-instrução]
    jal clear2
    li  $v0,10
    syscall
    
clear2:     
   ...                 # $t0 <- $a0                              [completar com 1 instrução nativa]
   ...                 # $t1 <- size*4                           [completar com 1 instrução nativa]
   add $t2,$a0,$t1     # $t2 <- &array[size]                    
loop2:
   ...                 # $t3 = (p < &array[size])                [completar com 1 instrução nativa]
   ...                 # se (p >= &array[size]) desvia para Exit [completar com 1 instrução nativa]
   sw $zero,0($t0)     # mem[p] = 0                              
   addi $t0,$t0,...    # p = p + ?                               [completar operando faltante]
   j loop2
   
Exit:
   jr $ra

