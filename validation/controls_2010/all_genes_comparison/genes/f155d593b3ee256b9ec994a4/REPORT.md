# YKR089C
Status: ok. Length: 2851 nt. Measured usable bases: 1131. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1131 | 0.2445 | 0.2438 |
| rnafold | ok | 1131 | 0.2009 | 0.2099 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 144 | 0.0380 | 0.1787 |
| seed_p | 144 | 0.1782 | 0.0832 |
| seed_p_vs_seed_pars | 85 | -0.0241 | -0.3063 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
