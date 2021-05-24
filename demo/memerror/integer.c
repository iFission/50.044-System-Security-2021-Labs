int main() {
	int size;
	char buf[16];
	scanf("%i", &size);
	if (size > 16) exit(1);
	read(0, buf, size);
}

