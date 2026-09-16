# YKL145W
Status: ok. Length: 1618 nt. Measured usable bases: 819. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 819 | 0.3805 | 0.3595 |
| rnafold | ok | 819 | 0.2469 | 0.2406 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 615 | -0.1436 | -0.2614 |
| seed_p | 615 | -0.2269 | -0.2348 |
| seed_p_vs_seed_pars | 495 | -0.4323 | -0.4547 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
