# YHR074W
Status: ok. Length: 2282 nt. Measured usable bases: 1654. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1654 | 0.3251 | 0.3160 |
| rnafold | ok | 1654 | 0.2584 | 0.2606 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1103 | -0.1171 | -0.0236 |
| seed_p | 1103 | -0.1353 | -0.1241 |
| seed_p_vs_seed_pars | 879 | -0.3041 | -0.2948 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
