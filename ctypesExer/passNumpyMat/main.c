#include<stdio.h>
#include "indexing.h"
#include"handletensor.h"

int main(int argc, char const *argv[])
{
    float img[P*H*W];
    float ret[2*P*H*W];

    for(int i=0;i<3;i++){
        for(int j=0;j<4;j++){
            for(int k=0;k<5;k++){
                img[at(i,j,k)]=1;
            }
        }
    }

    handle_tensor(img,ret);
    printf("%f\n", ret[0]);
    return 0;
}