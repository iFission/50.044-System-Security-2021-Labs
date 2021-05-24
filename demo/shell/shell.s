.global _start
_start: 
 mov $59, %al # execve
 lea binsh(%rip), %rdi #rip-relative addressing convention: load register with exact address of binsh
 xor %rsi, %rsi  # 0
 xor %rdx, %rdx	 # 0
 syscall

binsh:
  .string "/bin/sh"
