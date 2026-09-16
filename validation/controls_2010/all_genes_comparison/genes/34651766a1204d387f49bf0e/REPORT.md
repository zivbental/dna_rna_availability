# YHR005C-A
Status: ok. Length: 438 nt. Measured usable bases: 337. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 337 | 0.3903 | 0.3617 |
| rnafold | ok | 337 | 0.3331 | 0.3412 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 293 | -0.3252 | -0.4337 |
| seed_p | 293 | -0.3929 | -0.3331 |
| seed_p_vs_seed_pars | 245 | -0.4892 | -0.5229 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
