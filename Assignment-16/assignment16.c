#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define ITEMS 10

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;

/* Semaphores */
sem_t empty;
sem_t full;

/* Mutex for shared memory access */
pthread_mutex_t mutex;

/* Producer Thread */
void* producer(void* arg) {

    for (int i = 1; i <= ITEMS; i++) {

        /* Wait if buffer is full */
        sem_wait(&empty);

        /* Lock critical section */
        pthread_mutex_lock(&mutex);

        buffer[in] = i;

        printf("Producer produced item %d at position %d\n", i, in);

        in = (in + 1) % BUFFER_SIZE;

        /* Unlock critical section */
        pthread_mutex_unlock(&mutex);

        /* Increase full count */
        sem_post(&full);

        sleep(1);
    }

    return NULL;
}

/* Consumer Thread */
void* consumer(void* arg) {

    for (int i = 1; i <= ITEMS; i++) {

        /* Wait if buffer is empty */
        sem_wait(&full);

        /* Lock critical section */
        pthread_mutex_lock(&mutex);

        int item = buffer[out];

        printf("Consumer consumed item %d from position %d\n", item, out);

        out = (out + 1) % BUFFER_SIZE;

        /* Unlock critical section */
        pthread_mutex_unlock(&mutex);

        /* Increase empty count */
        sem_post(&empty);

        sleep(2);
    }

    return NULL;
}

int main() {

    pthread_t producer_thread;
    pthread_t consumer_thread;

    /* Initialize semaphores */
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);

    /* Initialize mutex */
    pthread_mutex_init(&mutex, NULL);

    /* Create threads */
    pthread_create(&producer_thread, NULL, producer, NULL);
    pthread_create(&consumer_thread, NULL, consumer, NULL);

    /* Wait for threads */
    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);

    /* Destroy synchronization tools */
    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);

    printf("\nAll items produced and consumed successfully.\n");

    return 0;
}