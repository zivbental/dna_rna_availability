# YOR247W
Status: ok. Length: 633 nt. Measured usable bases: 585. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 585 | 0.2835 | 0.2787 |
| rnafold | ok | 585 | 0.2871 | 0.2732 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 593 | -0.1071 | -0.1621 |
| seed_p | 593 | -0.0857 | -0.0838 |
| seed_p_vs_seed_pars | 555 | -0.1963 | -0.2306 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
