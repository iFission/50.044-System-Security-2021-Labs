#include <unistd.h>
#include <sys/mman.h>
#include <sys/time.h>
#include <stdlib.h>

int main(int argc, char **argv) {
	struct timeval start, end;
	
	gettimeofday(&start, NULL);
	void *page = mmap(0x1337000, 0x1000, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANON, 0, 0);
	gettimeofday(&end, NULL);
	printf("mmap time: %f\n", ((end.tv_sec-start.tv_sec)*1e9 + (end.tv_usec-start.tv_usec))); 
	
	gettimeofday(&start, NULL);
	void *x= malloc(16); 
	gettimeofday(&end, NULL);
	printf("malloc time: %f\n", ((end.tv_sec-start.tv_sec)*1e9 + (end.tv_usec-start.tv_usec))); 
	
	gettimeofday(&start, NULL);
	void *y= malloc(16); 
	gettimeofday(&end, NULL);
	printf("malloc 2 time: %f\n", ((end.tv_sec-start.tv_sec)*1e9 + (end.tv_usec-start.tv_usec))); 

	return 0;
}
