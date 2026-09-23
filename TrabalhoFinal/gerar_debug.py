import glob
from shape_pipeline import extract_shape_signature
 
# ajuste o caminho abaixo se necessario
PASTA_TREINO = r"data\train"  # ou caminho absoluto, ex.: r"C:\Users\Arthur\Desktop\TrabalhoFinal\data\train"
 
for fp in glob.glob(f"{PASTA_TREINO}\\**\\*.jpeg", recursive=True):
    try:
        extract_shape_signature(fp, debug_plot=True)
        print("ok:", fp)
    except Exception as e:
        print(fp, "ERRO:", e)