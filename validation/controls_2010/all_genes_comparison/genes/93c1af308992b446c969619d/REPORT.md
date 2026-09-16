# YIL138C
Status: ok. Length: 829 nt. Measured usable bases: 403. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 403 | 0.3625 | 0.3619 |
| rnafold | ok | 403 | 0.3567 | 0.3615 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 130 | 0.3019 | 0.1547 |
| seed_p | 130 | 0.3115 | 0.3094 |
| seed_p_vs_seed_pars | 93 | 0.0404 | 0.0709 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
