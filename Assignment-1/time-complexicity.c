#include<stdio.h>
#include<time.h>

int constant_time(int n)
{
    int result;
    result = n * n;
    return result;
}

int linear_time(int n)
{
    int i, total = 0;
    for (i = 0; i < n; i++)
    {
        total = total + i;
    }
    return total;
}

int quadratic_time(int n)
{
    int i, j, count = 0;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            count = count + 1;
        }
    }
    return count;
}

int main()
{
    int sizes[8] = {100, 500, 1000, 2000, 5000, 12345,123456,99999};
    int n, k;
    clock_t start, end;
    double time_used;

    printf("Input\tO(1)\t\tO(n)\t\tO(n^2)\n");

    for (k = 0; k < 8; k++)
    {
        n = sizes[k];

        start = clock();
        constant_time(n);
        end = clock();
        time_used = (double)(end - start) / CLOCKS_PER_SEC;
        printf("%d\t%.6f", n, time_used);

        start = clock();
        linear_time(n);
        end = clock();
        time_used = (double)(end - start) / CLOCKS_PER_SEC;
        printf("\t%.6f", time_used);

        start = clock();
        quadratic_time(n);
        end = clock();
        time_used = (double)(end - start) / CLOCKS_PER_SEC;
        printf("\t%.6f\n", time_used);
    }

    return 0;
}
