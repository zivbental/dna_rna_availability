# YBL055C
Status: ok. Length: 1421 nt. Measured usable bases: 609. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 609 | 0.4325 | 0.3880 |
| rnafold | ok | 609 | 0.3805 | 0.3339 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | 0.2799 | 0.2956 |
| seed_p | 25 | 0.7175 | 0.6843 |
| seed_p_vs_seed_pars | 9 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
