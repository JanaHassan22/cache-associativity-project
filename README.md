# Cache Associativity Simulator — CSCE 2303 Project 2

A set-associative cache simulator built for Project 2 (Effect of Associativity
on Cache Performance). Implements `initCache()` and `cacheAccess()` on top of
provided starter code and memory generators, then sweeps associativity
(1, 2, 4, 8, 16 ways) across six synthetic memory access patterns to study
how conflict, capacity, and spatial locality affect hit rate.

## Team

- Jana Hassan
- Sedra Elkhayat
- Sama Almallak

## Files

- `cache.cpp` — the simulator (cache implementation + experiment harness,
  provided starter code with `initCache`/`cacheAccess` implemented)
- `results.csv` — output of running `cache.cpp`, one row per
  (generator, ways) combination
- `plot_results.py` — generates the hit-ratio-vs-ways figure from
  `results.csv`
- `report.pdf` — full write-up (implementation, setup, results, analysis)

## Building and running the simulator

```bash
g++ -O2 -std=c++17 -o cache cache.cpp
./cache results.csv
```

This runs all 6 generators across all 5 associativities (30 runs,
1,000,000 accesses each) and writes `results.csv`.

## Generating the plots

```bash
pip install pandas matplotlib seaborn
python3 plot_results.py
```

Requires `results.csv` to be in the same directory.

## Cache configuration

| Parameter | Value |
|---|---|
| Cache size | 64 KB |
| Line size | 64 B |
| DRAM size | 64 MB |
| Associativity | 1, 2, 4, 8, 16 ways |
| Replacement | Random |
| Write policy | Write-back + write-allocate |

See `report.pdf` for the full implementation description, verification,
results, and analysis.
