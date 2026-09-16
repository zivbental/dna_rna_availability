# YDL052C
Status: ok. Length: 1011 nt. Measured usable bases: 685. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 685 | 0.2386 | 0.2167 |
| rnafold | ok | 685 | 0.2635 | 0.2286 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 392 | 0.1863 | 0.1154 |
| seed_p | 392 | 0.1955 | 0.1301 |
| seed_p_vs_seed_pars | 299 | 0.0907 | -0.1501 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
