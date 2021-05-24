int main() {
 void *a, *b, *c, *d, *e, *f, *x, *y, *z;
 a = malloc(16);
 b = malloc(16);
 c = malloc(32);
 d = malloc(48);
 e = malloc(32);
 f = malloc(32);

 x = malloc(64);
 y = malloc(64);
 z = malloc(64);

 // adding to tcache
 free(b);
 free(a);
 free(f);
 free(e);
 free(c);
 free(d);
}

