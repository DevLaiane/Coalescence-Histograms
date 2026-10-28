# Geração de Histogramas de Coalescence Levels

Este script em Python foi desenvolvido para gerar os gráficos (histogramas). O objetivo é visualizar a distribuição dos níveis de coalescência (Coalescence Levels) em janelas CTU para diferentes vídeos, configurações e QPs.

## Sobre o Projeto

O script processa um arquivo `.csv` contendo os resultados de 56 experimentos (7 vídeos, 2 configurações e 4 QPs). Para cada combinação de vídeo e configuração (RA ou LD), é gerado um gráfico sobrepondo os dados dos quatro QPs (22, 27, 32 e 37) em um único histograma.

## Estrutura dos Dados

O script espera um arquivo `.csv` de entrada com as seguintes colunas (nesta ordem):
1.  `Video`: Nome do vídeo.
2.  `QP`: Parâmetro de Quantização (22, 27, 32, 37).
3.  `Config`: Configuração de codificação (RA, LD).
4.  `CTU_Window`: Tamanho da janela CTU.
5.  `Coalescence_Level`: Nível de coalescência registrado.

## Funcionalidades e Arquitetura

O código foi estruturado utilizando **Decorators** em Python para separar as responsabilidades e manter a função de plotagem limpa:

*   **`@checar_qps`**: Valida se o vídeo e a configuração atual possuem dados para todos os 4 QPs necessários (22, 27, 32, 37). Se faltar algum QP, o gráfico daquela combinação é ignorado e um aviso é exibido no console.
*   **`@salvar_no_pdf`**: Gerencia a criação da figura, a chamada da função de desenho e o salvamento automático no arquivo PDF final, garantindo que a memória seja liberada corretamente.
*   **`gerar_histogramas_por_video`**: Função principal que filtra os dados e utiliza a função `plt.hist` do Matplotlib para criar as barras sobrepostas com transparência (`alpha=0.5`) para cada QP.

## Requisitos

Certifique-se de ter as bibliotecas necessárias instaladas:

```bash
pip install pandas matplotlib
