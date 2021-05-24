struct malloc_chunk {
  unsigned long mchunk_prev_size;
  unsigned long mchunk_size;
  struct malloc_chunk* fd;
  struct malloc_chunk* bk;
  struct malloc_chunk* fd_nextsize;
  struct malloc_chunk* bk_nextsize;
};


int main() {
 struct malloc_chunk fake_chunk = {0};
 unsigned long *a = malloc(16);

 printf("before poisoning, a: %p\n", a);
 
 fake_chunk.mchunk_prev_size = 0;
 fake_chunk.mchunk_size = 0x20;
 free(&fake_chunk.fd);

 a = malloc(16);
 printf("after poisoning, a: %p\n", a);
}
