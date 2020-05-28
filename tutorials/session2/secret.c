#include <stdio.h>

#include <stdlib.h>

int secret = 0;

char * my_gets(char * buf) {

  int c;

  while ((c = getchar()) != EOF && c != '\n')

    *
    buf++ = c;

  * buf = '\0';

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

  if (secret == 1)
    puts("secret");

  printf("x = %d\n", x);

}