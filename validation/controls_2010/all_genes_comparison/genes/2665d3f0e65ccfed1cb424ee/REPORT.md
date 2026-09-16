# YBR272C
Status: ok. Length: 1611 nt. Measured usable bases: 611. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 611 | 0.2429 | 0.2482 |
| rnafold | ok | 611 | 0.1853 | 0.1965 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | 0.5535 | 0.6883 |
| seed_p | 50 | 0.4717 | 0.4202 |
| seed_p_vs_seed_pars | 37 | 0.4893 | 0.4635 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
