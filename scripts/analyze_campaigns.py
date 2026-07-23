#!/usr/bin/env python3
"""
MARTHR Statistical Analysis - Ablation & Comparison
Generates tables and statistical tests for IEEE publication
"""

import os
import csv
import numpy as np
from pathlib import Path
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]


class CampaignAnalyzer:
    """Analyze simulation campaign results"""
    
    def __init__(self, campaign_dir=None):
        self.campaign_dir = Path(campaign_dir) if campaign_dir else ROOT / "data" / "estimated" / "simulations"
        self.results = {}
        self.load_campaigns()
    
    def load_campaigns(self):
        """Load all campaign CSV files"""
        for csv_file in self.campaign_dir.glob("campaign_*.csv"):
            scenario_name = csv_file.stem.replace("campaign_", "").replace("_aggregated", "")
            with open(csv_file) as f:
                reader = csv.DictReader(f)
                self.results[scenario_name] = [row for row in reader]
        print(f"✅ Loaded {len(self.results)} scenarios")
    
    def extract_metrics(self, scenario_name):
        """Extract numeric metrics from a scenario"""
        if scenario_name not in self.results:
            return None
        
        data = self.results[scenario_name]
        metrics = {
            'rank': np.array([float(row['rank']) for row in data]),
            'trust': np.array([float(row['trust']) for row in data]),
            'energy': np.array([float(row['energy']) for row in data]),
            'mcs': np.array([float(row['mcs']) for row in data]),
            'latency': np.array([float(row['qos_latency']) for row in data]),
        }
        return metrics
    
    def baseline_mrhof(self):
        """Load MRHOF baseline results if available."""
        import csv
        mrhof_files = {
            'lossless': 'campaign_mrhof_lossless_aggregated.csv',
            'lossy': 'campaign_mrhof_lossy_aggregated.csv',
            'attack': 'campaign_mrhof_attack_aggregated.csv',
        }
        results = {}
        for scenario, filename in mrhof_files.items():
            path = self.simulations_dir / filename
            if path.exists():
                with open(path) as f:
                    reader = csv.DictReader(f)
                    rows = list(reader)
                results[scenario] = {
                    m: [float(r[m]) for r in rows if r.get(m)]
                    for m in ['rank', 'trust', 'energy', 'mcs', 'qos_latency']
                }
        if not results:
            return None
        return results
    
    def statistical_test(self, scenario1_metrics, scenario2_metrics, metric_name):
        """Mann-Whitney U test (non-parametric)"""
        data1 = scenario1_metrics[metric_name]
        data2 = scenario2_metrics[metric_name]
        
        statistic, pvalue = stats.mannwhitneyu(data1, data2, alternative='two-sided')
        
        mean1 = np.mean(data1)
        mean2 = np.mean(data2)
        improvement = ((mean1 - mean2) / mean2 * 100) if mean2 != 0 else 0
        
        return {
            'metric': metric_name,
            'mean_marthr': round(mean1, 4),
            'mean_baseline': round(mean2, 4),
            'improvement_percent': round(improvement, 2),
            'pvalue': round(pvalue, 6),
            'significant': 'YES' if pvalue < 0.05 else 'NO'
        }
    
    def generate_comparison_table(self):
        """Generate Table 1: MARTHR vs MRHOF baseline"""
        print("\n" + "="*100)
        print("TABLE 1: MARTHR vs MRHOF Baseline (5 scenarios, Mann-Whitney U test)")
        print("="*100)
        
        scenarios = list(self.results.keys())
        baseline = self.baseline_mrhof()
        
        all_results = []
        
        for scenario in scenarios:
            metrics = self.extract_metrics(scenario)
            if not metrics:
                continue
            
            print(f"\n{scenario.upper()}")
            print("-" * 100)
            print(f"{'Metric':<15} {'MARTHR Mean':<15} {'MRHOF Baseline':<15} {'Improvement %':<15} {'p-value':<12} {'Significant':<12}")
            print("-" * 100)
            
            for metric_name in ['rank', 'trust', 'energy', 'mcs', 'latency']:
                baseline_data = baseline[metric_name]
                
                # Create a dictionary with baseline data for statistical test
                baseline_metrics = {metric_name: baseline_data}
                
                result = self.statistical_test(metrics, baseline_metrics, metric_name)
                result['scenario'] = scenario
                all_results.append(result)
                
                print(f"{metric_name:<15} {result['mean_marthr']:<15.4f} {result['mean_baseline']:<15.4f} "
                      f"{result['improvement_percent']:<15.2f}% {result['pvalue']:<12.6f} {result['significant']:<12}")
        
        return all_results
    
    def generate_ablation_table(self):
        """Generate Table 2: Ablation study (individual component impact)"""
        print("\n" + "="*100)
        print("TABLE 2: Ablation Study - Individual Component Impact on MCS")
        print("="*100)
        
        # Simple ablation: compare scenarios
        scenarios = list(self.results.keys())
        
        print(f"\n{'Scenario':<30} {'Mean MCS':<15} {'Std Dev':<15} {'Min':<10} {'Max':<10}")
        print("-" * 100)
        
        ablation_results = []
        for scenario in scenarios:
            metrics = self.extract_metrics(scenario)
            if not metrics:
                continue
            
            mcs = metrics['mcs']
            result = {
                'scenario': scenario,
                'mean_mcs': round(np.mean(mcs), 4),
                'std_mcs': round(np.std(mcs), 4),
                'min_mcs': round(np.min(mcs), 4),
                'max_mcs': round(np.max(mcs), 4),
            }
            ablation_results.append(result)
            
            print(f"{scenario:<30} {result['mean_mcs']:<15.4f} {result['std_mcs']:<15.4f} "
                  f"{result['min_mcs']:<10.4f} {result['max_mcs']:<10.4f}")
        
        return ablation_results
    
    def generate_summary_stats(self):
        """Generate Table 3: Summary statistics per scenario"""
        print("\n" + "="*100)
        print("TABLE 3: Summary Statistics - All Metrics Across Scenarios")
        print("="*100)
        
        summary_data = []
        for scenario in sorted(self.results.keys()):
            metrics = self.extract_metrics(scenario)
            if not metrics:
                continue
            
            print(f"\n{scenario.upper()}")
            print("-" * 100)
            print(f"{'Metric':<15} {'Mean':<12} {'Std Dev':<12} {'Min':<12} {'Max':<12} {'Q1':<12} {'Median':<12}")
            print("-" * 100)
            
            for metric_name in ['rank', 'trust', 'energy', 'mcs', 'latency']:
                data = metrics[metric_name]
                result = {
                    'scenario': scenario,
                    'metric': metric_name,
                    'mean': round(np.mean(data), 4),
                    'std': round(np.std(data), 4),
                    'min': round(np.min(data), 4),
                    'max': round(np.max(data), 4),
                    'q1': round(np.percentile(data, 25), 4),
                    'median': round(np.median(data), 4),
                }
                summary_data.append(result)
                
                print(f"{metric_name:<15} {result['mean']:<12.4f} {result['std']:<12.4f} "
                      f"{result['min']:<12.4f} {result['max']:<12.4f} {result['q1']:<12.4f} {result['median']:<12.4f}")
        
        return summary_data
    
    def export_tables_csv(self):
        """Export all tables to CSV"""
        output_dir = ROOT / "data" / "estimated"
        
        # Table 3: descriptive statistics only. Comparison and ablation
        # tables are generated by dedicated scripts from documented inputs.
        summary_table = self.generate_summary_stats()
        with open(output_dir / "table3_summary.csv", 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=summary_table[0].keys())
            writer.writeheader()
            writer.writerows(summary_table)
        
        print(f"\n✅ Exported tables to {output_dir}")


def main():
    print("\n🔬 MARTHR Statistical Analysis")
    print("="*100)
    
    analyzer = CampaignAnalyzer()
    
    # Generate all tables
    analyzer.export_tables_csv()
    
    print("\n✅ Analysis complete")


if __name__ == "__main__":
    main()
