# YGR132C
Status: ok. Length: 1201 nt. Measured usable bases: 801. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 801 | 0.3323 | 0.3180 |
| rnafold | ok | 801 | 0.2908 | 0.2900 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 511 | -0.1040 | 0.0261 |
| seed_p | 511 | 0.0097 | 0.0546 |
| seed_p_vs_seed_pars | 423 | 0.1000 | 0.0621 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
