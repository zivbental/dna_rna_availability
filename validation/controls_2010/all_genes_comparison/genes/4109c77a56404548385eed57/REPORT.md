# YIL110W
Status: ok. Length: 1739 nt. Measured usable bases: 732. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 732 | 0.3130 | 0.3007 |
| rnafold | ok | 732 | 0.2246 | 0.2222 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 265 | -0.0881 | 0.0351 |
| seed_p | 265 | -0.2754 | -0.2992 |
| seed_p_vs_seed_pars | 200 | -0.4944 | -0.5532 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
