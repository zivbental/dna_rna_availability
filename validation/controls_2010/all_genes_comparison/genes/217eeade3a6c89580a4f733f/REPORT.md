# YML009C
Status: ok. Length: 362 nt. Measured usable bases: 217. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 217 | 0.5036 | 0.4786 |
| rnafold | ok | 217 | 0.4689 | 0.4401 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 106 | -0.0227 | -0.4710 |
| seed_p | 106 | -0.4044 | -0.4256 |
| seed_p_vs_seed_pars | 82 | -0.2741 | -0.2758 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
