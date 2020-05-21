#include <stdio.h>
#include <stdlib.h>

char * my_gets(char * buf) {
  int c;

  while ((c = getchar()) != EOF && c != '\n')
  {
    *buf++ = c;
  }
  *buf = '\0';
  return buf;
}

int read_req(void) {
  char buf[8];
  int i;
  my_gets(buf);
  i = atoi(buf);
  return i;
}

int main() {
  int x = read_req();
  printf("x = %d\n", x);
}
