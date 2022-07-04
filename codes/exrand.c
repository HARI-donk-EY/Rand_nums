#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
    FILE *fp; 

// Uniform random numbers
    //uniform("uni.dat", 1000000);

    fp = fopen("uni.dat", "r");

//  Gaussian random numbers
    //gaussian("gau.dat", 1000000);

//Mean of uniform

double x_0 = mean("uni.dat"); 
printf("mean:\t\t%lf\n",x_0);

// For varience:


double sum = 0;
double x_i;

for(int i =0; i<1000000; i++)
    {
        fscanf(fp, "%lf", &x_i);
        sum += pow((x_i - x_0), 2);
    }

sum /= 1000000;

printf("varience:\t%lf\n", sum);

return 0;
}


