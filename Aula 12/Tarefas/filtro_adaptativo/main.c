#include <stdio.h>

int main(){

    FILE *Data_in, *Data_out;

    if((Data_in = fopen("wn.pcm", "rb")) == NULL){

        printf("\nO arquivo de entrada n�o abriu");
        return 0;
    }

    if((Data_out = fopen("SaidaIdentificacao.pcm", "wb")) == NULL){

        printf("\nO arquivo de saida nao abriu");
        return 0;
    }

    float u = 0.000000000005;
    // Cumprimento dos filtros
    int N = 10, i, j;
    int Nmax = N;

    // Pegando a largura do FILE de entrada
    fseek(Data_in, 0L, SEEK_END);
    long int len = ftell(Data_in);
    fclose(Data_in);

    if((Data_in = fopen("wn.pcm", "rb")) == NULL){

        printf("\nO arquivo de entrada n�o abriu");
        return 0;
    }

    // Criando os vetores  para ser utilziados
    short wn[N], yn[Nmax], x_linhan[Nmax];            // si no funciona cambiar a float
    for(i = 0; i < Nmax; i++)
    {
        wn[i] = 0;
        yn[i] = 0;
        x_linhan[i] = 0;
    }

    // Definindo a planta
    short Wo[] = {0.5, 0.3, -0.5, 0.8}, y, d_new;
    int NWo = 4, amostras;

    // Criando mais vetores
    short  Read, ee, e_salva[len], y_salva[len], w_salva[len][N], x_new = 0;

    for(i = 0; i < len; i++)
    {
        e_salva[i] = 0;
        y_salva[i] = 0;
        
        for(j = 0; j < N; j++)
        {
            w_salva[i][j] = 0;
        } 
    }

    for(i = 0; i < len; i++)
    {
        // Lendo a amostra de entrada
        amostras = fread(&Read, sizeof(short), 1, Data_in);
        x_new = Read;

        // Filtrando o sinal de entrada x
        x_linhan[i] = x_new;

        y = 0;

        for(j = 0; j < N; j++)
        {
            y = y + x_linhan[j] * wn[j];
        }

        y_salva[i] = y; 

        d_new = 0;

        for(j = 0; j < NWo; j++)
        {
            d_new = d_new + x_linhan[j] * Wo[j];
        }

        // Calculo do erro e(n) = d(n) - y(n)
        ee = d_new - y;
        printf("valor do ee: %d\n", ee);
        e_salva[i] = ee;

        // Escrevendo o erro no arquivo de saida
        fwrite(&ee, sizeof(short), 1, Data_out);

        // Atualizando os coeficientes do filtro usando LMS
        for(j =0; j < N; j++)
        {
            wn[j] = wn[j] + u*ee*x_linhan[j];
        }

        for(j = 0; j < N; j++)
        {
            w_salva[i][N] = wn[j];
        }

        // Atualizando o vetor x_linhan
        for(j = N; j > 1; j--)
        {
            x_linhan[j] = x_linhan[j-1];
        }

    }

    fclose(Data_in);
    fclose(Data_out);

    return 0;
}