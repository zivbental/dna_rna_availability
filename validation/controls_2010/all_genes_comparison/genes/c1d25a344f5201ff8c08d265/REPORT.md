# YKL006W
Status: ok. Length: 556 nt. Measured usable bases: 239. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 239 | 0.2194 | 0.1690 |
| rnafold | ok | 239 | 0.3018 | 0.2948 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.4213 | -0.4171 |
| seed_p | 143 | -0.6510 | -0.4715 |
| seed_p_vs_seed_pars | 135 | -0.6337 | -0.4272 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
