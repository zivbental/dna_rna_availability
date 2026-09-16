# YGL112C
Status: ok. Length: 1695 nt. Measured usable bases: 936. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 936 | 0.2932 | 0.2923 |
| rnafold | ok | 936 | 0.2201 | 0.2030 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 236 | -0.0275 | -0.0292 |
| seed_p | 236 | -0.0871 | -0.2180 |
| seed_p_vs_seed_pars | 188 | -0.3272 | -0.3422 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
