# Introduction

Exploiting buffer overflows requires precise control over the execution environment. A small change in the compiler, environment variables, or the way the program is executed can result in slightly different memory layout and code structure, thus requiring a different exploit. For this reason, this lab uses a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) to run the vulnerable web server code.

# Setup VM

#### 1) Download VM software

To start working on this lab assignment, you'll need software that lets you run a virtual machine. On Windows, Mac or Linux, use [Oracle VM Virtual](https://ist.mit.edu/vmware/workstation) available on the Downloads tab.

#### 2) Download VM Image

Once you have virtual machine software installed on your machine, you should download the [course VM image](https://people.csail.mit.edu/jfrg/6.858-x86_64-v19.zip), and unpack it on your computer. This virtual machine contains an installation of Debian 9.7 Linux.

#### 3) Import & Configure VM Image

To start the course VM using VMware, import `ISTD50044.vdi`. Go to File > New, select "create a custom virtual machine", choose Linux > Debian 9.x 64-bit, choose Legacy BIOS, and use an existing virtual disk (and select the `ISTD50044.vdi` file, choosing the "Take this disk away" option). Finally, click Finish to complete the setup.

#### 4) Start VM

To start the VM with kvm, run **./6.858-x86_64-v19.sh** from a terminal (`Ctrl+A x` to force quit). If you get a permission denied error from this script, try adding yourself to the `kvm` group with `sudo gpasswd -a`whoami`kvm`, then log out and log back in.

:::tip

#### VM Credentials

**You'll use two accounts on the VM:**

| Username | Password | Description                                                                                                                                                                      |
| :------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `httpd`  | `httpd`  | You should use the `httpd` account for your work. By default the VM should login to this account when started.                                                                   |
| `root`   | `root`   | You can use the `root` account to install new software packages with **apt-get install \*pkgname\***. Or you can log in as `httpd` and run the command with the **sudo** prefix. |

:::

#### 5) Connect to the VM via SSH

You can either log into the virtual machine using its console, or use ssh to log into the virtual machine over the (virtual) network. The latter also lets you easily copy files into and out of the virtual machine with `scp` or `rsync`. How you access the virtual machine over the network depends on how you're running it. If you're using VMWare, you'll first have to find the virtual machine's IP address. To do so, log in as root on the console, run **ip addr show dev eth0**, and note the IP address listed beside `inet`. With kvm, you can use `localhost` as the IP address for ssh and HTTP. You can now log in with ssh by running the following command from your host machine: **ssh -p 2222 httpd@IPADDRESS**. To avoid having to type the password each time, you may want to set up an [SSH Key](https://www.booleanworld.com/set-ssh-keys-linux-unix-server/).

#### 6) Download Labs repository

The files you will need for this and subsequent labs are distributed using the [Git](http://git-scm.com/)[overview of Git](https://hacker-tools.github.io/version-control/)[Git user's manual](http://www.kernel.org/pub/software/scm/git/docs/user-manual.html). The course Git repository is available at **https://web.mit.edu/6858/2019/lab.git**. To get the lab code, log into the VM using the `httpd` account and clone the source code for lab 1 as follows:

```
httpd@6858-v19:~$ git clone https://web.mit.edu/6858/2019/lab.git
Cloning into 'lab'...
httpd@6858-v19:~$ cd lab
httpd@6858-v19:~/lab$
```

# Labs

Now that you have your environment ready, follow the `Labs Guide link` on the toolbar to proceed with the lab.
