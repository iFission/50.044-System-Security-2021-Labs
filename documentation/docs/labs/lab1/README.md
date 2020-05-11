# Lab 1 - Memory Vulnerabilities

:::tip

## Homework Submission

For this assignment, you should complete 6 exercises and submit their respective files on [edimension](https://edimension.sutd.edu.sg/webapps/login/). This includes your **assignment answers in .doc, .docx or .pdf format**, which briefly explains your solution to **all question**. **You can zip all files before submission.**

The deliverables for the exercises are summarized below with the command to generate them. Keep in mind that those commands only compress the files of your lab folder. Make sure that your changes are included in the compressed files according to their respective exercises.

| Exercise                                                     | Deliverable                                       | Command                   |
| ------------------------------------------------------------ | ------------------------------------------------- | ------------------------- |
| [1](#exercise-1)                                             | `Assignment answer`                               |                           |
| [2](#exercise-2), [3.1](#exercise-3-1), [3.2](#exercise-3-2) | `lab1a-handin.tar.gz` **and** `Assignment answer` | **make prepare-submit-a** |
| [4](#exercise-4), [6](#exercise-6)                           | `lab1-handin.tar.gz` **and** `Assignment answers` | **make prepare-submit**   |
| [5](#exercise-5)                                             | `Assignment answer`                               |                           |

:::

Lab 1 will introduce you to buffer overflow vulnerabilities, in the context of a web server called `zookws`. The `zookws` web server runs a simple python web application, `zoobar`, with which users transfer "**zoobars**" (credits) between each other. You will find buffer overflows in the `zookws` web server code, write exploits for the buffer overflows to inject code into the server over the network, and figure out how to bypass non-executable stack protection. Later labs look at other security aspects of the `zoobar` and `zookws` infrastructure.

## Getting started

The files you will need for this and subsequent labs are distributed using the [Git](http://git-scm.com/)[overview of Git](https://hacker-tools.github.io/version-control/)[Git user's manual](http://www.kernel.org/pub/software/scm/git/docs/user-manual.html)

![lab1_git](/labs/labs/lab1_git.gif)

The course Git repository is available at [https://gitlab.com/istd50044/labs](https://gitlab.com/istd50044/labs). To get the lab code, log into the VM using the `httpd` account and clone the source code for lab 1 as follows:

```bash
httpd@istd:~$ git clone https://gitlab.com/istd50044/labs
Cloning into 'labs'...
httpd@istd:~$ cd labs/lab1_mem_vulnerabilities
httpd@istd:~/labs/lab1_mem_vulnerabilities$
```

Before you proceed with this lab assignment, make sure you can compile the `zookws` web server:

```bash
httpd@istd:~/labs$ make
cc zookd.c -c -o zookd.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static -fno-stack-protector
cc http.c -c -o http.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static -fno-stack-protector
cc -m64  zookd.o http.o  -lcrypto -o zookd
cc -m64 zookd.o http.o  -lcrypto -o zookd-exstack -z execstack
cc -m64 zookd.o http.o  -lcrypto -o zookd-nxstack
cc zookd.c -c -o zookd-withssp.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static
cc http.c -c -o http-withssp.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static
cc -m64  zookd-withssp.o http-withssp.o  -lcrypto -o zookd-withssp
cc -m64   -c -o shellcode.o shellcode.S
objcopy -S -O binary -j .text shellcode.o shellcode.bin
cc run-shellcode.c -c -o run-shellcode.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static -fno-stack-protector
cc -m64  run-shellcode.o  -lcrypto -o run-shellcode
rm shellcode.o
httpd@istd:~/labs$
```

The component of `zookws` that receives HTTP requests is `zookd`. It is written in C and serves static files and executes dynamic scripts. For this lab you don't have to understand the dynamic scripts; they are written in Python and the exploits in this lab apply only to C code. The HTTP-related code is in `http.c`. [Here](http://www.garshol.priv.no/download/text/http-tut.html) is a tutorial about the HTTP protocol.

There are two versions of `zookd` you will be using:

- `zookd-exstack`
- `zookd-nxstack`

`zookd-exstack` has an executable stack, which makes it easy to inject executable code given a stack buffer overflow vulnerability. has a non-executable stack, and requires a more sophisticated attack to exploit stack buffer overflows.

Now, make sure you can run the `zookws` web server and access the `zoobar` web application from a browser running on your machine, as follows:

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ ./clean-env.sh ./zookd 8080
```

The commands above start `zookd` on port 8080. To open the zoobar application, open your browser and point it at the URL `http://127.0.0.1:8080/`, where `127.0.0.1` is the your local machine IP which has port 8080 mapped to the same VM port. If something doesn't seem to be working, check if the NAT Network is setup correctly on the VM before proceeding further.

The reference binaries of `zookd` are provided in `bin.tar.gz`, which we will use for grading. Make sure your exploits work on those binaries. The **make check** command will use both `clean-env.sh` and `bin.tar.gz` to check your submission.

## A) Finding buffer overflows

In the first part of this lab assignment, you will find buffer overflows in the provided web server. To do this lab, you will need to understand the basics of buffer overflows. To help you get started with this, you should read [Smashing the Stack in the 21st Century](https://thesquareplanet.com/blog/smashing-the-stack-21st-century/), which goes through the details of how buffer overflows work, and how they can be exploited.

:::tip

### **Exercise 1**

Study the web server's C code (in `zookd.c` and `http.c`), and find one example of code that allows an attacker to overwrite the return address of a function. **Hint: look for buffers allocated on the stack**. Write down a description of the vulnerability in the `Assignment document`. For your vulnerability, describe the buffer which may overflow, how you would structure the input to the web server (i.e., the HTTP request) to overflow the buffer and overwrite the return address, and the call stack that will trigger the buffer overflow (i.e., the chain of function calls starting from `process_client`).

It is worth taking your time on this exercise and familiarizing yourself with the code, because your next job is to exploit the vulnerability you identified. In fact, you may want to go back and forth between this exercise and [Exercises 2](#exercise-2) and [3.2](#exercise-3-2), as you work out the details and document them. That is, if you find a buffer overflow that you think can be exploited, you can use Exercises 2 and 3 to figure out if it indeed can be exploited. It will be helpful to draw a stack diagram like the figures in [Smashing the Stack in the 21st Century](https://thesquareplanet.com/blog/smashing-the-stack-21st-century/).

:::

Now, you will start developing exploits to take advantage of the buffer overflows you have found above. We have provided template Python code for an exploit in `~/labs/lab1_mem_vulnerabilities/exploit-template.py`, which issues an HTTP request. The exploit template takes two arguments, the server name and port number, so you might run it as follows to issue a request to `zookws` running on localhost:

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ ./clean-env.sh ./zookd-exstack 8080 &
[1] 2676
httpd@istd:~/labs/lab1_mem_vulnerabilities$ ./exploit-template.py localhost 8080
HTTP request:
GET / HTTP/1.0

...
httpd@istd:~/labs/lab1_mem_vulnerabilities$
```

You are free to use this template, or write your own exploit code from scratch. Note, however, that if you choose to write your own exploit, the exploit must run correctly inside the provided virtual machine.

:::tip

### Exercise 2

Write an exploit that uses a buffer overflow to crash the web server (or one of the processes it creates). You do not need to inject code at this point. Verify that your exploit crashes the server by checking the last few lines of `dmesg | tail`, using `gdb`, or observing that the web server crashes (i.e., it will print `Child process 9999 terminated incorrectly, receiving signal 11`)

Provide the code for the exploit in a file called `exploit-2.py`.

The vulnerability you found in [Exercise 1](#exercise-1) may be too hard to exploit. Feel free to find and exploit a different vulnerability.

:::

You may find `gdb` useful in building your exploits (though it is not required for you to do so). As `zookd` forks off many processes (one for each client), it can be difficult to debug the correct one. The easiest way to do this is to run the web server ahead of time with `clean-env.sh` and then attaching `gdb` to an already-running process with the `-p` flag. You can find the PID of a process by using `pgrep`; for example, to attach to `zookd-exstack`, start the server and, in another shell, run

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ gdb -p $(pgrep zookd-)
...
(gdb) break your-breakpoint
Breakpoint 1 at 0x1234567: file zookd.c, line 999.
(gdb) continue
Continuing.
```

Keep in mind that a process being debugged by `gdb` will not get killed even if you terminate the parent `zookd` process using `Control + C (^C)`. If you are having trouble restarting the web server, check for leftover processes from the previous run, or be sure to exit `gdb` before restarting `zookd`. You can also save yourself some typing by using `b` instead of `break`, and `c` instead of `continue`.

When a process being debugged by `gdb` forks, by default `gdb` continues to debug the parent process and does not attach to the child. Since `zookd` forks a child process to service each request, you may find it helpful to have `gdb` attach to the child on fork, using the command `set follow-fork-mode child`. We have added that command to `~/labs/lab1_mem_vulnerabilities/.gdbinit`, which will take effect if you start `gdb` in that directory.

For this and subsequent exercises, you may need to encode your attack payload in different ways, depending on which vulnerability you are exploiting. In some cases, you may need to make sure that your attack payload is URL-encoded; that is, use `+` instead of space and `%2b` instead of `+`. Here is a [URL encoding reference](http://www.blooberry.com/indexdot/html/topics/urlencoding.htm) and a handy [conversion tool](https://www.url-encode-decode.com/). You can also use quoting functions in the python `urllib` module to URL encode strings. In other cases, you may need to include binary values into your payload. The Python [struct](http://docs.python.org/2/library/struct.html) module can help you do that. For example, `struct.pack("<Q", x)` will produce an 8-byte (64-bit) binary encoding of the integer `x`.

You can check whether your exploits crash the server as follows:

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ make check-crash
```

## B) Code injection

In this part, you will use your buffer overflow exploits to inject code into the web server. The goal of the injected code will be to unlink (remove) a sensitive file on the server, namely `/home/httpd/grades.txt`. Use `zookd-exstack`, since it has an executable stack that makes it easier to inject code. The `zookws` web server should be started as follows.

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ ./clean-env.sh ./zookd-exstack 8080
```

You can build the exploit in two steps. First, write the shell code that unlinks the sensitive file, namely `~/labs/lab1_mem_vulnerabilities/grades.txt`. Second, embed the compiled shell code in an HTTP request that triggers the buffer overflow in the web server.

When writing shell code, it is often easier to use assembly language rather than higher-level languages, such as C. This is because the exploit usually needs fine control over the stack layout, register values and code size. The C compiler will generate additional function preludes and perform various optimizations, which makes the compiled binary code unpredictable.

We have provided shell code for you to use in `~/labs/lab1_mem_vulnerabilities/shellcode.S`, along with `Makefile` rules that produce `~/labs/lab1_mem_vulnerabilities/shellcode.bin`, a compiled version of the shell code, when you run **make**. The provided shell code is intended to exploit setuid-root binaries, and thus it runs a shell. You will need to modify this shell code to instead unlink `/home/httpd/grades.txt`.

:::tip

### Exercise 3.1

Modify `shellcode.S` to unlink `/home/httpd/grades.txt`. Your assembly code can either invoke the `SYS_unlink` system call, or call the `unlink()` library function.

:::

To help you develop your shell code for this exercise, we have provided a program called `run-shellcode` that will run your binary shell code, as if you correctly jumped to its starting point. For example, running it on the provided shell code will cause the program to `execve("/bin/sh")`, thereby giving you another shell prompt:

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ ./run-shellcode shellcode.bin
```

To test whether the shell code does its job, run the following commands:

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ make
httpd@istd:~/labs/lab1_mem_vulnerabilities$ touch ~/grades.txt
httpd@istd:~/labs/lab1_mem_vulnerabilities$ ./run-shellcode shellcode.bin
httpd@istd:~/labs/lab1_mem_vulnerabilities$ ls ~/grades.txt
ls: cannot access /home/httpd/grades.txt: No such file or directory
```

You may find [strace](https://linux.die.net/man/1/strace) useful when trying to figure out what system calls your shellcode is making. Much like with `gdb`, you attach `strace` to a running program:

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ strace -f -p $(pgrep zookd-)
```

It will then print all of the system calls that program makes. If your shell code isn't working, try looking for the system call you think your shell code should be executing (i.e., `unlink`).

Next, we construct a malicious HTTP request that injects the compiled byte code to the web server, and hijack the server's control flow to run the injected code. When developing an exploit, you will have to think about what values are on the stack, so that you can modify them accordingly.

When you're constructing an exploit, you will often need to know the addresses of specific stack locations, or specific functions, in a particular program. One way to do this is to add `printf()` statements to the function in question. For example, you can use `printf("Pointer: %p\n", &x);` to print the address of variable `x` or function `x`. However, this approach requires some care: you need to make sure that your added statements are not themselves changing the stack layout or code layout. We (and **make check**) will be grading the lab without any `printf` statements you may have added.

A more fool-proof approach to determine addresses is to use `gdb`. For example, suppose you want to know the stack address of the `pn[]` array in the `http_serve` function in `zookd-exstack`, and the address of its saved return pointer. You can obtain them using `gdb` by first starting the web server (remember `clean-evn`!), and then attaching `gdb` to it:

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ gdb -p $(pgrep zookd-)
...
(gdb) break http_serve
Breakpoint 1 at 0x5555555561d2: file http.c, line 275.
(gdb) continue
Continuing.
```

Be sure to run `gdb` from the `~/labs/lab1_mem_vulnerabilities` directory, so that it picks up the `set follow-fork-mode child` command from `~/labs/lab1_mem_vulnerabilities/.gdbinit`. Now you can issue an HTTP request to the web server, so that it triggers the breakpoint, and so that you can examine the stack of `http_serve`.

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ curl localhost:8080
```

This will cause `gdb` to hit the breakpoint you set and halt execution, and give you an opportunity to ask `gdb` for addresses you are interested in:

```bash
Thread 2.1 "zookd-exstack" hit Breakpoint 1, http_serve (fd=4, name=0x55555575f80c "/") at http.c:275
275         void (*handler)(int, const char *) = http_serve_none;
(gdb) print &pn
$1 = (char (*)[2048]) 0x7fffffffd4b0
(gdb) info frame
Stack level 0, frame at 0x7fffffffdce0:
 rip = 0x55555555622e in http_serve (http.c:275); saved rip = 0x5555555558e5
 called by frame at 0x7fffffffed10
 source language c.
 Arglist at 0x7fffffffdcd0, args: fd=4, name=0x55555575f80c "/"
 Locals at 0x7fffffffdcd0, Previous frame's sp is 0x7fffffffdce0
 Saved registers:
  rbx at 0x7fffffffdcc8, rbp at 0x7fffffffdcd0, rip at 0x7fffffffdcd8
(gdb)
```

From this, you can tell that, at least for this invocation of `http_serve`, the `pn[]` buffer on the stack lives at address `0x7fffffffd4b0`, and the saved value of `%rip` (the return address in other words) is at `0x7fffffffdcd8`. If you want to see register contents, you can also use **info registers**.

:::tip

### Exercise 3.2

Now it's your turn to develop an exploit.

You can check whether your exploit works as follows:

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ make check-exstack
```

The test either prints "PASS" or "FAIL".

The standard C compiler used on Linux, gcc, implements a version of stack canaries (called SSP). You can explore whether GCC's version of stack canaries would or would not prevent a given vulnerability by using the SSP-enabled versions of `zookd`: `zookd-withssp`.

Submit your answers to the first two parts of this lab assignment by running **make prepare-submit-a** and upload the resulting `lab1a-handin.tar.gz` file to [edimension website](https://edimension.sutd.edu.sg).

:::

## C) Return-to-libc attacks

Many modern operating systems mark the stack non-executable in an attempt to make it more difficult to exploit buffer overflows. In this part, you will explore how this protection mechanism can be circumvented. Run the web server configured with binaries that have a non-executable stack, as follows.

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ ./clean-env.sh ./zookd-nxstack 8080
```

The key observation to exploiting buffer overflows with a non-executable stack is that you still control the program counter, after a `ret` instruction jumps to an address that you placed on the stack. Even though you cannot jump to the address of the overflowed buffer (it will not be executable), there's usually enough code in the vulnerable server's address space to perform the operation you want.

Thus, to bypass a non-executable stack, you need to first find the code you want to execute. This is often a function in the standard library, called libc, such as `execve`, `system`, or `unlink`. Then, you need to arrange for the stack and registers to be in a state consistent with calling that function with the desired arguments. Finally, you need to arrange for the `ret` instruction to jump to the function you found in the first step. This attack is often called a _return-to-libc_ attack.

One challenge with return-to-libc attacks is that you need to pass arguments to the libc function that you want to invoke. The x86-64 calling conventions make this a challenge because the first 6 arguments [are passed in registers](https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64). For example, the first argument must be in register `%rdi` (see `man 2 syscall`, which documents the calling convention). So, you need an instruction that loads the first argument into `%rdi`. In Exercise 3, you could have put that instruction in the buffer that your exploit overflows. But, in this part of the lab, the stack is marked non-executable, so executing the instruction would crash the server, but wouldn't execute the instruction.

The solution to this problem is to find a piece of code in the server that loads an address into `%rdi`. Such a piece of code is referred to as a "borrowed code chunk", or more generally as a [_rop gadget_](https://en.wikipedia.org/wiki/Return-oriented_programming), because it is a tool for return-oriented programming (rop). Luckily, `zookd.c` accidentally has a useful gadget: see the function `accidentally`.

:::tip

### Exercise 4

Starting from your exploit in [Exercise 2](#exercise-2) and [3.2](#exercise-3-2), construct an exploit that unlinks `/home/httpd/grades.txt` when run on the binaries that have a non-executable stack. Name this new exploit `exploit-4.py`.

In this attack you are going to take control of the server over the network _without injecting any code_ into the server. You should use a return-to-libc attack where you redirect control flow to code that already existed before your attack. The outline of the attack is to perform a buffer overflow that:

1. causes the argument to the chosen libc function to be on stack
2. then causes `accidentally` to run so that argument ends up in `%rdi`
3. and then causes `accidentally` to return to the chosen libc function

It will be helpful to draw a stack diagram like the figures in [Smashing the Stack in the 21st Century](https://thesquareplanet.com/blog/smashing-the-stack-21st-century/) at (1) the point that the buffer overflows and (2) at the point that `accidentally` runs.

You can test your exploits as follows:

```bash
httpd@istd:~/labs/lab1_mem_vulnerabilities$ make check-libc
```

:::

## D) Fixing buffer overflows and other bugs

Now that you have figured out how to exploit buffer overflows, you will try to find other kinds of vulnerabilities in the same code. As with many real-world applications, the "security" of our web server is not well-defined. Thus, you will need to use your imagination to think of a plausible threat model and policy for the web server.

:::tip

### Exercise 5

Look through the source code and try to find more vulnerabilities that can allow an attacker to compromise the security of the web server. Describe the attacks you have found in the `Assignment document`, along with an explanation of the limitations of the attack, what an attacker can accomplish, why it works, and how you might go about fixing or preventing it. You should ignore bugs in `zoobar`'s code. They will be addressed in future labs.

One approach for finding vulnerabilities is to trace the flow of inputs controlled by the attacker through the server code. At each point that the attacker's input is used, consider all the possible values the attacker might have provided at that point, and what the attacker can achieve in that manner.

You should find at least two vulnerabilities for this exercise.

:::

Finally, you will fix the vulnerabilities that you have exploited in this lab assignment.

:::tip

### Exercise 6

For each buffer overflow vulnerability you have exploited in Exercises 2, 3, and 4, fix the web server's code to prevent the vulnerability in the first place. Do not rely on compile-time or runtime mechanisms such as [stack canaries](https://en.wikipedia.org/wiki/Stack_buffer_overflow#Stack_canaries), removing `-fno-stack-protector`, baggy bounds checking, etc.

Make sure that your code actually stops your exploits from working. Use **make check-fixed** to run your exploits against your modified source code (as opposed to the staff reference binaries from `bin.tar.gz`). These checks should report FAIL (i.e., exploit no longer works). If they report PASS, this means the exploit still works, and you did not correctly fix the vulnerability.

Note that your submission should _not_ make changes to the `Makefile` and other grading scripts. We will use our unmodified version during grading.

You should also make sure your code still passes all tests using **make check**, which uses the unmodified lab binaries.

:::

You are done! Submit your answers to the lab assignment by running **make prepare-submit** and upload the resulting `lab1-handin.tar.gz` file to [edimension website](https://edimension.sutd.edu.sg).
