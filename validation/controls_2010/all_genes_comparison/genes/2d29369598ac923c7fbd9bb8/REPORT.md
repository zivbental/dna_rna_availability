# YER012W
Status: ok. Length: 776 nt. Measured usable bases: 465. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 465 | 0.2829 | 0.2703 |
| rnafold | ok | 465 | 0.2675 | 0.2547 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 232 | -0.0743 | -0.2229 |
| seed_p | 232 | -0.2686 | -0.2822 |
| seed_p_vs_seed_pars | 176 | -0.4236 | -0.4463 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
