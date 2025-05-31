import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymcdm import methods, normalizations, weights
from scipy.stats import rankdata
import warnings
import os
from datetime import datetime
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9

def create_output_directory():
    """Tworzy folder do zapisywania wyników lub zwraca istniejący."""
    folder_name = "wykresy_raporty"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Utworzono folder: {folder_name}")
    else:
        print(f"Używam istniejącego folderu: {folder_name}")
    return folder_name

def generate_filename(base_name, extension, output_dir):
    """Generuje unikalną nazwę pliku z timestampem."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_name}_{timestamp}.{extension}"
    return os.path.join(output_dir, filename)

def safe_method_call(method_class, decision_matrix, weights_values, criteria_types, method_name):
    """Bezpieczne wywołanie metody MCDM z obsługą błędów."""
    try:
        if method_name == 'SPOTIS':
            bounds = np.array([[np.min(decision_matrix[:, j]), np.max(decision_matrix[:, j])] 
                              for j in range(decision_matrix.shape[1])], dtype=float)
            method_instance = method_class(bounds)
        else:
            method_instance = method_class()
        scores = method_instance(decision_matrix, weights_values, criteria_types)
        return scores
    except Exception as e:
        print(f"Błąd w metodzie {method_name}: {e}")
        return None

def calculate_entropy_weights(decision_matrix):
    """Oblicz wagi entropijne."""
    try:
        if hasattr(weights, 'entropy_weighting'):
            return weights.entropy_weighting(decision_matrix)
        elif hasattr(weights, 'entropy'):
            return weights.entropy(decision_matrix)
        else:
            return manual_entropy_weights(decision_matrix)
    except Exception:
        return manual_entropy_weights(decision_matrix)

def manual_entropy_weights(decision_matrix):
    """Ręczna implementacja metody entropijnej."""
    try:
        m, n = decision_matrix.shape
        normalized = decision_matrix / np.sum(decision_matrix, axis=0)
        entropy_values = np.zeros(n)
        k = 1 / np.log(m)
        
        for j in range(n):
            column = normalized[:, j]
            column = np.where(column <= 0, 1e-10, column)
            entropy_values[j] = -k * np.sum(column * np.log(column))
        
        diversity = 1 - entropy_values
        weights_entropy = diversity / np.sum(diversity)
        return weights_entropy
    except Exception:
        return np.ones(decision_matrix.shape[1]) / decision_matrix.shape[1]

def normalize_scores_for_comparison(scores, method_name):
    """Normalizacja wyników dla porównania między metodami."""
    if scores is None:
        return None
    if method_name == 'TOPSIS':
        return scores
    else:
        max_score = np.max(scores)
        return max_score - scores

def main():
    """Główna funkcja analizy MCDM."""
    print("=== Analiza wielokryterialnego podejmowania decyzji ===")
    
    output_dir = create_output_directory()
    
    print("\nProblem: Wybór najlepszego samochodu")
    print("-" * 50)
    
    decision_matrix = np.array([
        [25000, 6.5, 8.5, 7.0, 8.0],  # Toyota Corolla
        [35000, 8.0, 9.0, 8.5, 7.5],  # BMW 3 Series
        [22000, 5.5, 7.5, 6.5, 9.0],  # Honda Civic
        [28000, 7.0, 8.0, 8.0, 8.5],  # Volkswagen Golf
        [32000, 6.0, 9.5, 9.0, 8.0]   # Audi A4
    ], dtype=float)
    
    alternatives = ['Toyota Corolla', 'BMW 3 Series', 'Honda Civic', 
                   'Volkswagen Golf', 'Audi A4']
    criteria = ['Cena', 'Spalanie', 'Bezpieczeństwo', 'Komfort', 'Niezawodność']
    criteria_types = np.array([-1, -1, 1, 1, 1])
    weights_values = np.array([0.3, 0.2, 0.25, 0.15, 0.1])
    weights_values = weights_values / np.sum(weights_values)
    
    print("Macierz decyzyjna:")
    df_matrix = pd.DataFrame(decision_matrix, index=alternatives, columns=criteria)
    print(df_matrix)
    print(f"\nWagi kryteriów: {dict(zip(criteria, weights_values))}")
    print(f"Typy kryteriów: {dict(zip(criteria, ['min' if x == -1 else 'max' for x in criteria_types]))}")
    
    results = {}
    
    print("\n" + "="*50)
    print("1. METODA TOPSIS")
    print("="*50)
    
    topsis_scores = safe_method_call(methods.TOPSIS, decision_matrix, weights_values, criteria_types, 'TOPSIS')
    
    if topsis_scores is not None:
        topsis_ranking = rankdata(-topsis_scores)
        best_topsis_idx = np.argmax(topsis_scores)
        
        results['TOPSIS'] = {
            'scores': topsis_scores,
            'ranking': topsis_ranking,
            'best': alternatives[best_topsis_idx],
            'best_idx': best_topsis_idx
        }
        
        print("Wyniki TOPSIS:")
        topsis_results = pd.DataFrame({
            'Alternatywa': alternatives,
            'Score': topsis_scores,
            'Ranking': topsis_ranking.astype(int)
        }).sort_values('Ranking')
        print(topsis_results.to_string(index=False))
    
    print("\n" + "="*50)
    print("2. METODA SPOTIS")
    print("="*50)
    
    spotis_scores = safe_method_call(methods.SPOTIS, decision_matrix, weights_values, criteria_types, 'SPOTIS')
    
    if spotis_scores is not None:
        spotis_ranking = rankdata(spotis_scores)
        best_spotis_idx = np.argmin(spotis_scores)
        
        results['SPOTIS'] = {
            'scores': spotis_scores,
            'ranking': spotis_ranking,
            'best': alternatives[best_spotis_idx],
            'best_idx': best_spotis_idx
        }
        
        print("Wyniki SPOTIS:")
        spotis_results = pd.DataFrame({
            'Alternatywa': alternatives,
            'Score': spotis_scores,
            'Ranking': spotis_ranking.astype(int)
        }).sort_values('Ranking')
        print(spotis_results.to_string(index=False))
    
    print("\n" + "="*50)
    print("3. METODA VIKOR")
    print("="*50)
    
    vikor_scores = safe_method_call(methods.VIKOR, decision_matrix, weights_values, criteria_types, 'VIKOR')
    
    if vikor_scores is not None:
        vikor_ranking = rankdata(vikor_scores)
        best_vikor_idx = np.argmin(vikor_scores)
        
        results['VIKOR'] = {
            'scores': vikor_scores,
            'ranking': vikor_ranking,
            'best': alternatives[best_vikor_idx],
            'best_idx': best_vikor_idx
        }
        
        print("Wyniki VIKOR:")
        vikor_results = pd.DataFrame({
            'Alternatywa': alternatives,
            'Score': vikor_scores,
            'Ranking': vikor_ranking.astype(int)
        }).sort_values('Ranking')
        print(vikor_results.to_string(index=False))
    
    print("\n" + "="*50)
    print("4. PORÓWNANIE WYNIKÓW")
    print("="*50)
    
    comparison_data = {'Alternatywa': alternatives}
    
    for method_name, method_results in results.items():
        if method_results is not None:
            comparison_data[f'{method_name}_Score'] = method_results['scores']
            comparison_data[f'{method_name}_Rank'] = method_results['ranking'].astype(int)
    
    if comparison_data:
        comparison_df = pd.DataFrame(comparison_data)
        print("Porównanie wszystkich metod:")
        print(comparison_df.to_string(index=False))
    
    print("\n" + "="*50)
    print("5. WAGI METODĄ ENTROPII")
    print("="*50)
    
    entropy_weights = calculate_entropy_weights(decision_matrix)
    entropy_results = {}
    
    if entropy_weights is not None:
        print(f"Wagi eksperckie:  {weights_values}")
        print(f"Wagi entropijne:  {entropy_weights}")
        
        print("\nPorównanie najlepszych alternatyw z wagami entropijnymi:")
        
        for method_name in results.keys():
            if method_name == 'TOPSIS':
                entropy_scores = safe_method_call(methods.TOPSIS, decision_matrix, entropy_weights, criteria_types, 'TOPSIS')
                if entropy_scores is not None:
                    best_entropy_idx = np.argmax(entropy_scores)
                    entropy_results[method_name] = {
                        'scores': entropy_scores,
                        'ranking': rankdata(-entropy_scores),
                        'best': alternatives[best_entropy_idx]
                    }
                    print(f"TOPSIS (entropia): {alternatives[best_entropy_idx]}")
            
            elif method_name == 'SPOTIS':
                entropy_scores = safe_method_call(methods.SPOTIS, decision_matrix, entropy_weights, criteria_types, 'SPOTIS')
                if entropy_scores is not None:
                    best_entropy_idx = np.argmin(entropy_scores)
                    entropy_results[method_name] = {
                        'scores': entropy_scores,
                        'ranking': rankdata(entropy_scores),
                        'best': alternatives[best_entropy_idx]
                    }
                    print(f"SPOTIS (entropia): {alternatives[best_entropy_idx]}")
            
            elif method_name == 'VIKOR':
                entropy_scores = safe_method_call(methods.VIKOR, decision_matrix, entropy_weights, criteria_types, 'VIKOR')
                if entropy_scores is not None:
                    best_entropy_idx = np.argmin(entropy_scores)
                    entropy_results[method_name] = {
                        'scores': entropy_scores,
                        'ranking': rankdata(entropy_scores),
                        'best': alternatives[best_entropy_idx]
                    }
                    print(f"VIKOR (entropia): {alternatives[best_entropy_idx]}")
    
    print("\n" + "="*50)
    print("6. TESTOWANIE NORMALIZACJI")
    print("="*50)
    
    normalization_methods = [
        ('minmax', normalizations.minmax_normalization),
        ('vector', normalizations.vector_normalization),
        ('sum', normalizations.sum_normalization)
    ]
    
    normalized_data = {}
    for norm_name, norm_func in normalization_methods:
        try:
            print(f"\nNormalizacja: {norm_name}")
            normalized = norm_func(decision_matrix)
            normalized_data[norm_name] = normalized
            print(f"Przykład znormalizowanych danych (pierwsza alternatywa): {normalized[0]}")
        except Exception as e:
            print(f"Błąd normalizacji {norm_name}: {e}")
    
    print("\n" + "="*50)
    print("7. WIZUALIZACJA")
    print("="*50)
    
    if results:
        try:
            fig, axes = plt.subplots(2, 3, figsize=(18, 12))
            fig.suptitle('Analiza wielokryterialnego podejmowania decyzji', fontsize=16, fontweight='bold')
            
            ax1 = axes[0, 0]
            im1 = ax1.imshow(decision_matrix, cmap='viridis', aspect='auto')
            ax1.set_title('Macierz decyzyjna')
            ax1.set_xlabel('Kryteria')
            ax1.set_ylabel('Alternatywy')
            ax1.set_xticks(range(len(criteria)))
            ax1.set_xticklabels(criteria, rotation=45, ha='right')
            ax1.set_yticks(range(len(alternatives)))
            ax1.set_yticklabels([alt.replace(' ', '\n') for alt in alternatives])
            plt.colorbar(im1, ax=ax1, shrink=0.8)
            
            ax2 = axes[0, 1]
            x = np.arange(len(alternatives))
            width = 0.25
            colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
            
            i = 0
            legend_labels = []
            for method_name, method_results in results.items():
                if i < 3:
                    normalized_scores = normalize_scores_for_comparison(method_results['scores'], method_name)
                    if normalized_scores is not None:
                        ax2.bar(x + i * width, normalized_scores, width, 
                               label=method_name, alpha=0.8, color=colors[i])
                        legend_labels.append(method_name)
                    i += 1
            
            ax2.set_xlabel('Alternatywy')
            ax2.set_ylabel('Znormalizowane wyniki')
            ax2.set_title('Porównanie wyników metod')
            ax2.set_xticks(x + width)
            ax2.set_xticklabels([alt.split()[0] for alt in alternatives], rotation=45)
            if legend_labels:
                ax2.legend()
            ax2.grid(True, alpha=0.3)
            
            ax3 = axes[0, 2]
            i = 0
            for method_name, method_results in results.items():
                if i < 3:
                    ranking = method_results['ranking']
                    ax3.bar(x + i * width, ranking, width, 
                           label=method_name, alpha=0.8, color=colors[i])
                    i += 1
            
            ax3.set_xlabel('Alternatywy')
            ax3.set_ylabel('Pozycja w rankingu')
            ax3.set_title('Porównanie rankingów')
            ax3.set_xticks(x + width)
            ax3.set_xticklabels([alt.split()[0] for alt in alternatives], rotation=45)
            if legend_labels:
                ax3.legend()
            ax3.grid(True, alpha=0.3)
            ax3.invert_yaxis()
            
            ax4 = axes[1, 0]
            wedges, texts, autotexts = ax4.pie(weights_values, labels=criteria, autopct='%1.1f%%', 
                                              startangle=90)
            ax4.set_title('Rozkład wag kryteriów')
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
            
            ax5 = axes[1, 1]
            data_for_boxplot = []
            labels_for_boxplot = []
            
            for j, criterion in enumerate(criteria):
                values = decision_matrix[:, j]
                if criteria_types[j] == -1:
                    normalized_values = (np.max(values) - values) / (np.max(values) - np.min(values))
                else:
                    normalized_values = (values - np.min(values)) / (np.max(values) - np.min(values))
                
                data_for_boxplot.append(normalized_values)
                labels_for_boxplot.append(criterion)
            
            bp = ax5.boxplot(data_for_boxplot, labels=labels_for_boxplot, patch_artist=True)
            colors_box = plt.cm.Set2.colors
            for patch, color in zip(bp['boxes'], colors_box):
                patch.set_facecolor(color)
            ax5.set_title('Rozkład znormalizowanych wartości')
            ax5.set_ylabel('Wartość znormalizowana')
            ax5.tick_params(axis='x', rotation=45)
            ax5.grid(True, alpha=0.3)
            
            ax6 = axes[1, 2]
            x_pos = np.arange(len(criteria))
            width = 0.35
            
            ax6.bar(x_pos - width/2, weights_values, width, label='Wagi eksperckie', alpha=0.8)
            
            if entropy_weights is not None:
                ax6.bar(x_pos + width/2, entropy_weights, width, label='Wagi entropijne', alpha=0.8)
            
            ax6.set_xlabel('Kryteria')
            ax6.set_ylabel('Waga')
            ax6.set_title('Porównanie metod wyznaczania wag')
            ax6.set_xticks(x_pos)
            ax6.set_xticklabels(criteria, rotation=45)
            ax6.legend()
            ax6.grid(True, alpha=0.3)
            
            plt.tight_layout()
            
            plot_filename = generate_filename('mcdm_analysis', 'png', output_dir)
            plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
            plt.show()
            
            print(f"Wykresy zapisane: {plot_filename}")
            
        except Exception as e:
            print(f"Błąd wizualizacji: {e}")
    
    print("\n" + "="*50)
    print("8. GENEROWANIE RAPORTU")
    print("="*50)
    
    report_lines = [
        "# Raport z analizy wielokryterialnego podejmowania decyzji",
        "",
        "## Problem",
        "Wybór najlepszego samochodu spośród 5 opcji na podstawie 5 kryteriów.",
        "",
        "## Alternatywy",
        *[f"- {alt}" for alt in alternatives],
        "",
        "## Kryteria i wagi",
        *[f"- {crit}: {weight:.3f} ({'min' if ct == -1 else 'max'})" 
          for crit, weight, ct in zip(criteria, weights_values, criteria_types)],
        "",
        "## Wyniki analizy"
    ]
    
    for method_name, method_results in results.items():
        best_alt = method_results['best']
        report_lines.extend([
            f"",
            f"### {method_name} - najlepsza alternatywa: {best_alt}"
        ])
    
    if len(results) > 1:
        all_winners = [res['best'] for res in results.values()]
        from collections import Counter
        winner_counts = Counter(all_winners)
        most_common_winner, most_common_count = winner_counts.most_common(1)[0]
        
        report_lines.extend([
            "",
            "## Analiza zgodności",
            f"Najczęściej wybierana alternatywa: **{most_common_winner}** ({most_common_count}/{len(results)} metod)",
            "",
            "### Wyniki poszczególnych metod:",
            *[f"- {method}: {winner}" for method, winner in zip(results.keys(), all_winners)]
        ])
    
    if entropy_weights is not None:
        report_lines.extend([
            "",
            "## Wagi entropijne",
            "Porównanie wag eksperkich z wagami entropijnymi:",
            *[f"- {crit}: ekspercka={exp:.3f}, entropijna={ent:.3f}" 
              for crit, exp, ent in zip(criteria, weights_values, entropy_weights)]
        ])
        
        if entropy_results:
            report_lines.extend([
                "",
                "### Wyniki z wagami entropijnymi:",
                *[f"- {method}: {res['best']}" for method, res in entropy_results.items()]
            ])
    
    report_lines.extend([
        "",
        "## Wnioski",
        "1. Analiza wielokryterialna została przeprowadzona pomyślnie",
        "2. Porównano różne metody MCDM i ich zgodność",
        "3. Zbadano wpływ różnych metod wyznaczania wag",
        "",
        f"Data analizy: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}"
    ])
    
    report_content = "\n".join(report_lines)
    
    try:
        report_filename = generate_filename('raport_mcdm', 'md', output_dir)
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
        print(f"Raport zapisany: {report_filename}")
    except Exception as e:
        print(f"Błąd zapisu raportu: {e}")
    
    print("\n" + "="*50)
    print("PODSUMOWANIE")
    print("="*50)
    
    print("Zastosowane metody MCDM:")
    for method_name, method_results in results.items():
        best_alt = method_results['best']
        print(f"- {method_name}: {best_alt}")
    
    if len(results) > 1:
        all_winners = [res['best'] for res in results.values()]
        if len(set(all_winners)) == 1:
            print(f"\nWszystkie metody wskazują: {all_winners[0]}")
        else:
            print(f"\nMetody wskazują różne alternatywy:")
            from collections import Counter
            winner_counts = Counter(all_winners)
            for winner, count in winner_counts.most_common():
                print(f"  - {winner}: {count} głos(ów)")
    
    print("\nAnaliza zakończona pomyślnie!")
    
    try:
        files_in_output = os.listdir(output_dir)
        current_files = sorted([f for f in files_in_output if f.endswith(('.png', '.md'))])[-2:]
        print("Wygenerowane pliki:")
        for file in current_files:
            print(f"- {file}")
    except Exception:
        pass

if __name__ == "__main__":
    required_packages = ['pymcdm', 'numpy', 'pandas', 'matplotlib', 'scipy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Błąd: Brakuje bibliotek: {', '.join(missing_packages)}")
        print(f"Zainstaluj: pip install {' '.join(missing_packages)}")
    else:
        main()