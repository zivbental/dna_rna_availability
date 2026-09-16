# YBR086C
Status: ok. Length: 3183 nt. Measured usable bases: 2145. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2145 | 0.2897 | 0.2769 |
| rnafold | ok | 2145 | 0.2538 | 0.2415 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1331 | -0.0870 | -0.0717 |
| seed_p | 1331 | -0.1918 | -0.1583 |
| seed_p_vs_seed_pars | 1055 | -0.2302 | -0.2200 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
