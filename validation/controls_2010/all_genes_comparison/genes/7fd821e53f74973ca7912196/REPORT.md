# YIR038C
Status: ok. Length: 828 nt. Measured usable bases: 549. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 549 | 0.2714 | 0.2607 |
| rnafold | ok | 549 | 0.3324 | 0.3116 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 257 | -0.0766 | 0.0529 |
| seed_p | 257 | -0.1851 | -0.2196 |
| seed_p_vs_seed_pars | 205 | -0.0953 | -0.0692 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
