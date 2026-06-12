#include <stdio.h>
#include <pthread.h>

#define THREADS 4
#define INCREMENTS 1000000

long long counter = 0;

/* Mutex variable */
pthread_mutex_t lock;

/* Thread function without synchronization */
void* increment_without_mutex(void* arg) {

    for (int i = 0; i < INCREMENTS; i++) {
        counter++;
    }

    return NULL;
}

/* Thread function with mutex synchronization */
void* increment_with_mutex(void* arg) {

    for (int i = 0; i < INCREMENTS; i++) {

        /* Lock critical section */
        pthread_mutex_lock(&lock);

        counter++;

        /* Unlock critical section */
        pthread_mutex_unlock(&lock);
    }

    return NULL;
}

int main() {

    pthread_t threads[THREADS];

    printf("===== WITHOUT MUTEX (Race Condition) =====\n");

    counter = 0;

    /* Create threads without synchronization */
    for (int i = 0; i < THREADS; i++) {
        pthread_create(&threads[i], NULL, increment_without_mutex, NULL);
    }

    /* Wait for all threads */
    for (int i = 0; i < THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Expected Counter Value : %d\n", THREADS * INCREMENTS);
    printf("Actual Counter Value   : %lld\n\n", counter);


    printf("===== WITH MUTEX (Synchronized) =====\n");

    counter = 0;

    /* Initialize mutex */
    pthread_mutex_init(&lock, NULL);

    /* Create threads with mutex synchronization */
    for (int i = 0; i < THREADS; i++) {
        pthread_create(&threads[i], NULL, increment_with_mutex, NULL);
    }

    /* Wait for all threads */
    for (int i = 0; i < THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Expected Counter Value : %d\n", THREADS * INCREMENTS);
    printf("Actual Counter Value   : %lld\n", counter);

    /* Destroy mutex */
    pthread_mutex_destroy(&lock);

    return 0;
}