# YBR017C
Status: ok. Length: 2883 nt. Measured usable bases: 1371. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1371 | 0.3053 | 0.2881 |
| rnafold | ok | 1371 | 0.2723 | 0.2546 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 191 | 0.3502 | 0.3014 |
| seed_p | 191 | 0.1130 | 0.2594 |
| seed_p_vs_seed_pars | 158 | -0.2068 | 0.0686 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
