# YBR165W
Status: ok. Length: 954 nt. Measured usable bases: 392. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 392 | 0.2769 | 0.2750 |
| rnafold | ok | 392 | 0.2730 | 0.2577 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | -0.0191 | 0.1456 |
| seed_p | 40 | 0.2693 | 0.1794 |
| seed_p_vs_seed_pars | 23 | 0.3016 | 0.3833 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
