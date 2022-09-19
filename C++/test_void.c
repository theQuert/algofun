# include <stdio.h>
# define INCREMENT(x) ++x
# define MULTIPLY(a, b) (a)*(b)
# define merge(a, b) a##b
# define PRINT(i, limit) while (i < limit) \
                        {\
                          printf("Geek"); \
                          i++; \
                        }
// # define square(x) (x)*(x)

static inline int square(int x) {return x*x;}
/* int main()
{
    static int i = 5;
    if(--i)
    {
        printf("%d\n", i);
        
        main(10);
    }

} */
/*
int main()
{
    char *ptr = "Test";
    int x = 10;
    printf("%s\n", INCREMENT(ptr));
    printf("%d\n", INCREMENT(x));
    return 0;

} */
/*
int main()
{
   printf("%d", MULTIPLY(2+3, 3+5));

   return 0;
} */
/*
int main()
{
    printf("%d", merge(12, 34));

    return 0;
} */
/*
int main()
{
    int i = 0;
    PRINT(i, 3);

    return 0;
}
*/

int main()
{
    int x = 36;
    // printf("%d", square(x));
    int ans = 36/square(6);
    printf("%d", ans);

    return 0;
}
