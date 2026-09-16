# YBR139W
Status: ok. Length: 1724 nt. Measured usable bases: 1002. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1002 | 0.2521 | 0.2480 |
| rnafold | ok | 1002 | 0.2426 | 0.2323 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 334 | -0.1501 | -0.1256 |
| seed_p | 334 | -0.3047 | -0.3628 |
| seed_p_vs_seed_pars | 233 | -0.4255 | -0.4049 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
