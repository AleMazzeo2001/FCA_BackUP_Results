import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_performance_vs_Q(input_dir):
    sns.set(style="whitegrid", font_scale=1.1)
    result_file = os.path.join(input_dir, "risultati_finali.txt")

    if not os.path.exists(result_file):
        print(f"File non trovato: {result_file}")
        sys.exit(1)

    df = pd.read_csv(result_file)

    # Conversioni sicure
    df["mean"] = pd.to_numeric(df["mean"], errors='coerce')
    df["variance"] = pd.to_numeric(df["variance"], errors='coerce')
    df["Q"] = pd.to_numeric(df["Q"], errors='coerce')
    df["std"] = df["variance"]

    # Tutti i metodi da includere
    method_groups = {
        1: ["Sample_", "Rie____", "IW_____"],
        2: ["Sample_", "Rie____", "IW_____"],
        3: ["Clipped", "Kendall", "TMFG___"],
        4: ["Sample__SI", "Rie_____SI", "IW______SI", "Clipped_SI", "Kendall_SI", "TMFG____SI"],
        5: ["Sample__SD", "Rie_____SD", "IW______SD", "Clipped_SD", "Kendall_SD", "TMFG____SD"]
    }

    # Palette fissa e coerente
    unique_methods = sorted(set(m for group in method_groups.values() for m in group))
    palette = sns.color_palette("tab10", n_colors=len(unique_methods))
    color_map = {method: palette[i] for i, method in enumerate(unique_methods)}

    for A in range(1, 6):
        plt.figure(figsize=(10, 6))
        methods = method_groups[A]

        for method in methods:
            df_method = df[df["method"] == method].sort_values("Q")
            if df_method.empty:
                continue

            Q = df_method["Q"].values
            mean = df_method["mean"].values
            std = df_method["std"].values

            label_clean = method.replace("_", "").replace("SI", " SI").replace("SD", " SD")
            plt.plot(Q, mean, label=label_clean, color=color_map[method])
            plt.fill_between(Q, mean - std, mean + std, alpha=0.2, color=color_map[method])

        if A in [1, 2, 4, 5]:
            plt.yscale("log")
        if A == 2:
            plt.xlim(0.7, 1.2)

        plt.xlabel("q", fontsize=13)
        plt.ylabel("Mean Variance", fontsize=13)
        plt.title(f"Performance vs q (A = {A})", fontsize=14)
        plt.legend()
        plt.tight_layout()

        output_path = os.path.join(input_dir, f"performance_vs_Q_A_{A}.pdf")
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