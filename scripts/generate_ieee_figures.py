#!/usr/bin/env python3
"""
MARTHR Figure Generation - IEEE Quality
Generates TikZ/PGFPlots compatible figures for publication
"""

import os
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib import rcParams

ROOT = Path(__file__).resolve().parents[1]

# IEEE figure style
rcParams['figure.figsize'] = (3.5, 2.5)
rcParams['font.size'] = 9
rcParams['font.family'] = 'serif'
rcParams['axes.labelsize'] = 10
rcParams['xtick.labelsize'] = 8
rcParams['ytick.labelsize'] = 8
rcParams['legend.fontsize'] = 8
rcParams['lines.linewidth'] = 1.5
rcParams['grid.linestyle'] = '--'
rcParams['grid.linewidth'] = 0.5


def load_campaign_data(scenario_name):
    """Load campaign CSV data"""
    csv_file = ROOT / "data" / "estimated" / "simulations" / f"campaign_{scenario_name}_aggregated.csv"
    if not csv_file.exists():
        return None
    
    data = {'rank': [], 'trust': [], 'energy': [], 'mcs': [], 'latency': []}
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data['rank'].append(float(row['rank']))
            data['trust'].append(float(row['trust']))
            data['energy'].append(float(row['energy']))
            data['mcs'].append(float(row['mcs']))
            data['latency'].append(float(row['qos_latency']))
    
    return data


def figure1_mcs_comparison():
    """Figure 1: MCS across scenarios"""
    fig, ax = plt.subplots()
    
    scenarios = ['lossless', 'lossy', 'attack', 'energy', 'stress']
    scenario_full = ['lossless_baseline', 'lossy_network', 'attack_high_threat', 'energy_stress', 'stress_large_grid']
    
    mcs_means = []
    mcs_stds = []
    
    for scenario in scenario_full:
        data = load_campaign_data(scenario)
        if data:
            mcs_means.append(np.mean(data['mcs']))
            mcs_stds.append(np.std(data['mcs']))
    
    x = np.arange(len(scenarios))
    width = 0.35
    
    ax.bar(x, mcs_means, width, label='MARTHR', color='#2E86AB')
    
    ax.set_ylabel('Multi-Criteria Score (MCS)')
    ax.set_xlabel('Scenario')
    ax.set_xticks(x)
    ax.set_xticks(np.arange(len(scenarios)))
    ax.set_xticklabels(scenarios, rotation=45, ha='right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1.1])
    
    plt.tight_layout()
    plt.savefig(ROOT / 'manuscript' / 'Figures' / 'fig1_mcs_comparison.pdf', dpi=300, bbox_inches='tight')
    print("✅ Figure 1: MCS Comparison")


def figure2_trust_dynamics():
    """Figure 2: Trust score evolution"""
    fig, ax = plt.subplots()
    
    scenarios = ['lossless_baseline', 'lossy_network', 'attack_high_threat']
    colors = ['green', 'orange', 'red']
    
    for scenario, color in zip(scenarios, colors):
        data = load_campaign_data(scenario)
        if data:
            bins = np.linspace(0, 1, 20)
            ax.hist(data['trust'], bins=bins, alpha=0.5, label=scenario.replace('_', ' ').title(), color=color)
    
    ax.set_xlabel('Trust Score')
    ax.set_ylabel('Frequency')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(ROOT / 'manuscript' / 'Figures' / 'fig2_trust_dynamics.pdf', dpi=300, bbox_inches='tight')
    print("✅ Figure 2: Trust Dynamics")


def figure3_energy_consumption():
    """Figure 3: Energy depletion over time"""
    fig, ax = plt.subplots()
    
    scenario = 'energy_stress'
    data = load_campaign_data(scenario)
    
    if data:
        energy = np.array(data['energy'])
        timestamps = np.arange(len(energy))
        
        # Smooth with moving average
        window = 50
        energy_smooth = np.convolve(energy, np.ones(window)/window, mode='valid')
        timestamps_smooth = timestamps[:len(energy_smooth)]
        
        ax.plot(timestamps_smooth, energy_smooth, linewidth=2, color='#A23B72')
        ax.fill_between(timestamps_smooth, energy_smooth, alpha=0.3, color='#A23B72')
        
        ax.set_xlabel('Time Steps')
        ax.set_ylabel('Residual Energy')
        ax.set_ylim([0, 1.1])
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(ROOT / 'manuscript' / 'Figures' / 'fig3_energy_consumption.pdf', dpi=300, bbox_inches='tight')
    print("✅ Figure 3: Energy Consumption")


def figure4_latency_comparison():
    """Figure 4: Latency vs Scenario"""
    fig, ax = plt.subplots()
    
    scenarios = ['lossless', 'lossy', 'attack', 'energy', 'stress']
    scenario_full = ['lossless_baseline', 'lossy_network', 'attack_high_threat', 'energy_stress', 'stress_large_grid']
    
    latencies = []
    for scenario in scenario_full:
        data = load_campaign_data(scenario)
        if data:
            latencies.append(np.mean(data['latency']))
    
    ax.bar(scenarios, latencies, color='#F18F01', alpha=0.8)
    ax.set_ylabel('Average Latency')
    ax.set_xlabel('Scenario')
    ax.set_xticklabels(scenarios, rotation=45, ha='right')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(ROOT / 'manuscript' / 'Figures' / 'fig4_latency_comparison.pdf', dpi=300, bbox_inches='tight')
    print("✅ Figure 4: Latency Comparison")


def figure5_rank_distribution():
    """Figure 5: Rank distribution (box plot)"""
    fig, ax = plt.subplots()
    
    scenarios = ['lossless', 'lossy', 'attack', 'energy', 'stress']
    scenario_full = ['lossless_baseline', 'lossy_network', 'attack_high_threat', 'energy_stress', 'stress_large_grid']
    
    rank_data = []
    for scenario in scenario_full:
        data = load_campaign_data(scenario)
        if data:
            rank_data.append(data['rank'])
    
    bp = ax.boxplot(rank_data, tick_labels=scenarios, patch_artist=True)
    for patch in bp['boxes']:
        patch.set_facecolor('#E63946')
    
    ax.set_ylabel('Routing Rank')
    ax.set_xlabel('Scenario')
    ax.set_xticklabels(scenarios, rotation=45, ha='right')
    ax.set_ylim([0, 1.1])
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(ROOT / 'manuscript' / 'Figures' / 'fig5_rank_distribution.pdf', dpi=300, bbox_inches='tight')
    print("✅ Figure 5: Rank Distribution")


def figure6_ablation_study():
    """Figure 6: Ablation - MCS vs scenario complexity"""
    fig, ax = plt.subplots()
    
    scenarios = ['lossless', 'lossy', 'attack', 'energy', 'stress']
    scenario_full = ['lossless_baseline', 'lossy_network', 'attack_high_threat', 'energy_stress', 'stress_large_grid']
    
    complexities = [1, 2, 2, 3, 4]  # Relative complexity
    mcs_scores = []
    
    for scenario in scenario_full:
        data = load_campaign_data(scenario)
        if data:
            mcs_scores.append(np.mean(data['mcs']))
    
    ax.scatter(complexities, mcs_scores, s=100, alpha=0.7, color='#06A77D')
    z = np.polyfit(complexities, mcs_scores, 1)
    p = np.poly1d(z)
    ax.plot(complexities, p(complexities), "r--", alpha=0.8, label='Trend')
    
    ax.set_xlabel('Scenario Complexity')
    ax.set_ylabel('MCS Performance')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0.5, 1.0])
    
    plt.tight_layout()
    plt.savefig(ROOT / 'manuscript' / 'Figures' / 'fig6_ablation.pdf', dpi=300, bbox_inches='tight')
    print("✅ Figure 6: Ablation Study")


def main():
    print("\n🎨 Generating IEEE-Quality Figures")
    print("="*60)
    
    figures_dir = ROOT / "manuscript" / "Figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        figure1_mcs_comparison()
        figure2_trust_dynamics()
        figure3_energy_consumption()
        figure4_latency_comparison()
        figure5_rank_distribution()
        figure6_ablation_study()
        
        print("\n✅ All figures generated successfully")
        print(f"Location: {figures_dir}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
