# YLR066W
Status: ok. Length: 702 nt. Measured usable bases: 410. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 410 | 0.2768 | 0.2594 |
| rnafold | ok | 410 | 0.3232 | 0.2959 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 216 | -0.2020 | -0.1218 |
| seed_p | 216 | -0.1111 | -0.0374 |
| seed_p_vs_seed_pars | 181 | -0.0805 | -0.0716 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
