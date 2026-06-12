#include <stdio.h>

/* O(1) space */
int constant_space(int n)
{
    int x;
    return sizeof(x);
}

/* O(n) space */
int linear_space(int n)
{
    int arr[n];
    return sizeof(arr);
}

/* O(n^2) space */
int quadratic_space(int n)
{
    int arr[n][n];
    return sizeof(arr);
}

int main()
{
    int sizes[5] = {10, 50, 100, 200, 300};
    int i, n;

    printf("Space Complexity Observation\n");
    printf("----------------------------------------\n");

    for (i = 0; i < 5; i++)
    {
        n = sizes[i];

        printf("\nFor input size n = %d\n", n);
        printf("Constant space uses about %d bytes (does not grow with n).\n",
               constant_space(n));

        printf("Linear space uses about %d bytes (grows proportionally with n).\n",
               linear_space(n));

        printf("Quadratic space uses about %d bytes (grows very fast with n).\n",
               quadratic_space(n));
    }

    return 0;
}
