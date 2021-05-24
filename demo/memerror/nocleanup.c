int foo() {
	char data[8];
	puts("do nothing");
}
int bar() {
	char secret[8]="aaaaaa";
	puts("cannot see this!");
}
int main(int argc, char **argv) {
	bar();
	foo();
}
