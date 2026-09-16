# YKL144C
Status: ok. Length: 1366 nt. Measured usable bases: 425. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 425 | 0.3356 | 0.3413 |
| rnafold | ok | 425 | 0.2397 | 0.2386 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 93 | 0.3155 | 0.2033 |
| seed_p | 93 | -0.2857 | -0.1204 |
| seed_p_vs_seed_pars | 77 | -0.6893 | -0.4730 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
