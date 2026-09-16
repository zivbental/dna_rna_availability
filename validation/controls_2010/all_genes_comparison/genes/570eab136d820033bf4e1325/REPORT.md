# YNL157W
Status: ok. Length: 710 nt. Measured usable bases: 175. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 175 | 0.3019 | 0.2925 |
| rnafold | ok | 175 | 0.3587 | 0.3490 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 30 | -0.0983 | -0.1536 |
| seed_p | 30 | -0.1454 | -0.2099 |
| seed_p_vs_seed_pars | 11 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
