# YOR095C
Status: ok. Length: 995 nt. Measured usable bases: 699. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 699 | 0.3735 | 0.3561 |
| rnafold | ok | 699 | 0.2882 | 0.2608 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 464 | -0.2793 | -0.0969 |
| seed_p | 464 | -0.2735 | -0.2504 |
| seed_p_vs_seed_pars | 330 | -0.4143 | -0.3833 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
