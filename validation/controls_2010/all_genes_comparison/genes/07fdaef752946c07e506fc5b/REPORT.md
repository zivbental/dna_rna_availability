# YJL186W
Status: ok. Length: 1875 nt. Measured usable bases: 1362. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1362 | 0.2838 | 0.2744 |
| rnafold | ok | 1362 | 0.2299 | 0.2211 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 877 | 0.1733 | 0.0649 |
| seed_p | 877 | -0.1136 | -0.1472 |
| seed_p_vs_seed_pars | 676 | -0.1952 | -0.1349 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
