# YMR251W-A
Status: ok. Length: 412 nt. Measured usable bases: 192. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 192 | 0.3476 | 0.3376 |
| rnafold | ok | 192 | 0.3199 | 0.2977 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 154 | -0.5190 | -0.3880 |
| seed_p | 154 | -0.4308 | -0.4142 |
| seed_p_vs_seed_pars | 136 | -0.4104 | -0.3604 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
