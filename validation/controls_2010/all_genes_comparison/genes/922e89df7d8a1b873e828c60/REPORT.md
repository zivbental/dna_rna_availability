# YHR009C
Status: ok. Length: 1782 nt. Measured usable bases: 1132. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1132 | 0.3003 | 0.2772 |
| rnafold | ok | 1132 | 0.2432 | 0.2276 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 488 | -0.1621 | -0.0620 |
| seed_p | 488 | -0.2794 | -0.2214 |
| seed_p_vs_seed_pars | 371 | -0.4123 | -0.2194 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
