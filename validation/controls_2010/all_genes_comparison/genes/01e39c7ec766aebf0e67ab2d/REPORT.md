# YDR410C
Status: ok. Length: 755 nt. Measured usable bases: 468. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 468 | 0.3277 | 0.3269 |
| rnafold | ok | 468 | 0.2944 | 0.3077 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 250 | -0.2350 | -0.1504 |
| seed_p | 250 | -0.2263 | -0.1803 |
| seed_p_vs_seed_pars | 162 | -0.2827 | -0.1158 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
