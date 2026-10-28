import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

# Carregar o CSV
csv_file_path = '/home/laiane/Documentos/histo/clsc-levels-learning-all.csv'
df = pd.read_csv(csv_file_path)

# Renomear as colunas
df.columns = ['Video', 'QP', 'Config', 'CTU_Window', 'Coalescence_Level']

# Agrupar os dados por vídeo, QP e configuração (RA/LD)
grouped_data = df.groupby(['Video', 'QP', 'Config'])['Coalescence_Level'].apply(list).reset_index()

# Função para gerar os histogramas para cada vídeo e configuração
def gerar_histogramas_por_video(video, config, pdf_pages):
    # Filtrar os dados para o vídeo e configuração especificados
    data_filtrada = grouped_data[(grouped_data['Video'] == video) & (grouped_data['Config'] == config)]
    
    # Preparar os dados para cada QP (22, 27, 32, 37)
    coalescence_qp22 = data_filtrada[data_filtrada['QP'] == 22]['Coalescence_Level'].values[0]
    coalescence_qp27 = data_filtrada[data_filtrada['QP'] == 27]['Coalescence_Level'].values[0]
    coalescence_qp32 = data_filtrada[data_filtrada['QP'] == 32]['Coalescence_Level'].values[0]
    coalescence_qp37 = data_filtrada[data_filtrada['QP'] == 37]['Coalescence_Level'].values[0]
    
    # Criar o histograma
    plt.figure(figsize=(10, 6))
    plt.hist(coalescence_qp22, bins=50, alpha=0.5, label='QP 22', color='blue')
    plt.hist(coalescence_qp27, bins=50, alpha=0.5, label='QP 27', color='green')
    plt.hist(coalescence_qp32, bins=50, alpha=0.5, label='QP 32', color='red')
    plt.hist(coalescence_qp37, bins=50, alpha=0.5, label='QP 37', color='purple')
    
    # Adicionar títulos e legendas
    plt.xlabel("Coalescence Level", size=14)
    plt.ylabel("Occurrences", size=14)
    plt.title(f"Coalescence Levels Histogram - {video} ({config})", size=16)
    plt.legend(loc='upper right')
    
    # Adicionar o gráfico ao PDF
    pdf_pages.savefig()
    plt.close()

# Lista de vídeos e configurações
videos = df['Video'].unique()
configuracoes = ['RA', 'LD']

# Caminho para salvar o PDF
pdf_output_path = '/home/laiane/Documentos/histo/coalescence_histograms.pdf'

# Gerar e salvar os gráficos no PDF
with PdfPages(pdf_output_path) as pdf_pages:
    for video in videos:
        for config in configuracoes:
            gerar_histogramas_por_video(video, config, pdf_pages)

print(f"Histograms saved in {pdf_output_path}")
