#include <stdio.h>
#include <math.h>
#include <cycles.h>

#define NORM 32768.0

extern short funcao (short, short, short);

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
        
        CYCLES_START(stats);
        entrada = buff;
        saida = funcao(entrada, abs_entrada, th);
        
		CYCLES_STOP(stats);
		
        fwrite(&saida, sizeof(short), 1, out_file);

    } while (n_amost);
	
	CYCLES_PRINT(stats);
    //fecha os arquivos de entrada de saída
    fclose(out_file);
    fclose(in_file);
    return 0;
}