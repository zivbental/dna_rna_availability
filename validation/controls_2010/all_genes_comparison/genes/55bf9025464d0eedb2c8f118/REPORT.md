# YIL062C
Status: ok. Length: 550 nt. Measured usable bases: 456. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 456 | 0.2350 | 0.2245 |
| rnafold | ok | 456 | 0.1778 | 0.1749 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 396 | 0.0607 | 0.1898 |
| seed_p | 396 | 0.0665 | 0.0162 |
| seed_p_vs_seed_pars | 355 | -0.0475 | -0.0923 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
