int main() {
	void *x = malloc(4);
	void *y = malloc(8);
	void *z = malloc(32);
	void *u = malloc(4);
	printf("x: %p\n", x);
	printf("y: %p\n", y);
	printf("z: %p\n", z);
	printf("u: %p\n", u);

	printf("... freeing x\n");
	free(x);
	printf("... allocate 4 byte\n");
	void *v = malloc(4);
	printf("v: %p\n", v);
	return 0;
}
