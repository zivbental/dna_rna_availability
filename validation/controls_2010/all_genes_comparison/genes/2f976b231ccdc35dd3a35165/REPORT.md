# YOR128C
Status: ok. Length: 1787 nt. Measured usable bases: 992. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 992 | 0.3019 | 0.2706 |
| rnafold | ok | 992 | 0.3005 | 0.2931 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 287 | -0.3160 | -0.3038 |
| seed_p | 287 | -0.3627 | -0.4054 |
| seed_p_vs_seed_pars | 190 | -0.3943 | -0.4467 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
