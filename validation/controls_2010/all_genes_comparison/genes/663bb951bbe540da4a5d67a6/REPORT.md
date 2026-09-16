# YLR164W
Status: ok. Length: 749 nt. Measured usable bases: 257. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 257 | 0.1827 | 0.1783 |
| rnafold | ok | 257 | 0.1662 | 0.1850 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 48 | -0.4316 | -0.7047 |
| seed_p | 48 | -0.2893 | -0.4276 |
| seed_p_vs_seed_pars | 37 | -0.5446 | -0.5902 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
