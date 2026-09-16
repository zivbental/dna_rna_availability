# YOR115C
Status: ok. Length: 937 nt. Measured usable bases: 400. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 400 | 0.3311 | 0.3225 |
| rnafold | ok | 400 | 0.3126 | 0.3010 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | 0.5188 | -0.1813 |
| seed_p | 45 | -0.2930 | -0.0926 |
| seed_p_vs_seed_pars | 37 | -0.5600 | -0.1985 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
