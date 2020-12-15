double funcao (double entrada, double abs_entrada, double th)
{

double saida;
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

	return saida;
}