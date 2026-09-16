# YKL028W
Status: ok. Length: 1789 nt. Measured usable bases: 534. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 534 | 0.2687 | 0.2456 |
| rnafold | ok | 534 | 0.2693 | 0.2322 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 27 | -0.3029 | -0.1983 |
| seed_p | 27 | -0.5949 | -0.6962 |
| seed_p_vs_seed_pars | 9 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
