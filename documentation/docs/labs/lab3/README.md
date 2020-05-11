# Lab 3 - Web Security

## Introduction

This lab will introduce you to browser-based attacks, as well as to how one might go about preventing them. The lab has several parts:

- Part A: cross-site scripting attack
- Part B: cross-site request forgery
- Part C: side channel and phishing attack
- Part D: profile worm

Each part has several exercises that help you build up an attack. All attacks will involve exploiting weaknesses in the zoobar site, but these are representative of weaknesses found in real web sites.

### Network setup

For this lab, you will be crafting attacks in your web browser that exploit vulnerabilities in the zoobar web application. To ensure that your exploits work on our machines when we grade your lab, we need to agree on the URL that refers to the zoobar web site. For the purposes of this lab, your zoobar web site must be acessible on `http://localhost:8080/`. If you have been using the default VM's, this configuration should work out of the box.

### Setting up the web server

Before you begin working on these exercises, please use Git to commit your Lab 3 solutions, fetch the latest version of the course repository, and then create a local branch called `lab4` based on our lab4 branch, `origin/lab4`. Do _not_ merge your lab 2 and 3 solutions into lab 4. Here are the shell commands:

```bash
httpd@istd:~$ cd labs/lab3_web_security
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

Exercises 5, 13, and 14, require that the displayed site look a certain way. The `make check` script is not smart enough to compare how the site looks with and without your attack, so you will need to do that comparison yourself (and so will we, during grading). When `make check` runs, it generates reference images for what the attack page is _supposed_ to look like (`answer-XX.ref.png`) and what your attack page actually shows (`answer-XX.png`), and places them in the `lab4-tests/` directory. Make sure that your `answer-XX.png` screenshots look like the reference images in `answer-XX.ref.png`. To view these images from `lab4-tests/`, copy them to your local machine, or open them via the VSCode online editor exposed by the VM ([http://127.0.0.1:3000/](http://127.0.0.1:3000/)).

## A) cross-site scripting (XSS) attack

The zoobar users page has a flaw that allows theft of a logged-in user's cookie from the user's browser, if an attacker can trick the user into clicking a specially-crafted URL constructed by the attacker. Your job is to construct such a URL. An attacker might e-mail the URL to the victim user, hoping the victim will click on it. A real attacker could use a stolen cookie to impersonate the victim.

You will develop the attack in several steps. To learn the necessary infrastructure for constructing the attacks, you first do a few exercises that familiarize yourself with Javascript, the DOM, etc.

:::tip

### Exercise 1

#### Print cookie

1. Read about how [cookies are accessed from Javascript](https://developer.mozilla.org/en-US/docs/Web/API/document.cookie).

2. Save a copy of `zoobar/templates/users.html` (you'll need to restore this original version later). Add a `<script>` tag to `users.html` that prints the logged-in user's cookie using `alert()`.

   Your script might not work immediately if you made a Javascript programming error. Fortunately, Chrome has fantastic debugging tools accessible in the Inspector: the JavaScript console, the DOM inspector, and the Network monitor. The JavaScript console lets you see which exceptions are being thrown and why. The DOM Inspector lets you peek at the structure of the page and the properties and methods of each node it contains. The Network monitor allows you to inspect the requests going between your browser and the website. By clicking on one of the requests, you can see what cookie your browser is sending, and compare it to what your script prints.

3. Put the contents of your script in a file named `answer-1.js`. Your file should only contain javascript (don't include `<script>` tags).

:::
