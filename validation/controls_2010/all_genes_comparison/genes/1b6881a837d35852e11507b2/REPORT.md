# YMR110C
Status: ok. Length: 1763 nt. Measured usable bases: 852. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 852 | 0.2510 | 0.2471 |
| rnafold | ok | 852 | 0.2099 | 0.2263 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 211 | -0.1736 | -0.1759 |
| seed_p | 211 | -0.2718 | -0.3986 |
| seed_p_vs_seed_pars | 146 | -0.4621 | -0.4310 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
