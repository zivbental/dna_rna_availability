# YLR330W
Status: ok. Length: 2175 nt. Measured usable bases: 1120. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1120 | 0.3945 | 0.3914 |
| rnafold | ok | 1120 | 0.3292 | 0.3360 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 335 | -0.2504 | -0.1871 |
| seed_p | 335 | -0.1929 | -0.2048 |
| seed_p_vs_seed_pars | 260 | -0.1938 | -0.3058 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
