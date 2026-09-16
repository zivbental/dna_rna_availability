# YGL126W
Status: ok. Length: 1435 nt. Measured usable bases: 1038. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1038 | 0.2923 | 0.2612 |
| rnafold | ok | 1038 | 0.2295 | 0.2266 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 856 | 0.0254 | -0.0309 |
| seed_p | 856 | 0.0230 | 0.0335 |
| seed_p_vs_seed_pars | 757 | -0.2052 | -0.2210 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
