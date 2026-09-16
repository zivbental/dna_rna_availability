# YDR482C
Status: ok. Length: 688 nt. Measured usable bases: 310. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 310 | 0.3780 | 0.3805 |
| rnafold | ok | 310 | 0.3877 | 0.3945 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | -0.1899 | -0.7191 |
| seed_p | 82 | -0.5364 | -0.6172 |
| seed_p_vs_seed_pars | 48 | -0.7121 | -0.4855 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
