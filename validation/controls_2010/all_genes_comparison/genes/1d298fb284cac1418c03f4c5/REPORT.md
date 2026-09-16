# YML103C
Status: ok. Length: 5056 nt. Measured usable bases: 2014. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2014 | 0.2788 | 0.2642 |
| rnafold | ok | 2014 | 0.2083 | 0.1992 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 205 | 0.1093 | 0.2768 |
| seed_p | 205 | -0.1791 | -0.1229 |
| seed_p_vs_seed_pars | 142 | -0.1366 | -0.0678 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
