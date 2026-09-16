# YIL143C
Status: ok. Length: 2704 nt. Measured usable bases: 1116. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1116 | 0.3477 | 0.3280 |
| rnafold | ok | 1116 | 0.3005 | 0.2863 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 95 | 0.2742 | 0.1707 |
| seed_p | 95 | 0.1064 | 0.0961 |
| seed_p_vs_seed_pars | 61 | 0.1522 | 0.3050 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
