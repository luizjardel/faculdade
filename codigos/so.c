//Aula de Sistemas Operacionais
#include<stdio.h>
#include<stdlib.h>
int main(){
    int nota[5],i;
    for(i=0;i<5;i++){
        printf("Digite o vetor [%d]: ",i,nota[i]);
        scanf("%d",&nota[i]);
    }
}