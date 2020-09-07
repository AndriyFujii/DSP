#include <stdio.h>
#include <stdlib.h>
#define k 16  // tamanho da media

int main()
{
    //Abrindo o arquivo como leitura e binario
    FILE *file;
    file = fopen("wn.pcm", "rb");
    if (file == NULL)
    {
        printf("Nao foi possivel encontrar o arquivo\n");
    }
    //Se conseguiu abrir, faz o algoritmo
    else
    {
        double coef[k];
        for (int i = 0; i < k; i++)
        {
            coef[i] = 1.0 / k;
        }
        fseek(file, 0, SEEK_END);

        int itera;
        //Tamanho do arquivo
        itera = ftell(file)/sizeof(short);
        rewind(file);
        
        //Aloca a memoria para X e le o vetor do arquivo
        short *x = malloc(itera * sizeof(short));
        fread(x, sizeof(short), itera, file);
        fclose(file);

        double *y = malloc(itera * sizeof(double));
        double *result = malloc(itera * sizeof(double));

        for (int i = 0; i < itera; i++)
        {
            y[0] = x[i];
            double sum = 0;

            for (int n = 0; n < k; n++)
                sum += coef[n] * y[n];

            result[i] = sum;

            for (int n = k; n < 2; n--)
                x[n] = x[n-1];
        }
        //Salvando arquivo de saida
        file = fopen("wn_media_movel.pcm", "wb");
        fwrite(result, sizeof(double), itera, file);

        free(result);
        free(y);
        free(x);
    }
    return 0;
}