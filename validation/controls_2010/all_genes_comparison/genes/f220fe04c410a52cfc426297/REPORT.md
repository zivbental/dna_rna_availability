# YNL173C
Status: ok. Length: 1217 nt. Measured usable bases: 470. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 470 | 0.4054 | 0.3904 |
| rnafold | ok | 470 | 0.3073 | 0.3300 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | 0.0056 | -0.1457 |
| seed_p | 60 | 0.0943 | -0.2386 |
| seed_p_vs_seed_pars | 54 | -0.2902 | -0.1661 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
