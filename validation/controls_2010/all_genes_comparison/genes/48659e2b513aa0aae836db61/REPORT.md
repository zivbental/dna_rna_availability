# YHL025W
Status: ok. Length: 1133 nt. Measured usable bases: 614. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 614 | 0.4522 | 0.4399 |
| rnafold | ok | 614 | 0.2967 | 0.3003 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 178 | -0.1008 | -0.2965 |
| seed_p | 178 | -0.5419 | -0.5597 |
| seed_p_vs_seed_pars | 115 | -0.8193 | -0.6431 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
