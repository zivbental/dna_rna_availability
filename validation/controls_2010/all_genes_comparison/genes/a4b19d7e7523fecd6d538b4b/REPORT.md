# YDR079C-A
Status: ok. Length: 444 nt. Measured usable bases: 224. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 224 | 0.4342 | 0.4432 |
| rnafold | ok | 224 | 0.4098 | 0.4210 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 59 | -0.5007 | -0.7689 |
| seed_p | 59 | 0.3085 | 0.0832 |
| seed_p_vs_seed_pars | 41 | 0.3775 | 0.2798 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
