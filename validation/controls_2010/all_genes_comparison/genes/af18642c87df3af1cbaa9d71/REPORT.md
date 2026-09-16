# YGL055W
Status: ok. Length: 1852 nt. Measured usable bases: 1453. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1453 | 0.3239 | 0.3228 |
| rnafold | ok | 1453 | 0.2880 | 0.2669 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1290 | -0.1322 | -0.1312 |
| seed_p | 1290 | -0.0461 | -0.0739 |
| seed_p_vs_seed_pars | 1169 | -0.0831 | -0.1120 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
