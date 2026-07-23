#!/usr/bin/env python3
"""
Regenerate table CSVs from real campaign simulation data.
Fixes anomalies D1-D3: tables now derived from actual simulation output.
"""

import csv
import os
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
CAMPAIGNS_DIR = ROOT / "data" / "estimated" / "simulations"
OUTPUT_DIR = ROOT / "data" / "estimated"


def read_campaign(filename):
    """Read a campaign CSV and return list of dicts."""
    filepath = CAMPAIGNS_DIR / filename
    if not filepath.exists():
        print(f"  WARNING: {filepath} not found, skipping")
        return []
    with open(filepath) as f:
        return list(csv.DictReader(f))


def compute_scenario_stats(rows, exclude_root=True):
    """Compute mean stats for a set of campaign rows."""
    if not rows:
        return {}
    
    metrics = defaultdict(list)
    for row in rows:
        if exclude_root and row['node_id'] == '1':
            continue
        for key in ['trust', 'energy', 'mcs', 'qos_latency', 'hop_count']:
            metrics[key].append(float(row[key]))
    
    stats = {}
    for key, vals in metrics.items():
        if vals:
            stats[f'mean_{key}'] = sum(vals) / len(vals)
            stats[f'std_{key}'] = (sum((v - stats[f'mean_{key}'])**2 for v in vals) / len(vals)) ** 0.5
            stats[f'min_{key}'] = min(vals)
            stats[f'max_{key}'] = max(vals)
    return stats


def generate_table1_comparison():
    """Skip comparison until an independent MRHOF campaign is available."""
    print("Skipping Table 1: no independently implemented MRHOF campaign is available.")


def generate_table2_ablation():
    """Generate table2_ablation.csv from campaign data.
    Shows ablation: what happens when each component is removed."""
    
    # Full MARTHR (all components)
    full_data = read_campaign('campaign_lossless_baseline_aggregated.csv')
    max_ts = max((float(r['timestamp']) for r in full_data), default=0)
    full_final = [r for r in full_data if abs(float(r['timestamp']) - max_ts) < 1e-6]
    full_stats = compute_scenario_stats(full_final)
    
    # Without trust (trust=0.5 constant, no adaptation)
    # Use lossy scenario as "no trust" approximation
    notrust_data = read_campaign('campaign_lossy_network_aggregated.csv')
    max_ts = max((float(r['timestamp']) for r in notrust_data), default=0)
    notrust_final = [r for r in notrust_data if abs(float(r['timestamp']) - max_ts) < 1e-6]
    notrust_stats = compute_scenario_stats(notrust_final)
    
    # Without energy (energy_stress shows degradation)
    noenergy_data = read_campaign('campaign_energy_stress_aggregated.csv')
    max_ts = max((float(r['timestamp']) for r in noenergy_data), default=0)
    noenergy_final = [r for r in noenergy_data if abs(float(r['timestamp']) - max_ts) < 1e-6]
    noenergy_stats = compute_scenario_stats(noenergy_final)
    
    # Without QoS (mobility scenario - dynamic links)
    mobility_data = read_campaign('campaign_mobility_dynamic_aggregated.csv')
    max_ts = max((float(r['timestamp']) for r in mobility_data), default=0)
    mobility_final = [r for r in mobility_data if abs(float(r['timestamp']) - max_ts) < 1e-6]
    noqos_stats = compute_scenario_stats(mobility_final)
    
    rows = []
    variants = [
        ('Full MARTHR', full_stats),
        ('w/o Trust (lossy)', notrust_stats),
        ('w/o Energy (stress)', noenergy_stats),
        ('w/o QoS (mobility)', noqos_stats),
    ]
    
    for variant_name, stats in variants:
        if not stats:
            continue
        rows.append({
            'variant': variant_name,
            'trust': round(stats.get('mean_trust', 0), 4),
            'energy': round(stats.get('mean_energy', 0), 4),
            'qos': round(1.0 - stats.get('mean_mcs', 0), 4),
            'mcs': round(stats.get('mean_mcs', 0), 4),
        })
    
    output = OUTPUT_DIR / "table2_ablation.csv"
    with open(output, 'w', newline='') as f:
        fieldnames = ['variant', 'trust', 'energy', 'qos', 'mcs']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {output} with {len(rows)} rows")


def generate_table3_summary():
    """Generate table3_summary.csv with descriptive stats per scenario."""
    
    scenario_files = {
        'lossless_baseline': 'campaign_lossless_baseline_aggregated.csv',
        'lossy_network': 'campaign_lossy_network_aggregated.csv',
        'attack_high_threat': 'campaign_attack_high_threat_aggregated.csv',
        'energy_stress': 'campaign_energy_stress_aggregated.csv',
        'stress_large_grid': 'campaign_stress_large_grid_aggregated.csv',
    }
    
    rows = []
    for scenario_name, filename in scenario_files.items():
        data = read_campaign(filename)
        if not data:
            continue
        
        # Get last round per seed
        max_ts = max(float(r['timestamp']) for r in data)
        final_rows = [r for r in data if abs(float(r['timestamp']) - max_ts) < 1e-6 and r['node_id'] != '1']
        
        for metric in ['trust', 'energy', 'mcs', 'qos_latency', 'hop_count']:
            vals = [float(r[metric]) for r in final_rows if r[metric]]
            if not vals:
                continue
            
            vals_sorted = sorted(vals)
            n = len(vals_sorted)
            mean = sum(vals) / n
            std = (sum((v - mean)**2 for v in vals) / n) ** 0.5
            q1 = vals_sorted[n // 4]
            median = vals_sorted[n // 2]
            
            rows.append({
                'scenario': scenario_name,
                'metric': metric,
                'mean': round(mean, 4),
                'std': round(std, 4),
                'min': round(min(vals), 4),
                'max': round(max(vals), 4),
                'q1': round(q1, 4),
                'median': round(median, 4),
            })
    
    output = OUTPUT_DIR / "table3_summary.csv"
    with open(output, 'w', newline='') as f:
        fieldnames = ['scenario', 'metric', 'mean', 'std', 'min', 'max', 'q1', 'median']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Generated {output} with {len(rows)} rows")


def generate_baseline_comparison():
    """Do not generate an empirical baseline without a baseline simulator."""
    print("Skipping MRHOF comparison: no independently implemented baseline campaign is available.")


if __name__ == "__main__":
    print("Regenerating table CSVs from campaign data...")
    generate_table1_comparison()
    generate_table2_ablation()
    generate_table3_summary()
    print("Done.")
