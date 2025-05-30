import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_performance_vs_Q(input_dir):
    result_file = os.path.join(input_dir, "risultati_finali.txt")
    
    if not os.path.exists(result_file):
        print(f"File non trovato: {result_file}")
        sys.exit(1)
    
    # Carica il file con conversione robusta
    df = pd.read_csv(result_file)
   
    

    # Converte i campi numerici
    df["mean"] = pd.to_numeric(df["mean"], errors='coerce')
    df["variance"] = pd.to_numeric(df["variance"], errors='coerce')
    df["Q"] = pd.to_numeric(df["Q"], errors='coerce')
    df["std"] = df["variance"]

    # Lista dei metodi da estrarre
    methods = [
        "Sample_", "Rie____", "IW_____", "Clipped", "Kendall", "TMFG___",
        "Sample__SI", "Rie_____SI", "IW______SI", "Clipped_SI",
        "Kendall_SI", "TMFG____SI", "Sample__SD", "Rie_____SD",
        "IW______SD", "Clipped_SD", "Kendall_SD", "TMFG____SD"
    ]

    # Dizionari per salvare gli array
    Q_dict = {}
    mean_dict = {}
    std_dict = {}

    for method in methods:
        df_method = df[df["method"] == method].sort_values("Q")
        Q_dict[method] = df_method["Q"].values
        mean_dict[method] = df_method["mean"].values
        std_dict[method] = df_method["std"].values

    #print(Q_dict["Sample_"])
    #print(mean_dict["Sample_"])
    #print(mean_dict["Rie____"])

   
    for A in range(1, 6):

        if A==1:
            plt.plot(Q_dict["Sample_"], mean_dict["Sample_"], label="Sample_")
            plt.plot(Q_dict["Sample_"], mean_dict["Rie____"], label="Rie____")
            plt.plot(Q_dict["Sample_"], mean_dict["IW_____"], label="IW_____")
            plt.fill_between(Q_dict["Sample_"], mean_dict["Sample_"] - std_dict["Sample_"], mean_dict["Sample_"] + std_dict["Sample_"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["Rie____"] - std_dict["Rie____"], mean_dict["Rie____"] + std_dict["Rie____"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["IW_____"] - std_dict["IW_____"], mean_dict["IW_____"] + std_dict["IW_____"], alpha=0.2)
            plt.yscale('log')

            plt.xlabel("Q")
            plt.ylabel("Mean Variance")
            plt.legend()
            output_path = os.path.join(input_dir, f"performance_vs_Q_A_{A}.png")
            plt.savefig(output_path)
            print(f"Grafico salvato in: {output_path}")
            plt.close()

        elif A==2:
            plt.plot(Q_dict["Sample_"], mean_dict["Sample_"], label="Sample_")
            plt.plot(Q_dict["Sample_"], mean_dict["Rie____"], label="Rie____")
            plt.plot(Q_dict["Sample_"], mean_dict["IW_____"], label="IW_____")
            plt.fill_between(Q_dict["Sample_"], mean_dict["Sample_"] - std_dict["Sample_"], mean_dict["Sample_"] + std_dict["Sample_"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["Rie____"] - std_dict["Rie____"], mean_dict["Rie____"] + std_dict["Rie____"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["IW_____"] - std_dict["IW_____"], mean_dict["IW_____"] + std_dict["IW_____"], alpha=0.2)
            plt.yscale('log')
            plt.xlim(0.7, 1.2)

            plt.xlabel("Q")
            plt.ylabel("Mean Variance")
            plt.legend()
            output_path = os.path.join(input_dir, f"performance_vs_Q_A_{A}.png")
            plt.savefig(output_path)
            print(f"Grafico salvato in: {output_path}")
            plt.close()

        elif A==3:
            plt.plot(Q_dict["Sample_"], mean_dict["Clipped"], label="Clipped")
            plt.plot(Q_dict["Sample_"], mean_dict["Kendall"], label="Kendall")
            plt.plot(Q_dict["Sample_"], mean_dict["TMFG___"], label="TMFG___")
            plt.fill_between(Q_dict["Sample_"], mean_dict["Clipped"] - std_dict["Clipped"], mean_dict["Clipped"] + std_dict["Clipped"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["Kendall"] - std_dict["Kendall"], mean_dict["Kendall"] + std_dict["Kendall"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["TMFG___"] - std_dict["TMFG___"], mean_dict["TMFG___"] + std_dict["TMFG___"], alpha=0.2)
            plt.yscale('log')

            plt.xlabel("Q")
            plt.ylabel("Mean Variance")
            plt.legend()
            output_path = os.path.join(input_dir, f"performance_vs_Q_A_{A}.png")
            plt.savefig(output_path)
            print(f"Grafico salvato in: {output_path}")
            plt.close()

        elif A==4:
            plt.plot(Q_dict["Sample_"], mean_dict["Sample__SI"], label="Sample__SI")
            plt.plot(Q_dict["Sample_"], mean_dict["Rie_____SI"], label="Rie_____SI")
            plt.plot(Q_dict["Sample_"], mean_dict["IW______SI"], label="IW______SI")
            plt.plot(Q_dict["Sample_"], mean_dict["Clipped_SI"], label="Clipped_SI")
            plt.plot(Q_dict["Sample_"], mean_dict["Kendall_SI"], label="Kendall_SI")
            plt.plot(Q_dict["Sample_"], mean_dict["TMFG____SI"], label="TMFG____SI")
            plt.fill_between(Q_dict["Sample_"], mean_dict["Sample__SI"] - std_dict["Sample__SI"], mean_dict["Sample__SI"] + std_dict["Sample__SI"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["Rie_____SI"] - std_dict["Rie_____SI"], mean_dict["Rie_____SI"] + std_dict["Rie_____SI"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["IW______SI"] - std_dict["IW______SI"], mean_dict["IW______SI"] + std_dict["IW______SI"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["Clipped_SI"] - std_dict["Clipped_SI"], mean_dict["Clipped_SI"] + std_dict["Clipped_SI"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["Kendall_SI"] - std_dict["Kendall_SI"], mean_dict["Kendall_SI"] + std_dict["Kendall_SI"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["TMFG____SI"] - std_dict["TMFG____SI"], mean_dict["TMFG____SI"] + std_dict["TMFG____SI"], alpha=0.2)
            plt.yscale('log')

            plt.xlabel("Q")
            plt.ylabel("Mean Variance")
            plt.legend()
            output_path = os.path.join(input_dir, f"performance_vs_Q_A_{A}.png")
            plt.savefig(output_path)
            print(f"Grafico salvato in: {output_path}")
            plt.close()

        elif A==5:
            plt.plot(Q_dict["Sample_"], mean_dict["Sample__SD"], label="Sample__SD")
            plt.plot(Q_dict["Sample_"], mean_dict["Rie_____SD"], label="Rie_____SD")
            plt.plot(Q_dict["Sample_"], mean_dict["IW______SD"], label="IW______SD")
            plt.plot(Q_dict["Sample_"], mean_dict["Clipped_SD"], label="Clipped_SD")
            plt.plot(Q_dict["Sample_"], mean_dict["Kendall_SD"], label="Kendall_SD")
            plt.plot(Q_dict["Sample_"], mean_dict["TMFG____SD"], label="TMFG____SD")
            plt.fill_between(Q_dict["Sample_"], mean_dict["Sample__SD"] - std_dict["Sample__SD"], mean_dict["Sample__SD"] + std_dict["Sample__SD"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["Rie_____SD"] - std_dict["Rie_____SD"], mean_dict["Rie_____SD"] + std_dict["Rie_____SD"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["IW______SD"] - std_dict["IW______SD"], mean_dict["IW______SD"] + std_dict["IW______SD"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["Clipped_SD"] - std_dict["Clipped_SD"], mean_dict["Clipped_SD"] + std_dict["Clipped_SD"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["Kendall_SD"] - std_dict["Kendall_SD"], mean_dict["Kendall_SD"] + std_dict["Kendall_SD"], alpha=0.2)
            plt.fill_between(Q_dict["Sample_"], mean_dict["TMFG____SD"] - std_dict["TMFG____SD"], mean_dict["TMFG____SD"] + std_dict["TMFG____SD"], alpha=0.2)
            plt.yscale('log')

            plt.xlabel("Q")
            plt.ylabel("Mean Variance")
            plt.legend()
            output_path = os.path.join(input_dir, f"performance_vs_Q_A_{A}.png")
            plt.savefig(output_path)
            print(f"Grafico salvato in: {output_path}")
            plt.close()
    
    
   
        
    
    

# Entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python plot_performance_vs_Q.py <directory_input>")
        sys.exit(1)
    
    input_directory = sys.argv[1]
    plot_performance_vs_Q(input_directory)