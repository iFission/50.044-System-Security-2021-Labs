void vuln() {
 char small_buffer[16];
 read(0, small_buffer, 128);
}
int main(int argc, char **argv, char **envp)
{
  vuln();
  puts("Bye!");
}
void win() {
  sendfile(1, open("/flag", 0), 0, 0x1000);
}
