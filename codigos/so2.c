
#include <stdio.h>
int main() {
    int n = 3; // Quantidade de processos

    // Arrays para armazenar as propriedades de cada processo
    int id[] = {1, 2, 3};          // PID dos processos
    int tempo_exec[] = {5, 3, 8};  // Tempo de CPU (Burst Time)
    int tempo_espera[3];          // Tempo aguardando na fila
    int turnaround[3];            // Tempo total (espera + execução)

    // O primeiro processo a chegar não espera nada
    tempo_espera[0] = 0;
    turnaround[0] = tempo_exec[0];

    // Calculando o tempo de espera e turnaround para os próximos processos
    for (int i = 1; i < n; i++) {
        // O tempo de espera é o tempo de espera do anterior + o tempo que o anterior executou
        tempo_espera[i] = tempo_espera[i - 1] + tempo_exec[i - 1];
        
        // Turnaround é a soma da espera com o próprio tempo de execução
        turnaround[i] = tempo_espera[i] + tempo_exec[i];
    }

    // Exibição da tabela de resultados
    float soma_espera = 0, soma_turnaround = 0;

    printf("PID\tBurst\tEspera\tTurnaround\n");
    printf("-----------------------------------\n");

    for (int i = 0; i < n; i++) {
        soma_espera += tempo_espera[i];
        soma_turnaround += turnaround[i];

        printf("P%d\t%d\t%d\t%d\n", id[i], tempo_exec[i], tempo_espera[i], turnaround[i]);
    }

    printf("\nTempo Medio de Espera: %.2f\n", soma_espera / n);
    printf("Tempo Medio de Turnaround: %.2f\n", soma_turnaround / n);

    return 0;
} 