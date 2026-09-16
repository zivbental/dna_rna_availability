# YDR352W
Status: ok. Length: 1286 nt. Measured usable bases: 766. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 766 | 0.2782 | 0.2576 |
| rnafold | ok | 766 | 0.2849 | 0.2741 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 358 | 0.0244 | 0.1933 |
| seed_p | 358 | -0.1225 | -0.1001 |
| seed_p_vs_seed_pars | 291 | -0.2864 | -0.3369 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
