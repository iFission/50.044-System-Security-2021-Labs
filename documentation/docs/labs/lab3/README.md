# Lab 3 - Web Security

## A) Introduction

This lab will introduce you to browser-based attacks, as well as to how one might go about preventing them. The lab has several parts:

- Part 1: cross-site scripting attack
- Part 2: cross-site request forgery
- Part 3: side channel and phishing attack
- Part 4: a profile worm

Each part has several exercises that help you build up an attack. All attacks will involve exploiting weaknesses in the zoobar site, but these are representative of weaknesses found in real web sites.

### Network setup

For this lab, you will be crafting attacks in your web browser that exploit vulnerabilities in the zoobar web application. To ensure that your exploits work on our machines when we grade your lab, we need to agree on the URL that refers to the zoobar web site. For the purposes of this lab, your zoobar web site must be acessible on `http://localhost:8080/`. If you have been using the default VM's, this configuration should work out of the box.

### Setting up the web server

Before you begin working on these exercises, please use Git to commit your Lab 3 solutions, fetch the latest version of the course repository, and then create a local branch called `lab4` based on our lab4 branch, `origin/lab4`. Do _not_ merge your lab 2 and 3 solutions into lab 4. Here are the shell commands:

```bash
httpd@istd:~$ cd labs/lab3_web_security
httpd@istd:~/labs/lab3_web_security$ git commit -am 'my solution to lab3'
[lab3 c54dd4d] my solution to lab3
 1 files changed, 1 insertions(+), 0 deletions(-)
httpd@istd:~/labs/lab3_web_security$ git pull
Already up-to-date.
httpd@istd:~/labs/lab3_web_security$ git checkout -b lab4 origin/lab4
Branch lab4 set up to track remote branch lab4 from origin.
Switched to a new branch 'lab4'
httpd@istd:~/labs/lab3_web_security$ make
...
```

Note that lab 4's source code is based on the initial web server from lab 1. It does not include privilege separation or Python profiles.

Now you can start the `zookws` web server, as follows.

```bash
httpd@istd:~/labs/lab3_web_security$ ./zookld
```

Open your browser and go to the URL `http://localhost:8080/`. You should see the `zoobar` web application. If you don't, go back and double-check your steps. If you cannot get the web server to work, get in touch with course staff before proceeding further.

### Crafting attacks

You will craft a series of attacks against the `zoobar` web site you have been working on in previous labs. These attacks exploit vulnerabilities in the web application's design and implementation. Each attack presents a distinct scenario with unique goals and constraints, although in some cases you may be able to re-use parts of your code.

We will run your attacks after wiping clean the database of registered users (except the user named "attacker"), so do not assume the presence of any other users in your submitted attacks.

You can run our tests with `make check`; this will execute your attacks against the server, and tell you whether your exploits are working correctly. As in previous labs, keep in mind that the checks performed by `make check` are not exhaustive, especially with respect to race conditions. You may wish to run the tests multiple times to convince yourself that your exploits are robust.
