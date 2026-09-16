# YKR037C
Status: ok. Length: 1012 nt. Measured usable bases: 360. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 360 | 0.4057 | 0.3833 |
| rnafold | ok | 360 | 0.3629 | 0.3673 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 20 | -0.2592 | -0.4673 |
| seed_p | 20 | -0.9124 | -0.7269 |
| seed_p_vs_seed_pars | 11 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
