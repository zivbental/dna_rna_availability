# YOL111C
Status: ok. Length: 805 nt. Measured usable bases: 499. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 499 | 0.2688 | 0.2564 |
| rnafold | ok | 499 | 0.2444 | 0.2396 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 229 | 0.0017 | -0.2712 |
| seed_p | 229 | -0.1142 | -0.2365 |
| seed_p_vs_seed_pars | 178 | -0.2165 | -0.2146 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
