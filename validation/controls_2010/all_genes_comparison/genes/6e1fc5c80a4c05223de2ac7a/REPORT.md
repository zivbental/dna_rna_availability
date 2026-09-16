# YNL137C
Status: ok. Length: 1757 nt. Measured usable bases: 771. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 771 | 0.2972 | 0.3006 |
| rnafold | ok | 771 | 0.3156 | 0.3241 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 134 | 0.0520 | 0.0659 |
| seed_p | 134 | -0.2161 | -0.0783 |
| seed_p_vs_seed_pars | 115 | -0.3502 | -0.2137 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
