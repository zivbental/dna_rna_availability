# YBL071W-A
Status: ok. Length: 533 nt. Measured usable bases: 317. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 317 | 0.4115 | 0.4210 |
| rnafold | ok | 317 | 0.3728 | 0.3615 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 150 | -0.2679 | -0.3659 |
| seed_p | 150 | -0.4703 | -0.5266 |
| seed_p_vs_seed_pars | 123 | -0.4710 | -0.4453 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
