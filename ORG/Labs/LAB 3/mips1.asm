.data
_save: .word 6, 6, 6, 6, 6, 6, 6         # completar com Estímulo 1.1 ou 1.2
_k: .word 6             
.text
.globl main
main: # inicialização
la $s6, _save                       # completar com 1 pseudoinstrução
lw $s5, _k                          # completar com 1 pseudoinstrução
addi $s3, $zero, 0                  # completar com 1 instrução nativa      
Loop: # corpo do laço
sll $t1, $s3, 2    
add $t1, $t1, $s6 
lw $t0, 0($t1) 
bne $t0, $s5, Exit    
addi $s3, $s3, 1      
j Loop
                
Exit: # rotina para imprimir inteiro no console
addi $v0, $zero, 1
add $a0, $zero, $s3
syscall     
