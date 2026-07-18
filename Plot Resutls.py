"""
plot_results.py
Reads results.csv (produced by cache.cpp) and generates the hit-ratio
vs associativity figure used in the report.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('results.csv')

sns.set_theme(style="whitegrid")

colors = {
    'memGen1': '#4c72b0', 'memGen2': '#dd8452', 'memGen3': '#55a868',
    'memGen4': '#c44e52', 'memGen5': '#8172b3', 'memGen6': '#8c564b'
}

left_gens = ['memGen1', 'memGen3', 'memGen4']
right_gens = ['memGen2', 'memGen5', 'memGen6']

left_labels = {
    'memGen1': 'memGen1 (K=2 conflict)',
    'memGen3': 'memGen3 (K=8 conflict)',
    'memGen4': 'memGen4 (K=4 conflict, 16 sets)'
}
right_labels = {
    'memGen2': 'memGen2 (random)',
    'memGen5': 'memGen5 (sequential)',
    'memGen6': 'memGen6 (stack)'
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8), dpi=300)

df_left = df[df['generator'].isin(left_gens)].copy()
df_left['legend_name'] = df_left['generator'].map(left_labels)
sns.lineplot(
    data=df_left, x='ways', y='hit_ratio', hue='legend_name',
    marker='o', linewidth=3, markersize=10, ax=ax1,
    palette={left_labels[k]: colors[k] for k in left_gens}
)

for gen, ways, y_off in [('memGen1', 1, 0.03), ('memGen3', 2, 0.04),
                         ('memGen4', 2, 0.17), ('memGen1', 2, 1.03),
                         ('memGen3', 4, 0.21), ('memGen4', 4, 1.03),
                         ('memGen3', 8, 1.03), ('memGen1', 16, 1.03)]:
    val = df[(df.generator == gen) & (df.ways == ways)].hit_ratio.values[0]
    ax1.text(ways, y_off, f"{val*100:.1f}%", ha='center', va='bottom',
             fontsize=9, fontweight='bold')

ax1.set_title('Conflict-Limited Generators\n(step functions)', fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Associativity (Ways)', fontsize=12)
ax1.set_ylabel('Hit Ratio', fontsize=12)
ax1.set_xticks([1, 2, 4, 8, 16])
ax1.set_ylim(-0.05, 1.15)
ax1.legend(loc='lower right', fontsize=10)

df_right = df[df['generator'].isin(right_gens)].copy()
df_right['legend_name'] = df_right['generator'].map(right_labels)
sns.lineplot(
    data=df_right, x='ways', y='hit_ratio', hue='legend_name',
    marker='o', linewidth=3, markersize=10, ax=ax2,
    palette={right_labels[k]: colors[k] for k in right_gens}
)

for gen, y_off in [('memGen6', 1.03), ('memGen5', 0.95), ('memGen2', 0.03)]:
    val = df[(df.generator == gen) & (df.ways == 1)].hit_ratio.values[0]
    ax2.text(1, y_off, f"{val*100:.2f}%", ha='center', va='bottom',
             fontsize=9, fontweight='bold')

ax2.set_title('Capacity/Locality-Limited Generators\n(flat curves)', fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Associativity (Ways)', fontsize=12)
ax2.set_ylabel('Hit Ratio', fontsize=12)
ax2.set_xticks([1, 2, 4, 8, 16])
ax2.set_ylim(-0.05, 1.15)
ax2.legend(loc='center right', fontsize=10)

plt.suptitle('Cache Hit Ratio vs. Associativity (Ways)', fontsize=18, fontweight='bold', y=0.96)
plt.figtext(0.5, 0.02,
            "Left: hit ratio jumps sharply once ways reaches each generator's conflict count (2, 8, 4).\n"
            "Right: hit ratio is insensitive to associativity, limited instead by capacity, spatial locality, or working-set size.",
            ha="center", fontsize=11, style='italic')

plt.tight_layout(rect=[0, 0.06, 1, 0.93])
plt.savefig('hit_ratio_split_panels.png', dpi=300, bbox_inches='tight')
plt.show()