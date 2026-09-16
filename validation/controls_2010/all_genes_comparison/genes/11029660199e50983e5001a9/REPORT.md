# YNL121C
Status: ok. Length: 2002 nt. Measured usable bases: 1136. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1136 | 0.2670 | 0.2707 |
| rnafold | ok | 1136 | 0.2090 | 0.2248 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 311 | 0.1425 | 0.0646 |
| seed_p | 311 | -0.0220 | -0.0372 |
| seed_p_vs_seed_pars | 230 | 0.0439 | -0.0539 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
