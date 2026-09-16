# YLR324W
Status: ok. Length: 1859 nt. Measured usable bases: 715. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 715 | 0.2735 | 0.2635 |
| rnafold | ok | 715 | 0.2351 | 0.2398 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 75 | 0.0651 | 0.0448 |
| seed_p | 75 | 0.2852 | 0.3234 |
| seed_p_vs_seed_pars | 47 | 0.1531 | 0.1426 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
