int main() {
  char name[16];
  read(0, name, 128);
}
int foo() {
  return open("/flag", 0);
}
int bar() {
   int x = open("/notflag", 0);
   sendfile(1, x, 0, 1024);
}

