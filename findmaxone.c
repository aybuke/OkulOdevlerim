#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int i, j, n;
    int sayac = 0;
    int sonsayac = 0;
    int sutun=0;

    printf("satir sayisi giriniz: ");
    scanf("%d", &n);
    int dizi[n][10];
    srand(time(NULL));
    for(i=0; i<n; i++){
             for(j=0; j<10; j++){

                      dizi[i][j]=rand()%2;
                      printf("%d\t", dizi[i][j]);
                      }
             printf("\n");
             }

    for (j=0; j<10;j++){
        for(i=0; i<n; i++){
                 if(dizi[i][j]==1)
                                   sayac++;
            }
            if(sayac > sonsayac){
                     sonsayac=sayac;
                     sutun=j;
                     }
            sayac=0;
             }

    printf("en fazla 1 % d .inci sutunda ve %d tane var\n",sutun+1, sonsayac);

  return 0;
}
