# YNL101W
Status: ok. Length: 2510 nt. Measured usable bases: 1287. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1287 | 0.2971 | 0.2814 |
| rnafold | ok | 1287 | 0.2203 | 0.2179 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 233 | -0.3134 | -0.0229 |
| seed_p | 233 | -0.3587 | -0.1717 |
| seed_p_vs_seed_pars | 163 | -0.3665 | -0.1226 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
