int main() {
    char buf[16];
    while (1) {
        if (fork()) { wait(0); }
        else { read(0, buf, 128); return; }
    }
}

