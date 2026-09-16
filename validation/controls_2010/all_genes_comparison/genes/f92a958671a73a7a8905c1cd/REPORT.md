# YNL330C
Status: ok. Length: 1389 nt. Measured usable bases: 732. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 732 | 0.3714 | 0.3748 |
| rnafold | ok | 732 | 0.3025 | 0.3027 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 212 | -0.1350 | -0.4169 |
| seed_p | 212 | 0.2183 | 0.0071 |
| seed_p_vs_seed_pars | 169 | -0.0582 | -0.0561 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
