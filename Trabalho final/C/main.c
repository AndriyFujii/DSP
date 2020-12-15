#include <stdio.h>
#include <fcntl.h>
#include <io.h>
#include <math.h>

#define NORM 32768.0

int main()
{
    FILE *in_file, *out_file;
    int i, n, n_amost;

    short buff;
    //double entrada, saida;
    double entrada, saida;

    double th = 1.0 / 3.0;

    /* abre os arquivos de entrada e saida */
    if ((in_file = fopen("Seno.pcm", "rb")) == NULL)
    {
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        system("pause");
        return 0;
    }
    if ((out_file = fopen("Seno_OVERDRIVE.pcm", "wb")) == NULL)
    {
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }

    double abs_entrada;

    // execução do filtro
    do
    {
        //lê dado do arquivo
        n_amost = fread(&buff, sizeof(short), 1, in_file);
        //
        entrada = buff / NORM;
        // abs
        if (entrada < 0)
            abs_entrada = -1 * entrada;
        else
            abs_entrada = entrada;

        // overdrive
        // 0 <= x < 1/3
        // f(x) = 2x
        if (abs_entrada < th)
            saida = 2 * entrada;
        // 2/3 < x <= 1
        // f(x) = 1
        else if (abs_entrada > 2 * th)
        {
            if (entrada > 0)
                saida = 0.99;
            else
                saida = -0.99;
        }
        // 1/3 <= x <= 2/3
        // f(x) = (3-(2-3x)^2)/3
        else
        {
            if (entrada > 0)
            {
                saida = (2 - 3 * entrada) * (2 - 3 * entrada);
                saida = 3 - saida;
                saida = saida / 3;
            }
            else
            {
                saida = (2 - 3 * (-1 * entrada)) * (2 - 3 * (-1 * entrada));
                saida = 3 - saida;
                saida = -saida / 3;
            }
        }
        short saidavdd = saida * NORM;
        fwrite(&saidavdd, sizeof(short), 1, out_file);

    } while (n_amost);

    //fecha os arquivos de entrada de saída
    fclose(out_file);
    fclose(in_file);
    return 0;
}