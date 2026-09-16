# YOL086W-A
Status: ok. Length: 344 nt. Measured usable bases: 207. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 207 | 0.4686 | 0.4820 |
| rnafold | ok | 207 | 0.2886 | 0.3159 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 105 | 0.1428 | -0.1362 |
| seed_p | 105 | -0.2326 | -0.4071 |
| seed_p_vs_seed_pars | 88 | -0.4241 | -0.4492 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
