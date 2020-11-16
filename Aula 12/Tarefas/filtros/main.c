/* Implementação de um filtro
Lê um arquivo binário com amostras em 16bits
Salva arquivo filtrado também em 16 bits
George
 */
#include <stdio.h>
#include <fcntl.h>
#include <io.h>

#define NSAMPLES 160 // Numero de coeficientes
//#define NSAMPLES 160 
//#define NSAMPLES 320
//#define NSAMPLES 637
//#define NSAMPLES 160

int main() {
  FILE * in_file, * out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[NSAMPLES] = {
    0x0
  };

  float y = 0;

  int coef;
  printf("Entre com o coeficiente a ser utilizado:\n(1)PB\n(2)PA\n(3)PF\n(4)EQ\n(5)FA\n");
  scanf("%d", &coef);

  //Carregando os coeficientes do filtro média móvel
  float coef[NSAMPLES] = {
        //#include "coeficientes_pb.dat"
        //#include "coeficientes_pa.dat"
        //#include "coeficientes_pf.dat"
        //#include "coeficientes_eq.dat"
        #include "coeficientes_fa.dat"
  };

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("wn.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("saida_filtro.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // zera vetor de amostras
  for (i = 0; i < NSAMPLES; i++) {
    sample[i] = 0;
  }

  // execução do filtro
  do {

    //zera saída do filtro
    y = 0;

    //lê dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    //Convolução e acumulação
    for (n = 0; n < NSAMPLES; n++) {
      y += coef[n] * sample[n];
    }

    //desloca amostra
    for (n = NSAMPLES - 1; n > 0; n--) {
      sample[n] = sample[n - 1];
    }

    saida = (short) y;

    //escreve no arquivo de saída
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de saída
  fclose(out_file);
  fclose(in_file);
  return 0;
}