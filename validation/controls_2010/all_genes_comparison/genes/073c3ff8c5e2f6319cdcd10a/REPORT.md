# YDR121W
Status: ok. Length: 794 nt. Measured usable bases: 337. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 337 | 0.5225 | 0.5282 |
| rnafold | ok | 337 | 0.5082 | 0.5119 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | -0.3599 | -0.7836 |
| seed_p | 71 | -0.7085 | -0.6935 |
| seed_p_vs_seed_pars | 51 | -0.8070 | -0.6088 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
