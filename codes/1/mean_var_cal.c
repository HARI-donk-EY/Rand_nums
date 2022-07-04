#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../coeffs.h"

int main()
{


    double x_0 = mean("uni.dat");
    printf("mean:\t\t%lf\n",x_0);

    double sum = variance("uni.dat");

    printf("varience:\t%lf\n", sum);

    return 0;

}
