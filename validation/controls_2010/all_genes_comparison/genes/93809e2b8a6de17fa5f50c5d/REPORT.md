# YIL023C
Status: ok. Length: 1353 nt. Measured usable bases: 852. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 852 | 0.2678 | 0.2545 |
| rnafold | ok | 852 | 0.1234 | 0.1347 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 582 | -0.1458 | -0.2091 |
| seed_p | 582 | -0.1037 | -0.2132 |
| seed_p_vs_seed_pars | 435 | -0.2520 | -0.3190 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
