# YJL158C
Status: ok. Length: 876 nt. Measured usable bases: 747. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 747 | 0.2351 | 0.2152 |
| rnafold | ok | 747 | 0.1838 | 0.1913 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 691 | -0.0986 | -0.1534 |
| seed_p | 691 | -0.0460 | 0.0071 |
| seed_p_vs_seed_pars | 647 | -0.0455 | 0.0301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
