# YPL220W
Status: ok. Length: 826 nt. Measured usable bases: 151. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 151 | 0.2622 | 0.2923 |
| rnafold | ok | 151 | 0.1859 | 0.1796 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | -0.4473 | -0.3677 |
| seed_p | 101 | -0.8420 | -0.7529 |
| seed_p_vs_seed_pars | 90 | -0.4167 | -0.2003 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
