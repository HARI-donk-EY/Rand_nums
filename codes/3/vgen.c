#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../coeffs.h"


void vgen(char *str, int len)
{
    
    int i;
    FILE *fp;
    double x;
    fp = fopen(str,"w");
    //Generate numbers
    for (i = 0; i < len; i++)
        {
            x = (double)rand()/RAND_MAX;
            fprintf(fp,"%lf\n", (-2)*(log(1-x)));
        }
    fclose(fp);

}



int main()
{

    vgen("vdat.dat", 1000000);

}

