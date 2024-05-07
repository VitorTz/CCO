.data
_save: .word 999 7, 6, 6, 6, 6, 6, 6, 6               # completar com Estímulo 2.1 ou Estímulo 2.2
_k: .word 6 
_error: .asciiz "Index Out of Bounds Exception"	    
.text
.globl main
main: # inicialização
la $s6, _save                                 # completar com 1 pseudoinstrução
lw $s5, _k                                 # completar com 1 pseudoinstrução
addi $s3, $zero, 0                                 # completar com 1 instrução nativa
lw $t2, 4($s6)                                             # completar com 1 instrução nativa
Loop: 
# verificação de limite do arranjo
slt $t1, $s3, $t2                                 # teste de índice: completar com 1 instrução nativa
beq $t1, $zero, IndexOutOfBounds                                # desvio para mensagem de erro: completar com 1 instrução nativa
# corpo do laço
sll $t1, $s3, 2    
add $t1, $t1, $s6 
lw $t0, 8($t1)                         # você terá que modificar esta instrução!
bne $t0, $s5, Exit    
addi $s3, $s3, 1      
j Loop

Exit: # rotina para imprimir inteiro no console
addi $v0, $zero, 1
add $a0, $zero, $s3
syscall
j End

IndexOutOfBounds: # rotina para imprimir mensagem de erro no console
addi $v0, $zero, 4
la $a0, _error
syscall
End:   
