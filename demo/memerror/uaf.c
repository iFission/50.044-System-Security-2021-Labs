int main() {
  void *secret = malloc(32);
  strcpy(secret, "1234567890123456789012");
  printf("secret: %s\n", secret);
  free(secret);
  printf("after free, secret: %s\n", secret);
  printf("after free, secret+16: %s\n", secret+0x10);
  return 0;
}
