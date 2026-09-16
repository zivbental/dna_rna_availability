# YDR281C
Status: ok. Length: 466 nt. Measured usable bases: 199. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 199 | 0.3127 | 0.2915 |
| rnafold | ok | 199 | 0.2873 | 0.2801 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 27 | -0.4000 | -0.8197 |
| seed_p | 27 | -0.7088 | -0.5857 |
| seed_p_vs_seed_pars | 13 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
