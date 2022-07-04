#include <stdio.h>


int main()
{
    double x;
    FILE *fp;
    fp = fopen("uni.dat", "r");
   for(int i=0; i<1000000; i++) 
        {
            fscanf(fp, "%lf", &x);
            printf("%lf\n", x);
        }
}
