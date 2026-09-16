# YHR062C
Status: ok. Length: 993 nt. Measured usable bases: 568. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 568 | 0.3896 | 0.3902 |
| rnafold | ok | 568 | 0.3757 | 0.4015 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 193 | -0.3663 | -0.3857 |
| seed_p | 193 | -0.4790 | -0.3766 |
| seed_p_vs_seed_pars | 126 | -0.5562 | -0.4018 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
