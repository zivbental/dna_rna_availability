# YCL011C
Status: ok. Length: 1385 nt. Measured usable bases: 1015. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1015 | 0.3099 | 0.3034 |
| rnafold | ok | 1015 | 0.2908 | 0.2991 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 701 | -0.0015 | -0.2307 |
| seed_p | 701 | -0.2497 | -0.3314 |
| seed_p_vs_seed_pars | 591 | -0.2596 | -0.3220 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
