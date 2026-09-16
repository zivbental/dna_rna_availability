# YNL058C
Status: ok. Length: 1056 nt. Measured usable bases: 470. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 470 | 0.2993 | 0.3019 |
| rnafold | ok | 470 | 0.1952 | 0.2087 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | -0.2167 | -0.5037 |
| seed_p | 49 | -0.7091 | -0.7493 |
| seed_p_vs_seed_pars | 32 | -0.7762 | -0.8687 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
