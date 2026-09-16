# YHR078W
Status: ok. Length: 1857 nt. Measured usable bases: 899. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 899 | 0.3008 | 0.2900 |
| rnafold | ok | 899 | 0.2953 | 0.2893 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | 0.2969 | 0.0288 |
| seed_p | 79 | -0.1781 | -0.2568 |
| seed_p_vs_seed_pars | 42 | -0.1102 | -0.2840 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
