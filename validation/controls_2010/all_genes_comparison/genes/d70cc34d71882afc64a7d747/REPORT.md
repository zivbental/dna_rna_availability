# YHR147C
Status: ok. Length: 799 nt. Measured usable bases: 353. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 353 | 0.2717 | 0.2904 |
| rnafold | ok | 353 | 0.2484 | 0.2843 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 63 | 0.2414 | 0.0871 |
| seed_p | 63 | -0.5376 | -0.1696 |
| seed_p_vs_seed_pars | 55 | -0.7673 | -0.2412 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
