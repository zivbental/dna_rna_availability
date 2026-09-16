# YKR088C
Status: ok. Length: 1078 nt. Measured usable bases: 700. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 700 | 0.2437 | 0.2212 |
| rnafold | ok | 700 | 0.2082 | 0.1838 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 355 | -0.0913 | -0.1443 |
| seed_p | 355 | -0.0500 | -0.1290 |
| seed_p_vs_seed_pars | 281 | -0.2496 | -0.3046 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
