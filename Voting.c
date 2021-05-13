#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <pthread.h>

#define MEM_SIZ 4096
#define KOMISJE 5
#define ILOSC_GLOSOW 100000

struct partia{
	int glosy[5];
	pthread_mutexattr_t mutex_attr[5];
	pthread_mutex_t mutex[5];
};

double pomiar_rea();

double time_start;
double time_stop;

int main(){

int shmid;
void *pamiec_wspolna = (void *)0;
struct partia *wspolna;
int* glosy;
int oddano;
int suma = 0;
pthread_mutexattr_t *mutex_attr;
pthread_mutex_t *mutex;

int parties[5] = {0, 0, 0, 0, 0};

shmid = shmget((key_t)1111, MEM_SIZ, 0666 | IPC_CREAT);

if (shmid == -1){
	perror("blad shmget");
	exit(-1);
	}

pamiec_wspolna = shmat(shmid, (void *)0, 0);

if (pamiec_wspolna == (void *)-1) {
	perror("porazka shmat");
	exit(-2);
	}

wspolna = (struct partia *)pamiec_wspolna;

glosy = wspolna->glosy;

// MUTEX
for(int i=0; i<5; i++){
	pthread_mutexattr_init(&wspolna->mutex_attr[i]);
	pthread_mutexattr_setpshared(&wspolna->mutex_attr[i], PTHREAD_PROCESS_SHARED);

	if( pthread_mutex_init(&wspolna->mutex[i], &wspolna->mutex_attr[i]) < 0){
		puts("Blad 1");
		exit(1);
	}
}


// INICJALIZACJIA
for(int i =0; i<5; i++){
	glosy[i] = 0;
}

//POMIAR CZASU
time_start = pomiar_rea();
// GLOSOWANIE
for(int i =0; i<KOMISJE; i++){                                                                         
	if(fork() == 0){
	srand(getpid());
	for(int j=0; j<ILOSC_GLOSOW; j++){
		oddano=rand()%5;
		pthread_mutex_lock(&wspolna->mutex[oddano]);
		glosy[oddano] += 1;
		pthread_mutex_unlock(&wspolna->mutex[oddano]);
		}
	exit(0);
	}       
                                                    
} 

for(int i=0; i<KOMISJE; i++){
	wait(NULL);
}
// CZAS STOP
time_stop = pomiar_rea();

for(int i =0; i<5; i++){                                                                         
	suma += glosy[i];
	printf("Partia: %d uzyskala: %d glosow.\n", i+1, glosy[i]);                                                                    
}  
printf("\nSuma glosow: %d\n", suma);

// NISZCZENIE MUTEXA
for(int i=0; i<5; i++){
pthread_mutex_destroy(&wspolna->mutex[i]);
}

printf("\nPOMIAR REA: %.3f\n", time_stop-time_start);

return 0;
}

double pomiar_rea(){

        struct timeval  tv1;
        gettimeofday(&tv1, NULL);
        return (double) ( tv1.tv_usec) / 1000000 + (double) ( tv1.tv_sec);
}
