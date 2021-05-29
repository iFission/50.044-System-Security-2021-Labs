# Course VMs
There are 2 VMs you will need for this course: one is for your group project, the other is for  
practicing CTF challenges. 

## Setup Project VM

Exploiting buffer overflows requires precise control over the execution environment. A small change in the compiler, environment variables, or the way the program is executed can result in slightly different memory layout and code structure, thus requiring a different exploit. For this reason, this lab uses a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) to run the vulnerable web server code.

![home](/labs/setup_vm/home.png)

### 1) Download VM software

To start working on this lab assignment, you'll need software that lets you run a virtual machine. On Windows, Mac or Linux, use [Oracle VM Virtual Box 6.1.6](https://www.virtualbox.org/wiki/Downloads) available on the `Downloads tab`.

### 2) Download VM Image

Once you have virtual machine software installed on your machine, you should download the [ISTD50044.ova](https://drive.google.com/file/d/1iKXW7YgwMLvZITnJCX8oYDrKlgtouarQ/view?usp=sharing) (available on `Downloads tab`) to your computer. This virtual machine image contains an installation of Debian 9.7 Linux.

### 3) Import & Configure VM Image

To import the course VM, open Oracle VM Virtual Box and import `ISTD50044.ova`. Go to `File > Import Appliance`, select the file `ISTD50044.ova` and proceed the import process with the default settings. After some minutes the import process should finish and Oracle VM Virtual Box should will list the VM.

By default the VM image is imported with the correct NAT network settings, however you can verify if such configuration is correct. Go to `Settings > Network > Advanced` and open the `Port Forwarding window`. The Ports forwarding should be configured as the Figure below:

![nat_settings](/labs/setup_vm/nat_settings.png)

### 4) Start VM

To start the VM, simply select the **ISTD50044** entry and click on the Start button (Green right arrow on toolbar). If you get a firewall prompt, you can accept to allow the VM to open **ports 22000, 8080 and 3000** so you can connect and browse the labs apps.

![import_vm](/labs/setup_vm/import_vm.gif)

:::tip

#### VM Credentials

You'll use two accounts on the VM, the user account (**httpd**) and root. By default, the VM automatically logins **httpd** user.

| Username | Password | Description                                                                                                                                                                      |
| :------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `httpd`  | `httpd`  | You should use the `httpd` account for your work. By default the VM should login to this account when started.                                                                   |
| `root`   | `root`   | You can use the `root` account to install new software packages with **apt-get install \*pkgname\***. Or you can log in as `httpd` and run the command with the **sudo** prefix. |

:::

### 5) Connect to the VM

#### SSH Client

You can either log into the virtual machine using its console, or use SSH to log into the virtual machine over the (virtual) network. You can use any SSH client to access the VM, but we recommend using [MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html) as it provides easy access to VM's files via SFTP protocol. As the VM forwards it SSH port (22) to the host port 22000 by default, the SSH access is done via the localhost (httpd@127.0.0.1:22000). The configuration using MobaXterm SSH client is shown below.

![mobaxterm](/labs/setup_vm/mobaxterm.png)

#### VSCode IDE

After the VM is running, you can also access the online VSCode IDE which allows easy code browsing of the labs files.

![vscode](/labs/setup_vm/vscode.png)

#### Labs

Now that you have your environment ready, follow the link to [Lab 1](/labs/lab1/).


## Setup CTF VM

The practice VM image for CTF exercises can be downloaded here
[ctfd-vm.ova](https://drive.google.com/file/d/1SB2R-YDrRpRO-a3jNgEi-D1ztYi8C7TK/view?usp=sharing) or
directly from the `Download tab`. The VM is loaded with all challenges and necessary libaries. It is 
is roughly 6GB in size, and contains Ubuntu 20.04. It has been tested with VirtualBox 6.1.

Once started, you can SSH to it via port 22222 at 127.0.0.1. Specifically,


`ssh -p 22222 ctf@127.0.0.1`

where the password for ctf is `qwertyu`.

