# YDR002W
Status: ok. Length: 852 nt. Measured usable bases: 693. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 693 | 0.3465 | 0.3445 |
| rnafold | ok | 693 | 0.3539 | 0.3572 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 625 | 0.0003 | -0.3181 |
| seed_p | 625 | -0.1624 | -0.3266 |
| seed_p_vs_seed_pars | 530 | -0.1911 | -0.4015 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
