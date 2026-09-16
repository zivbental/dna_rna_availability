# YBR126C
Status: ok. Length: 1653 nt. Measured usable bases: 1132. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1132 | 0.2327 | 0.2305 |
| rnafold | ok | 1132 | 0.2120 | 0.2373 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 580 | 0.0700 | 0.0672 |
| seed_p | 580 | -0.0415 | -0.0368 |
| seed_p_vs_seed_pars | 419 | -0.1702 | -0.0751 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
