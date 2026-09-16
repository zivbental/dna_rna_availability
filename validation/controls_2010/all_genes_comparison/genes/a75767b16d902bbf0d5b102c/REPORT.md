# YPL232W
Status: ok. Length: 1131 nt. Measured usable bases: 637. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 637 | 0.3453 | 0.3438 |
| rnafold | ok | 637 | 0.2812 | 0.2905 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 223 | 0.2276 | 0.4093 |
| seed_p | 223 | 0.1727 | 0.0651 |
| seed_p_vs_seed_pars | 144 | -0.0763 | -0.1709 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
