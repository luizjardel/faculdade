#include <stdio.h>
#include <stdbool.h>

#define N 3

typedef struct {
    int id;
    int burst;
} Processo;

void executarFIFO(Processo proc[]) {
    printf("\n--- ESCALONAMENTO FIFO (FCFS) ---\n");
    int espera = 0, turnaround = 0;
    
    for (int i = 0; i < N; i++) {
        turnaround += proc[i].burst;
        printf("Processo P%d | Tempo de Espera: %d ms | Turnaround: %d ms\n", 
            proc[i].id, espera, turnaround);
        espera += proc[i].burst;
    }
}

void executarSJF(Processo proc[]) {
    printf("\n--- ESCALONAMENTO SJF (Shortest Job First) ---\n");
    // Ordena uma cópia local pelo tempo de burst
    Processo p[N];
    for(int i = 0; i < N; i++) p[i] = proc[i];

    for (int i = 0; i < N - 1; i++) {
        for (int j = i + 1; j < N; j++) {
            if (p[i].burst > p[j].burst) {
                Processo temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
        }
    }

    int espera = 0, turnaround = 0;
    for (int i = 0; i < N; i++) {
        turnaround += p[i].burst;
        printf("Processo P%d | Tempo de Espera: %d ms | Turnaround: %d ms\n", 
               p[i].id, espera, turnaround);
        espera += p[i].burst;
    }
}

void executarRoundRobin(Processo proc[], int quantum) {
    printf("\n--- ESCALONAMENTO ROUND ROBIN (Quantum = %d ms) ---\n", quantum);
    int restante[N];
    int tempo_atual = 0;
    bool concluidos = false;

    for (int i = 0; i < N; i++) restante[i] = proc[i].burst;

    while (!concluidos) {
        concluidos = true;
        for (int i = 0; i < N; i++) {
            if (restante[i] > 0) {
                concluidos = false;
                if (restante[i] > quantum) {
                    tempo_atual += quantum;
                    restante[i] -= quantum;
                    printf("Tempo %2d ms: Processo P%d executou %d ms (Restante: %d ms)\n", 
                           tempo_atual, proc[i].id, quantum, restante[i]);
                } else {
                    tempo_atual += restante[i];
                    printf("Tempo %2d ms: Processo P%d CONCLUÍDO (Executou %d ms finais)\n", 
                           tempo_atual, proc[i].id, restante[i]);
                    restante[i] = 0;
                }
            }
        }
    }
}

int main() {
    Processo processos[N] = {{1, 10}, {2, 5}, {3, 8}};
    int opcao;

    do {
        printf("\n=========================================");
        printf("\n   SIMULADOR DE ESCALONAMENTO DE CPU");
        printf("\n=========================================");
        printf("\n1. Executar FIFO (FCFS)");
        printf("\n2. Executar Shortest Job First (SJF)");
        printf("\n3. Executar Round Robin (Quantum = 3ms)");
        printf("\n0. Sair");
        printf("\nEscolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                executarFIFO(processos);
                break;
            case 2:
                executarSJF(processos);
                break;
            case 3:
                executarRoundRobin(processos, 3);
                break;
            case 0:
                printf("\nEncerrando o simulador.\n");
                break;
            default:
                printf("\nOpcao invalida!\n");
        }
    } while (opcao != 0);

    return 0;
}