# YOR207C
Status: ok. Length: 3638 nt. Measured usable bases: 1696. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1696 | 0.3197 | 0.3182 |
| rnafold | ok | 1696 | 0.2903 | 0.2821 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 285 | 0.2942 | 0.0327 |
| seed_p | 285 | 0.3687 | 0.1622 |
| seed_p_vs_seed_pars | 210 | 0.4159 | 0.3250 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
