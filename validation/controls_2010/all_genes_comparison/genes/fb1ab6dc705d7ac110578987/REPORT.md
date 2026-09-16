# YHR201C
Status: ok. Length: 1342 nt. Measured usable bases: 567. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 567 | 0.3650 | 0.3449 |
| rnafold | ok | 567 | 0.2686 | 0.2749 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.2050 | -0.2323 |
| seed_p | 58 | -0.3441 | 0.0918 |
| seed_p_vs_seed_pars | 35 | -0.3316 | 0.3101 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
