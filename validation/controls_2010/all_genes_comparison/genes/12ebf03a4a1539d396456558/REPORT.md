# YDL008W
Status: ok. Length: 623 nt. Measured usable bases: 315. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 315 | 0.3772 | 0.3649 |
| rnafold | ok | 315 | 0.3583 | 0.3568 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 109 | -0.4907 | -0.4134 |
| seed_p | 109 | -0.4326 | -0.3144 |
| seed_p_vs_seed_pars | 92 | -0.6718 | -0.6426 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
