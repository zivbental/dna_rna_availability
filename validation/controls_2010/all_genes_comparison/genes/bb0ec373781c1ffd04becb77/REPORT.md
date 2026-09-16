# YJL081C
Status: ok. Length: 1623 nt. Measured usable bases: 882. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 882 | 0.3148 | 0.3130 |
| rnafold | ok | 882 | 0.2626 | 0.2848 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 231 | -0.4265 | -0.5854 |
| seed_p | 231 | -0.5302 | -0.5364 |
| seed_p_vs_seed_pars | 192 | -0.4639 | -0.4150 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
