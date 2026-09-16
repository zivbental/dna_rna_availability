# YOL109W
Status: ok. Length: 537 nt. Measured usable bases: 443. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 443 | 0.4735 | 0.4792 |
| rnafold | ok | 443 | 0.4197 | 0.4356 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 395 | -0.1319 | -0.4476 |
| seed_p | 395 | -0.4425 | -0.4750 |
| seed_p_vs_seed_pars | 371 | -0.4182 | -0.3866 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
