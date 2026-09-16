# YMR047C
Status: ok. Length: 3487 nt. Measured usable bases: 1829. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1829 | 0.3739 | 0.3599 |
| rnafold | ok | 1829 | 0.3002 | 0.3092 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 403 | -0.4745 | -0.4283 |
| seed_p | 403 | -0.4389 | -0.3509 |
| seed_p_vs_seed_pars | 264 | -0.4636 | -0.3506 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
