# YJR147W
Status: ok. Length: 1425 nt. Measured usable bases: 756. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 756 | 0.2767 | 0.2851 |
| rnafold | ok | 756 | 0.2479 | 0.2430 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 171 | 0.2403 | 0.1816 |
| seed_p | 171 | -0.0690 | -0.1028 |
| seed_p_vs_seed_pars | 125 | -0.4008 | -0.4429 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
