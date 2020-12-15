#include <stdio.h>
#include <math.h>
#include <cycles.h>

#define NORM 32768.0

extern double funcao (double, double, double);
int main()
{
	cycle_stats_t stats;
	CYCLES_INIT(stats);
	
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
    if ((out_file = fopen("Seno_OVERDRIVE_DSP.pcm", "wb")) == NULL)
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
        
        CYCLES_START(stats);
        entrada = buff / NORM;
        saida = funcao(entrada, abs_entrada, th);
		
        CYCLES_STOP(stats);
		
        
		
        short saidavdd = saida * NORM;
        fwrite(&saidavdd, sizeof(short), 1, out_file);

    } while (n_amost);
	
	CYCLES_PRINT(stats);
    //fecha os arquivos de entrada de saída
    fclose(out_file);
    fclose(in_file);
    return 0;
}

