# YHR104W
Status: ok. Length: 1212 nt. Measured usable bases: 745. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 745 | 0.3784 | 0.3716 |
| rnafold | ok | 745 | 0.3269 | 0.3179 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 331 | -0.0032 | 0.1345 |
| seed_p | 331 | -0.1697 | 0.0571 |
| seed_p_vs_seed_pars | 245 | -0.5223 | -0.2327 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
