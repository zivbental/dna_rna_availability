# YJL167W
Status: ok. Length: 1211 nt. Measured usable bases: 1018. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1018 | 0.2922 | 0.2890 |
| rnafold | ok | 1018 | 0.2703 | 0.2669 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 897 | -0.1313 | -0.0785 |
| seed_p | 897 | -0.1091 | -0.1301 |
| seed_p_vs_seed_pars | 761 | -0.1513 | -0.1362 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
