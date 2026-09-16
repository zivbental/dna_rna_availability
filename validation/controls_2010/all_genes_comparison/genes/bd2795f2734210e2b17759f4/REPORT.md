# YML110C
Status: ok. Length: 1215 nt. Measured usable bases: 879. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 879 | 0.3670 | 0.3548 |
| rnafold | ok | 879 | 0.3249 | 0.3392 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 635 | -0.1943 | -0.3468 |
| seed_p | 635 | -0.2726 | -0.2888 |
| seed_p_vs_seed_pars | 514 | -0.3302 | -0.4255 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
