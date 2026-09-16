# YER186C
Status: ok. Length: 1101 nt. Measured usable bases: 531. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 531 | 0.3889 | 0.3778 |
| rnafold | ok | 531 | 0.2915 | 0.2854 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 86 | -0.2349 | -0.1289 |
| seed_p | 86 | -0.2124 | -0.1182 |
| seed_p_vs_seed_pars | 58 | -0.4927 | -0.6164 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
