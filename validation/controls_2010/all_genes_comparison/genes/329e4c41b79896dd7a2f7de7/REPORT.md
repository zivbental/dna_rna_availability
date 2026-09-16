# YER094C
Status: ok. Length: 962 nt. Measured usable bases: 731. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 731 | 0.3415 | 0.3245 |
| rnafold | ok | 731 | 0.2575 | 0.2616 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 635 | -0.0205 | 0.0424 |
| seed_p | 635 | -0.1094 | 0.0305 |
| seed_p_vs_seed_pars | 586 | -0.2615 | -0.2835 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
