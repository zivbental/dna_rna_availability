# YGR004W
Status: ok. Length: 1474 nt. Measured usable bases: 579. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 579 | 0.2879 | 0.2771 |
| rnafold | ok | 579 | 0.2079 | 0.2080 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | -0.6845 | -0.7556 |
| seed_p | 45 | -0.2081 | -0.4775 |
| seed_p_vs_seed_pars | 45 | -0.5409 | -0.7130 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
