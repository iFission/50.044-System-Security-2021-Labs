int main(int argc, char **argv) {
	char name[8]={0};
	char flag[64];
	read(open("/flag", 0), flag, 64); 
	puts("Name: ");
	read(0, name, 8); 
	puts(name);
}
