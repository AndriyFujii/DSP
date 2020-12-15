#include <stdio.h>
#include <math.h>
#include <cycles.h>

#define NORM 32768.0

int main()
{
	cycle_stats_t stats;
	CYCLES_INIT(stats);
	
    FILE *in_file, *out_file;
    int i, n, n_amost;

    short buff;
    //double entrada, saida;
    short entrada, saida;

    short th = NORM / 3;

    /* abre os arquivos de entrada e saida */
    if ((in_file = fopen("gtr-jazz-3.pcm", "rb")) == NULL)
    {
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        system("pause");
        return 0;
    }
    if ((out_file = fopen("gtr-jazz-3_OVERDRIVE.pcm", "wb")) == NULL)
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
        entrada = buff;
        
        // abs
        if (entrada < 0)
            abs_entrada = -1 * entrada;
        else
            abs_entrada = entrada;
		
		CYCLES_START(stats);	
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
                saida = (2/NORM - 3/NORM * entrada) * (2/NORM - 3/NORM * entrada);
                saida = 3/NORM - saida;
                saida = saida / 3/NORM;
            }
            else
            {
                saida = (2/NORM - 3/NORM * (-1 * entrada)) * (2/NORM - 3/NORM * (-1 * entrada));
                saida = 3/NORM - saida;
                saida = -saida / 3/NORM;
            }
        }
		CYCLES_STOP(stats);
		
        fwrite(&saida, sizeof(short), 1, out_file);

    } while (n_amost);
	
	CYCLES_PRINT(stats);
    //fecha os arquivos de entrada de saída
    fclose(out_file);
    fclose(in_file);
    return 0;
}