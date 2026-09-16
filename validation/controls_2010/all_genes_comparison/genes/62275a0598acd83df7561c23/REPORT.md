# YER081W
Status: ok. Length: 1790 nt. Measured usable bases: 698. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 698 | 0.2121 | 0.2134 |
| rnafold | ok | 698 | 0.2270 | 0.2515 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 53 | 0.0298 | -0.2290 |
| seed_p | 53 | -0.2089 | 0.1630 |
| seed_p_vs_seed_pars | 33 | -0.5470 | 0.0873 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
