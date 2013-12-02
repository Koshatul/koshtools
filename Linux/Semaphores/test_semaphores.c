/*
	Semaphore test.
	
	Compile with: gcc -lpthread -o test_semaphores test_semaphores.c
	
	Copied from: https://www.mail-archive.com/sage-devel@googlegroups.com/msg63592.html
	Author: Andrey Novoseltsev
 */

#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <semaphore.h>
#include <sys/stat.h>

int main(void) {
  sem_t *a = sem_open("/autoconf", O_CREAT, S_IRUSR|S_IWUSR, 0);
  if (a == SEM_FAILED) {
    perror("sem_open");
    return 1;
  }
  printf("All OK!\n");
  sem_close(a);
  sem_unlink("/autoconf");
  return 0;
}
