#include <stdio.h>
#include <fcntl.h>
#include <io.h>

#define NSAMPLES 160

int main() {
  FILE * in_file, * out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[NSAMPLES] = {
    0x0
  };

  float y_pb;
  float y_pa;
  float y_pf;
  float y;

  float g_pb = 0.5;
  float g_pf = 0.5;
  float g_pa = 0.5;


  float coef_pb[NSAMPLES] = {
    #include "coeficientes_pb.dat"
  };

  float coef_pa[NSAMPLES] = {
    #include "coeficientes_pa.dat"
  };

  float coef_pf[NSAMPLES] = {
    #include "coeficientes_pf.dat"
  };

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("Sweep10_3600.pcm", "rb")) == NULL) {
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
    y_pa = 0;
    y_pb = 0;
    y_pf = 0;

    //lê dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    //Convolução e acumulação
    for (n = 0; n < NSAMPLES; n++) {
      y_pb += coef_pb[n] * sample[n];
    }

    for (n = 0; n < NSAMPLES; n++) {
      y_pa += coef_pa[n] * sample[n];
    }

    for (n = 0; n < NSAMPLES; n++) {
      y_pf += coef_pf[n] * sample[n];
    }

    
    //desloca amostra
    for (n = NSAMPLES - 1; n > 0; n--) {
      sample[n] = sample[n - 1];
    }

    y = (y_pa*g_pa) + (y_pb*g_pb) + (y_pf*g_pf);

    saida = (short) y;

    //escreve no arquivo de saída
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de saída
  fclose(out_file);
  fclose(in_file);
  return 0;
}