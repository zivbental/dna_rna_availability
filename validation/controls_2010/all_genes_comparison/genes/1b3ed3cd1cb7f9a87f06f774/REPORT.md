# YGR253C
Status: ok. Length: 868 nt. Measured usable bases: 614. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 614 | 0.3900 | 0.4031 |
| rnafold | ok | 614 | 0.2420 | 0.2525 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 402 | -0.1781 | -0.1824 |
| seed_p | 402 | -0.2679 | -0.2752 |
| seed_p_vs_seed_pars | 309 | -0.2226 | -0.2314 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
