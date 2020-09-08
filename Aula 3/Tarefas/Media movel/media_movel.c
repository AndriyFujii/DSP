#include <stdio.h>
#include <stdlib.h>
#define k 4  // tamanho da media

int somaVetor(int *vet)
{
    int soma =0;
    for (int i = 0; i < k; i++)
    {
        soma += vet[i];
    }
    return soma;
}

void deslocaVetor(int *vet)
{
    for (int i = k-1; i > k; i--)
    {
        vet[i] = vet[i-1];
    }
}

int main()
{
    //Abrindo o arquivo como leitura e binario
    FILE *input;
    input = fopen("wn.pcm", "rb");
    if (input == NULL)
    {
        printf("Nao foi possivel encontrar o arquivo\n");
    }
    //Se conseguiu abrir, faz o algoritmo
    else
    {
        //Cria arquivo de saida para salvar durante o calculo
        FILE *output;
        output = fopen("wn_media_movel.pcm", "wb");

        int vetAux[k];
        //Zerando buffer
        for (int i = 0; i < k; i++)
        {
            vetAux[i] = 0;
        }

        short dado = 0;
        while(fread(&dado, 2, 1, input) != 0)
        {
            vetAux[0] = dado;
            short soma = somaVetor(vetAux)/k;
            fwrite(&soma, 2, 1, output);
            deslocaVetor(vetAux);
        }

        fclose(input);
        fclose(output);
    }
    return 0;
}