# YOR065W
Status: ok. Length: 1547 nt. Measured usable bases: 682. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 682 | 0.3105 | 0.3131 |
| rnafold | ok | 682 | 0.2681 | 0.2596 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 183 | -0.6232 | -0.5168 |
| seed_p | 183 | -0.4001 | -0.4977 |
| seed_p_vs_seed_pars | 106 | -0.6399 | -0.6127 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
