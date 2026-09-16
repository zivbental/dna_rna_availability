# YGR244C
Status: ok. Length: 1474 nt. Measured usable bases: 842. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 842 | 0.4197 | 0.3914 |
| rnafold | ok | 842 | 0.2814 | 0.2722 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 289 | -0.1390 | -0.1891 |
| seed_p | 289 | -0.2358 | -0.3864 |
| seed_p_vs_seed_pars | 170 | -0.3584 | -0.5164 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
