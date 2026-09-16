# YGL187C
Status: ok. Length: 1196 nt. Measured usable bases: 642. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 642 | 0.3425 | 0.3056 |
| rnafold | ok | 642 | 0.3578 | 0.3214 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 468 | -0.1107 | -0.1193 |
| seed_p | 468 | -0.3436 | -0.3302 |
| seed_p_vs_seed_pars | 417 | -0.4588 | -0.3653 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
